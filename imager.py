import numpy as np
from PIL import Image

gscale = " .:-=+*#%@"

def avg_brightness(pic):
    im = np.array(pic)
    width, height = im.shape
    return np.average(im.reshape(width, height))

def image_to_ascii(file_name, cols, scale):
    image = Image.open(file_name).convert('L')
    width, height = image.size
    tile_width = width / cols
    tile_height = tile_width / scale
    rows = int(height / tile_height)
    ascii_img = []
    for j in range(rows):
        y1 = int(j * tile_height)
        y2 = int((j + 1) * tile_height)
        if j == rows - 1:
            y2 = height

        row = ""
        for i in range(cols):
            x1 = int(i * tile_width)
            x2 = int((i + 1) * tile_width)
            if i == cols - 1:
                x2 = width

            tile = image.crop((x1, y1, x2, y2))
            avg = int(avg_brightness(tile))
            gsval = gscale[int((avg * 9) / 255)]
            row += gsval

        ascii_img.append(row)

    return ascii_img

def main():
    input_pic = 'x.jpg'
    out_file = 'out.txt'
    scale = 0.43
    cols = 80
    txt = image_to_ascii(input_pic, cols, scale)
    with open(out_file, 'w') as f:
        for row in txt:
            f.write(row + '\n')
    print(f"converted {input_pic} to ASCII in {out_file}")

main()
