import os
from PIL import Image

savedir = "results"
filename = "testcounters.png"
img = Image.open(filename)

start_pos = start_x, start_y = (54, 81)  # Coordinates of first cell
frame_size = w, h = (91, 90)  # Size of each cell

major_columns = 2  # Number of pages
major_column_w = 1010  # Width between cell to cell on next page
major_rows = 5  # Number of blocks per page
major_row_h = 228
columns = 10
rows = 2

frame_num = 1
w, h = frame_size
for col_m in range(major_columns):
    for row_m in range(major_rows):
        for row in range(rows):
            for col in range(columns):
                x = w * col + start_x + major_column_w * col_m
                y = h * row + start_y + major_row_h * row_m
                crop = img.crop((x, y, x + w, y + h))
                save_at_template = os.path.join(savedir, "counter_{:03}.png")
                crop.save(save_at_template.format(frame_num))
                frame_num += 1