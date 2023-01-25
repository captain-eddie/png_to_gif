
'''
Edward Abel Guobadia
12-14-2022
'''

import os
import argparse
from PIL import Image

def main():
    #   variables
    parser = argparse.ArgumentParser(
        description = "png to gif"
    )

    parser.add_argument(
        "--path",
        type = str,
        default = ".",
        help = "Directory path of the png files",
    )

    args = parser.parse_args()
    current_dir_path = args.path

    #   get files in directory
    files_in_directory = os.listdir()

    #   put images in list
    images = []
    for file in files_in_directory:
        file_path = os.path.join(current_dir_path, file)
        if file_path.endswith(".png"):
            images.append(file_path)

    # Open each image and convert it to RGB mode
    images = [Image.open(frame).convert('RGB') for frame in images]

    # Save the images as a GIF using the original filenames
    images[0].save(os.path.join(current_dir_path, 'animation.gif'), save_all=True, append_images=images[1:], duration=50, loop=0)


if __name__ == "__main__":
    main()
