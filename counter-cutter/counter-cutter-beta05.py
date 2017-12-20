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

with open("instr.txt") as f:
    lines = f.readlines()

start_pos = start_x, start_y = [int(x) for x in lines[0].split(",")]
counter_size = w, h = [int(x) for x in lines[1].split(",")]
major_columns = int(lines[2])
major_columns_w = int(lines[3])
major_rows = int(lines[4])
major_rows_h = int(lines[5])
columns = int(lines[6])
rows = int(lines[7])


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