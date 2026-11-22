from PIL import Image, ImageDraw, ImageFont
import sys, os
out = sys.argv[1]
S = 2
def save(im, name, size):
    im.resize(size, Image.LANCZOS).save(os.path.join(out, name))
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 110*S)
# id.png placeholder
im = Image.new("RGBA", (600*S, 720*S), (0,0,0,0)); d = ImageDraw.Draw(im)
d.ellipse((60*S,470*S,540*S,1000*S), fill=(26,35,64,255), outline=(36,123,255,255), width=6*S)
d.ellipse((165*S,120*S,435*S,400*S), fill=(36,48,85,255), outline=(255,53,79,255), width=5*S)
d.text((300*S,262*S), "RM", font=f, fill=(242,244,250,255), anchor="mm")
save(im, "id.png", (600,720))
# right_pointing.png placeholder
im = Image.new("RGBA", (700*S, 720*S), (0,0,0,0)); d = ImageDraw.Draw(im)
d.ellipse((20*S,470*S,420*S,1000*S), fill=(26,35,64,255), outline=(36,123,255,255), width=6*S)
d.line((300*S,540*S,600*S,450*S), fill=(36,48,85,255), width=70*S)
d.ellipse((565*S,415*S,665*S,515*S), fill=(36,48,85,255), outline=(255,53,79,255), width=5*S)
d.ellipse((90*S,120*S,350*S,390*S), fill=(36,48,85,255), outline=(255,53,79,255), width=5*S)
d.text((220*S,255*S), "RM", font=f, fill=(242,244,250,255), anchor="mm")
save(im, "right_pointing.png", (700,720))
