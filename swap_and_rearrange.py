from PIL import Image
import os

files = [
    'concat_00000004', 'concat_00000006', 'concat_00000007', 'concat_00000026', 'concat_00000036',
    'concat_00000039', 'concat_00000041', 'concat_00000043', 'concat_00000047', 'concat_00000052'
]
src = 'static/images/multiturn/'

for f in files:
    path = os.path.join(src, f + '.jpg')
    im = Image.open(path)
    w, h = im.size
    w1 = w // 3
    # 横向三等分
    im1 = im.crop((0, 0, w1, h))
    im2 = im.crop((w1, 0, 2 * w1, h))
    im3 = im.crop((2 * w1, 0, w, h))
    # 交换第二、三部分
    new_im = Image.new('RGB', (w, h))
    new_im.paste(im1, (0, 0))
    new_im.paste(im3, (w1, 0))
    new_im.paste(im2, (2 * w1, 0))
    new_im.save(os.path.join(src, f + '_swap.jpg')) 