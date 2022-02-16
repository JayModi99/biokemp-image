import urllib.request
from PIL import Image, ImageColor

# urllib.request.urlretrieve('https://cdn-biokemp.fi.tempcloudsite.com/kemp/colors/material/Hemp_base.png',"base.png")
im1 = Image.open("base.png").convert("RGBA")

# urllib.request.urlretrieve('https://cdn-biokemp.fi.tempcloudsite.com/kemp/components/components/A.png',"component.png")
im2 = Image.open("component.png").convert("RGBA")
im3 = Image.open("hemp.png").convert("RGBA")
# im4 = Image.blend(im2, im3, 0.5)
im2.paste(im3, (0,0), mask = im2)
# im2.save("abc.png","PNG")
im1.paste(im2, (0, 0), im2)
im1.save("final.png","PNG")
