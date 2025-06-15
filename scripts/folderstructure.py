import os
import shutil

source_images_root = 'C://Users//91887//Desktop//Python//yoloV8//Datasets//Images'  # this folder has 85 subfolders
source_labels = 'C://Users//91887//Desktop//Python//yoloV8//train'              # all your .txt files in one place
target_images = 'dataset/images/train'
target_labels = 'dataset/labels/train'

# Create output dirs
os.makedirs(target_images, exist_ok=True)
os.makedirs(target_labels, exist_ok=True)

# Collect and move
image_exts = ['.jpg', '.jpeg', '.png']

for folder in os.listdir(source_images_root):
    folder_path = os.path.join(source_images_root, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            name, ext = os.path.splitext(file)
            if ext.lower() in image_exts:
                # Move image
                src_img = os.path.join(folder_path, file)
                dst_img = os.path.join(target_images, file)
                shutil.copy2(src_img, dst_img)

                # Copy matching label
                txt_file = name + ".txt"
                src_lbl = os.path.join(source_labels, txt_file)
                dst_lbl = os.path.join(target_labels, txt_file)
                if os.path.exists(src_lbl):
                    shutil.copy2(src_lbl, dst_lbl)