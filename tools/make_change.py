# 生成数据列表
import os

def creat_data_list(dataset_path, mode='train'):
    with open(os.path.join(dataset_path, (mode + '_list.txt')), 'w') as f:
        A_path = os.path.join(os.path.join(dataset_path, mode), 'A')
        A_imgs_name = os.listdir(A_path)  # 获取文件夹下的所有文件名
        A_imgs_name.sort()
        for A_img_name in A_imgs_name:
            A_img = os.path.join(A_path, A_img_name)
            B_img = os.path.join(A_path.replace('A', 'B'), A_img_name)
            label_img = os.path.join(A_path.replace('A', 'label'), A_img_name)
            f.write(A_img + ' ' + B_img + ' ' + label_img + '\n')  # 写入list.txt
    print(mode + '_data_list generated')

dataset_path = 'dataset/LEVIR-CD'  # data的文件夹
# 分别创建三个list.txt
creat_data_list(dataset_path, mode='train')
creat_data_list(dataset_path, mode='test')
creat_data_list(dataset_path, mode='val')