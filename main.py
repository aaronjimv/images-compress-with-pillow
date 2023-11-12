from PIL import Image
import os


def compress_images(image_folder):
    '''
    Compresses all JPEG images in the specified folder.

    Parameters:
    - image_folder (str): The path to the folder containing the images to be compressed.

    Raises:
    - FileNotFoundError: If the specified folder is not found.

    Example:
    >>> compress_images('to-compress/')

    This function iterates through all the files in the specified folder, checks if they have a '.jpg' extension, and compresses them with a quality of 20.
    The compressed images are saved in the same folder with '_compress' appended to their original names.

    Note: This function uses the Pillow (PIL) library to handle image processing.
    '''
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension = os.path.splitext(image_folder + file)
            print("compressing images " + file_name + file_extension)

            if file_extension == '.jpg':
                with Image.open(image_folder + file) as file_compress:
                    file_compress.save(
                        file_name + "_compress.jpg",
                        optimize=True,
                        quality=20
                    )
    except FileNotFoundError as error:
        print(f"ERROR: {error}")


if __name__ == '__main__':
    compress_images('to-compress/')
