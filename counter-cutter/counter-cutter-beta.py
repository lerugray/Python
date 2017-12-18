############################################
#
#
#       WARGAME COUNTER-CUTTER
#       Programmed by Ray Weiss
#       lerugray@gmail.com
#
#
############################################

#  imports

import os
from PIL import Image
from sys import argv

save_dir = "results"
filename = argv[1]  # Your counter sheet
img = Image.open(filename)

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

coord_input = input("Enter coordinates of first cell x, y: ")
start_pos = start_x, start_y = [int(x) for x in coord_input.split(",")]

counter_input = input("Enter the size of the counters x, y: ")
counter_size = w, h = [int(x) for x in counter_input.split(",")]

major_columns = int(input("Number of Pages: "))
major_columns_w = int(input("Width between cell to cell on the next page: "))
major_rows = int(input("Number of blocks per page: "))
major_rows_h = int(input("height between cell to cell on the next block: "))
columns = int(input("Number of columns inside a block: "))
rows = int(input("Number of rows inside a block: "))

###################################
#
#  End of user supplied arguments
#  Start of program
#
###################################

frame_num = 1

w, h = counter_size

for col_m in range(major_columns):
    for row_m in range(major_rows):
        for row in range(rows):
            for col in range(columns):
                x = w * col + start_x + major_columns_w * col_m
                y = h * row + start_y + major_rows_h * row_m
                crop = img.crop((x, y, x + w, y + h))
                save_at_template = os.path.join(save_dir, "counter_{:03}.png")
                crop.save(save_at_template.format(frame_num))
                frame_num += 1
                