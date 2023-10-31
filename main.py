from PIL import Image
import os

def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension = os.path.splitext(image_folder + file)
            print("compressing images " + file_name + file_extension)

            if file_extension == '.jpg':
                file_compress = Image.open(image_folder + file)
                file_compress.save(
                    file_name + "_compress.jpg",
                    optimize=True,
                    quality=20
                )
    except FileNotFoundError as error:
        print(f"ERROR: {error}")


if __name__ == '__main__':
    compress_images('to-compress/')
