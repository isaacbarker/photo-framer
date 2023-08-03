'''

    PhotoFramer:
    
    A python based tool which frames images within a 4:5 aspect ratio for positing on
    Instagram for the most optimal screen coverage.

'''

import sys
import os
import glob
from PIL import Image, ImageFilter, ImageEnhance

def main():

    # Check correct usage
    if len(sys.argv) <= 3:
        return print('Incorrect usage please use: \'python(3) [input directory path] [output directory path] [WHITE|BLACK|BLUR (optional)] [margin (optional)]\'')

    # Get paths
    path = sys.argv[1]
    output = sys.argv[2]

    if not os.path.isdir(path):

        return print('Please enter a valid input directory path.')
    

    if not os.path.isdir(output):

        return print('Please enter a vlid output directory path.')

    # Get mode
    modes = ['WHITE', 'BLACK', 'BLUR']
    mode = 'WHITE'
    
    if len(sys.argv) >= 4:

        if sys.argv[3] not in modes:
            return print('Please use a valid mode e.g. BLUR.')
        
        mode = sys.argv[3]


    # Get margin
    margin = 15

    if len(sys.argv) >= 5:

        try:
            margin = int(sys.argv[4])
        except:
            return print('Your margin value cannot be converted to an Integer please use an Integer!')


    # Operation variables
    frame_dimension = (1080, 1350)

    # Add tailing '/' if required
    if not path.endswith('/'):
        path = path + '/'


    print('Finding images.')

    # Add images
    filenames = glob.glob(path + '*.jpg')
    filenames = filenames + glob.glob(path + '*.jpeg')
    filenames = filenames + glob.glob(path + '*.png')

    print(f'Found {len(filenames)} images. Framing...')

    # Frame each file
    i = 1

    for filename in filenames:

        img = Image.open(filename)
        img_aspect_ratio = img.size[1] / img.size[0]

        # Configure frame
        colour = None
        frame = None

        if mode == 'WHITE':

            colour = (255, 255, 255)
            frame = Image.new(img.mode, frame_dimension, color=colour)

        elif mode == 'BLACK':

            colour = (0, 0, 0)
            frame = Image.new(img.mode, frame_dimension, color=colour)

        elif mode == 'BLUR':

            # Create blurred background
            if img.size[0] > img.size[1]:

                frame = img.resize((int(frame_dimension[0] / img_aspect_ratio), frame_dimension[1]))
            
            else:

                frame = img.resize((frame_dimension[0], int(frame_dimension[1] * img_aspect_ratio)))
            
            frame = frame.crop((int((frame.size[0] - frame_dimension[0]) / 2), 0, frame.size[0] - (int((frame.size[0] - frame_dimension[0]) / 2)), frame_dimension[1]))
            frame = frame.filter(ImageFilter.BoxBlur(10))
            enhancer = ImageEnhance.Brightness(frame)
            frame = enhancer.enhance(0.75)


        # Resize img
        img_width_dimension = frame_dimension[0] - 2 * margin
        img_dimension = (int(img_width_dimension), int(img_aspect_ratio * img_width_dimension))
        img_resized = img.resize(img_dimension)

        # Calculate img position
        frame_centre = (int(frame_dimension[0] / 2), int(frame_dimension[1] /2))
        img_coord = (int(frame_centre[0] - img_dimension[0] / 2), int(frame_centre[1] - img_dimension[1] / 2))

        # Paste img
        frame.paste(img_resized, img_coord)

        # Save image
        output_img_path = os.path.realpath(output) + '/' + str(i) + '.jpg'
        frame.save(output_img_path)
        print(f'Successfully saved {output_img_path}...')
        i += 1

    print('Finished batch operation. Exiting...')

    
if __name__ == '__main__':
    main()




