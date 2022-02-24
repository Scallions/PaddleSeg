# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from .dataset import Dataset
from paddleseg.cvlibs import manager
from paddleseg.transforms import Compose

import numpy as np
# from PIL import Image
# from skimage import io
import cv2 as cv
import paddleseg.transforms.functional as F


@manager.DATASETS.add_component
class AerialImage(Dataset):
    """
    Args:
        dataset_root (str, optional): The dataset directory. Default: None.
        transforms (list, optional): Transforms for image. Default: None.
        mode (str, optional): Which part of dataset to use. It is one of ('train', 'val'). Default: 'train'.
        edge (bool, optional): Whether to compute edge while training. Default: False.
    """
    NUM_CLASSES = 2

    def __init__(self,
                 dataset_root=None,
                 transforms=None,
                 mode='train',
                 edge=False):
        self.dataset_root = dataset_root
        self.transforms = Compose(transforms)
        mode = mode.lower()
        self.mode = mode
        self.file_list = list()
        self.num_classes = self.NUM_CLASSES
        self.ignore_index = 255
        self.edge = edge

        if mode not in ['train', 'val', 'test']:
            raise ValueError(
                "`mode` should be 'train', 'val' or 'test', but got {}.".format(
                    mode))

        if self.transforms is None:
            raise ValueError("`transforms` is necessary, but it is None.")

        if mode == 'train':
            file_path = os.path.join(self.dataset_root, 'train.txt')
        elif mode == 'val':
            file_path = os.path.join(self.dataset_root, 'val.txt')
        else:
            file_path = os.path.join(self.dataset_root, 'test.txt')

        with open(file_path, 'r') as f:
            for line in f:
                items = line.strip().split(' ')
                if len(items) != 2:
                    if mode == 'train' or mode == 'val':
                        raise Exception(
                            "File list format incorrect! It should be"
                            " image_name label_name\\n")
                    image_path = os.path.join(self.dataset_root, items[0])
                    grt_path = None
                else:
                    image_path = os.path.join(self.dataset_root, items[0])
                    grt_path = os.path.join(self.dataset_root, items[1])
                self.file_list.append([image_path, grt_path])

    def __getitem__(self, idx):
        image_path, label_path = self.file_list[idx]
        if self.mode == 'test':
            im = cv.imread(image_path)
            im, _ = self.transforms(im=im)
            im = im[np.newaxis, ...]
            return im, image_path
        elif self.mode == 'val':
            im = cv.imread(image_path)
            im, _ = self.transforms(im=im)
            label = cv.imread(label_path)[:,:,0]
            label = label[np.newaxis, :, :]
            return im, label
        else:
            im = cv.imread(image_path)
            label = cv.imread(label_path)[:,:,0]
            im, label = self.transforms(im=im, label=label)
            if self.edge:
                edge_mask = F.mask_to_binary_edge(
                    label, radius=2, num_classes=self.num_classes)
                return im, label, edge_mask
            else:
                return im, label