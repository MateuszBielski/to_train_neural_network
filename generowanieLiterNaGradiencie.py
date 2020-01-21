from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

a = 28

txt = Image.new('RGB', (a,a), (0,50,70))
pixArray2 = np.array(txt)

for x in range(a):
    for y in range(a):
        g = int(x*50/a)
        b = int(y*70/a)
        pixArray2[y,x] = (0,g,b)
    
txt = Image.fromarray(pixArray2,'RGB')
# get a font
h = 20
fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', h)
# get a drawing context
d = ImageDraw.Draw(txt)
c1 = int(a/2-h/3)
c2 = int(a/2-h/2)
d.text((c1,c2), "H", font=fnt, fill=(255,255,255))

#~ txt.show()
plt.figure(figsize=(10,10))
plt.imshow(txt)
plt.colorbar()
plt.grid(False)
plt.show()
