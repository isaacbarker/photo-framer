# PhotoFramer

**A python based tool which converts images in batches from their own dimensions and ratios to the ideal Instagram aspect ratio and dimensions by adding a coloured frame as a background, also adding to the astethic of your grid.**

### About

Specifically this program takes input `.jpg, .png, .jpeg` images and resizes them to fit on a 1080x1350 coloured canvas with padding decided by the `margin` variable. Through this process a framed image with a 4:5 aspect ratio is obtained while still retaining the original ratio of the input image within. 

### Usage

To use the system download code and install required libraries from the Pipfile. This should only include `Pillow`. Then execute the code with the params: `[input directory] [output directory]`. This will use default margin and background params. To specific these add `[WHITE|BLACK|BLUR] [margin (px)]` to the end of the command.

e.g. `python3 convert.py . . BLUR 100` or `python3 convert.py . . BLACK 50`
