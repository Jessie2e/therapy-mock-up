from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parent.parent
im=Image.new('RGB',(1200,630),'#f7f4eb');d=ImageDraw.Draw(im)
regular='/System/Library/Fonts/Supplemental/Arial.ttf'
bold='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
# Supply these font paths on other systems when regenerating.
def font(size,weight=False): return ImageFont.truetype(bold if weight else regular,size)
d.line((72,78,1128,78),fill='#d6d6c9',width=2)
d.text((72,108),'2e STUDIO  /  WEBSITE COLLECTION',font=font(18,True),fill='#38664f')
d.text((68,175),'Therapy Mock Up',font=font(67,True),fill='#112f35')
d.text((72,292),'Therapy website template',font=font(31),fill='#bb452c')
d.text((72,359),'A space for every part of you.',font=font(24),fill='#112f35')
d.line((72,472,1128,472),fill='#d6d6c9',width=2)
d.text((72,507),'Designed by 2e Studio',font=font(21,True),fill='#112f35')
d.text((72,543),'Thoughtful design. Ready to make your own.',font=font(18),fill='#526159')
logo=Image.open(root/'dist/assets/emblem.webp').convert('RGBA');logo.thumbnail((365,370),Image.Resampling.LANCZOS)
im.paste(logo,(770,99),logo)
im.save(root/'dist/assets/whole-you-social-v1.jpg',quality=90,optimize=True)
# QA artifacts are not part of the distributable site.
qa=root/'work';qa.mkdir(exist_ok=True)
im.resize((600,315)).save(qa/'template-og-thumbnail.jpg')
im.crop((45,24,1155,606)).resize((600,315)).save(qa/'template-og-crop.jpg')
print('OG image:',im.size,(root/'dist/assets/whole-you-social-v1.jpg').stat().st_size,'bytes')
