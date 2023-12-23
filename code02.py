from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imag'
path_out = '/editedImags'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # Fix typo in ImageFilter
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    # Fix path_out and removed unnecessary dot in the path
    edit.save(f'{path_out}/{clean_name}_edited.jpg')
