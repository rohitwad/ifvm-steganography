import sys
import Image, ImageOps

def extract_image(from_image, s=4):
	data=Image.open(from_image)
	for x in range(data.size[0]):
		for y in range(data.size[1]):
			p=data.getpixel((x,y))
			r=(p[0]%s)*255/s
			g=(p[1]%s)*255/s
			b=(p[2]%s)*255/s
			data.putpixel((x,y), (r, g, b))
	return data

def hide_image(public_img, secret_img, s=4):
	data=Image.open(public_img)
	key=ImageOps.autocontrast(Image.open(secret_img).resize(data.size))
	for x in range(data.size[0]):
		for y in range(data.size[1]):
			p=data.getpixel((x,y))
			q=key.getpixel((x,y))
			r=p[0]-(p[0]%s)+(s*q[0]/255)
			g=p[1]-(p[1]%s)+(s*q[1]/255)
			b=p[2]-(p[2]%s)+(s*q[2]/255)
			data.putpixel((x,y), (r, g, b))
	return data

def give_help():
	print "wrong, try: "
	print "%s show from .jpg" %sys.argv[0]
	print "%s hide public.jpg secret.jpg" % sys.argv[0]

if __name__=="__main__":
	if len(sys.argv)!=3 and len(sys.argv)!=4:
		print "1"
		give_help()
	elif sys.argv[1]=="show":
		print "2"
		extract_image(sys.argv[2]).save("extracted.png");
		print "image saved as extracted.png";
	elif sys.argv[1]=="hide":
		print "3"
		hide_image(sys.argv[2], sys.argv[3]).save("hidden.png");
		print "successfully hided the image";
	else:
		print "4"
		give_help()
