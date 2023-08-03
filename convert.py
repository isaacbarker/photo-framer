'''

    PhotoFramer:
    
    A python based tool which frames images within a 4:5 aspect ratio for positing on
    Instagram for the most optimal screen coverage.

'''

import sys
import os
import glob
from PIL import Image

def main():
    # Get images from argvs
    path = sys.argv[1]
    output = sys.argv[2]
    colour = (255, 255, 255) #rgb
    margin = 10 #px
    frame_dimension = (1080, 1350)

    # Add tailing '/' if required
    if not path.endswith('/'):
        path = path + '/'

    filenames = glob.glob(path + '*.jpg')

    # Frame each file
    i = 1

    for filename in filenames:
        img = Image.open(filename)
        frame = Image.new(img.mode, frame_dimension, color=colour)

        # Resize img
        img_aspect_ratio = img.size[1] / img.size[0]
        img_width_dimension = frame_dimension[0] - 2 * margin
        img_dimension = (int(img_width_dimension), int(img_aspect_ratio * img_width_dimension))
        print(img_dimension)
        img_resized = img.resize(img_dimension)

        # Calculate img position
        frame_centre = (int(frame_dimension[0] / 2), int(frame_dimension[1] /2))
        img_coord = (int(frame_centre[0] - img_dimension[0] / 2), int(frame_centre[1] - img_dimension[1] / 2))

        # Paste img
        frame.paste(img_resized, img_coord)

        # Save image
        output_img_path = os.path.realpath(output) + '/' + str(i) + '.jpg'
        print(output_img_path)
        frame.save(output_img_path)
        i += 1

        

if __name__ == '__main__':
    main()




