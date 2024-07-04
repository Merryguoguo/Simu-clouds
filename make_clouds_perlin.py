import os
import pdb
import numpy as np
import cv2
import argparse
from tqdm import tqdm

from PythonClouds.Clouds_perlinNoise import CloudManager

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ['CUDA_VISIBLE_DEVICES'] = '2'


def main(args):
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)
        print('{} was created'.format(args.out_dir))

    for i in tqdm(range(args.n_clouds)):
        cm = CloudManager()
        co = cm.GetObject(i * 256)
        cloud = co.Colours

        # # 256
        # cloud = np.array(co.Colours).reshape([256, 256, 4])
        # cloud = np.array(co.Colours).reshape([256, 256, 3])
        # # 512
        cloud = np.array(co.Colours).reshape([512, 512, 4]) 
        # cloud = np.array(co.Colours).reshape([512, 512, 3])
        cloud = (cloud * 255).astype(np.uint8)

        cv2.imwrite(os.path.join(args.out_dir, 'cloud_{:06d}.png'.format(i)), cloud)

    print('{} images made. done.'.format(i+1))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_clouds', '-n', type=int, default=30000)
    parser.add_argument('--out_dir', '-o', type=str, default='./')
    args = parser.parse_args()

    main(args)
