from PIL import Image

image = Image.open('pic.jpg');
image.show()

gray_Scale = image.convert('L')
gray_Scale.save('gray_Scale_img.jpg')
gray_Scale.show()

