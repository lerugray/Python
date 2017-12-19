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
    line = f.readline()
    out = line.strip("\n")

    while line:
        line = f.readline()
        out = line.strip("\n")
        start_pos = start_x, start_y = [int(x) for x in out.split(",")]
        counter_size = w, h = [int(x) for x in out.split(",")]
        line = f.readline()
        out = line.strip("\n")
        major_columns = int(out)
        line = f.readline()
        out = line.strip("\n")
        major_columns_w = int(out)
        line = f.readline()
        out = line.strip("\n")
        major_rows = int(out)
        line = f.readline()
        out = line.strip("\n")
        major_rows_h = int(out)
        line = f.readline()
        out = line.strip("\n")
        columns = int(out)
        line = f.readline()
        out = line.strip("\n")
        line = f.readline()
        rows = int(out)

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