import sys
import os
from PIL import Image, ImageFilter

path = sys.argv[1]

news = sys.argv[2]

if  not os.path.exists(news):
	
	os.makedirs(news)

for file in os.listdir(path):
	img = Image.open(f'{path}{file}')
	clean_name = os.path.splitext(file)[0]
	img.save(f'{news}{clean_name}.png','png')
	print('done')

# filtered_img = img.filter(ImageFilter.SHARPEN)
# box = (5,10,5,10)
# new_pic = filtered_img.crop(box)
# new_pic.save('grey.png','png')

# new_pic.show()
