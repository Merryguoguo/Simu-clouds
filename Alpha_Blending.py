from glob import glob
from turtle import mode
import cv2
import random
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
from torchvision import transforms
import argparse


def main(mode, lbl_dir, cld_dir, out_dir):
    '''
    The function includes two parts:
    1st: Alpha Blending of label and cloud (selected offLinux), get Simulated Cloudy Image
    2nd: Cloud Mask Generation of the corresponding simulated cloudy image, get Cloud Mask

    Input:
    mode: str, 'Train'/'Test'/'Val' 
    lbl_dir: str, the directory of label image, default: /mnt/data/guoyujun/RICE2/RICE2_split/label
    cld_dir: str, the directory of good cloud selected offLinux, default: /mnt/data/guoyujun/Cloud/Cloud
    out_dir: str, the directory where the outputs placed in, default: /mnt/data/guoyujun/RICE2/RICE2_split/...

    Output:
    cld_img: the simulated cloudy image
    img:     the label image
    cld:     the cloud
    msk:     the cloud binary mask generated
    '''

    img_paths = glob('{:s}/{:s}/*.png'.format(lbl_dir, mode), recursive=True)  # label image paths
    cld_paths = glob('{:s}/*.png'.format(cld_dir), recursive=True)             # good cloud paths

    save_dir = '{:s}/simulated_real_cloudy_4/{:s}'.format(out_dir, mode)
    save_img_dir = '{:s}/simulated_label_4/{:s}'.format(mode)
    save_cld_dir = '{:s}/simulated_cld_4/{:s}'.format(mode)
    save_msk_dir = '{:s}/cloud_mask_0/{:s}'.format(mode)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        os.makedirs(save_img_dir)    
        os.makedirs(save_cld_dir)  
        os.makedirs(save_msk_dir)     

    l = len(img_paths)
    c = len(cld_paths)

    for i in range(l):
        img = cv2.imread(img_paths[i])
        cld = cv2.imread(cld_paths[random.randrange(c)], -1).astype(np.float32)
        name = img_paths[i].split('\\')[6]
        
        save_path = os.path.join(save_dir, name)
        save_img_path = os.path.join(save_img_dir, name)
        save_cld_path = os.path.join(save_cld_dir, name)
        save_msk_path = os.path.join(save_msk_dir, name)
        
        # Alpha Blending
        alpha = cld[:, :, 3] / 255.
        alpha = np.broadcast_to(alpha[:, :, None], alpha.shape + (3,))
        cld_img = (1. - alpha) * img + alpha * cld[:, :, :3]
        cld_img = np.clip(cld_img, 0., 255.)
        
    #     # Color correction
    #     cld_img = cld_img / 127.5 - 1
    #     cld = cld_img.transpose(2, 0, 1)

        # Cloud Mask Generation
        cloud = cld[:,:,3:4]
        means = np.mean(cloud)
        msk = np.zeros((512, 512, 3))
        msk = np.where(cloud>=means/1.2, msk, 255)

        cv2.imwrite(save_path, cld_img)
        cv2.imwrite(save_img_path, img)    
        cv2.imwrite(save_cld_path, cld) 
        cv2.imwrite(save_msk_path, msk)    


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', '-m', type=str, default='Train')
    parser.add_argument('--lbl_dir', '-l', type=str, default='./')
    parser.add_argument('--cld_dir', '-c', type=str, default='./')
    parser.add_argument('--out_dir', '-o', type=str, default='./')

    args = parser.parse_args()

    main(args)


