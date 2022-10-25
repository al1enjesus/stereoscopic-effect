import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--img', type=str, help='Path to image')
img_path = parser.parse_args().img

if __name__ == "__main__":
    os.system("rm -rf 3d-photo-inpainting/image/*")
    
    os.system(f"cp {img_path} 3d-photo-inpainting/image/")
    os.system("python 3d-photo-inpainting/main.py --config 3d-photo-inpainting/argument.yml")
    os.system(f"cp 3d-photo-inpainting/video/{img_path.split('/')[-1].split('.')[0]}_dolly-downshift-in.gif .")
