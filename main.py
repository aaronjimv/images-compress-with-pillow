from PIL import Image
import os

def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension = os.path.splitext(image_folder + file)
            print("compressing images " + file_name)
    
    except:
        print("ERROR!!!")


if __name__ == '__main__':
    compress_images('to-compress/')
