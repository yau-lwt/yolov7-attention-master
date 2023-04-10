import os
from PIL import Image
def extract_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, filename in enumerate(os.listdir(input_dir)):
        if i % 13 == 0:
            with Image.open(os.path.join(input_dir, filename)) as im:
                im.save(os.path.join(output_dir, filename))
def extract_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, filename in enumerate(os.listdir(input_dir)):
        if i % 13 == 0:
            with Image.open(os.path.join(input_dir, filename)) as im:
                im.save(os.path.join(output_dir, filename))
input_dir = 'C:/Users/taotao/Desktop/data2/Brown_Spot'
output_dir = 'C:/Users/taotao/Desktop/data2/2'
extract_images(input_dir, output_dir)
