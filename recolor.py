from PIL import Image
import time

basis = Image.open("planck.png")
basisdat = basis.load()

target = Image.open("wmap.png")
targetdat = target.load()

hashmap = {}
def memoized(blah):
	global hashmap
	if blah in hashmap:
		return hashmap[blah]
	answ = map_color(blah)
	hashmap[blah] = answ
	return answ

def map_color((rk, gk, bk)):
	acme = 255 * 255 * 3
	acmedex = 0
	merpdex = 0
	differs = (0,0,0)
	for x in range(basis.size[0]):
		r,g,b = basisdat[x, 0]
		diff = (rk - r)**2 + (gk - g)**2 + (bk - b)**2 
		if diff < acme:
			acme = diff
			differs = (rk-r,gk-g,bk-b)
			acmedex = x
		if diff == acme:
			merpdex = x
	schmardex = target.size[0] * ((acmedex + merpdex) / 2) / basis.size[0]
	rm, gm, bm = targetdat[schmardex, 0]
	rd, gd, bd = differs

	return (rm + rd, gm + gd, bm + bd)

# for x in range(basis.size[0]):
# 	print map_color(basisdat[x, 0])


im = Image.open("Planck_CMB_orig.jpg")
width, height = im.size
pixels = im.load()

# for x in range(basis.size[0]):
# 	print basisdat[x, 0]

# for x in range(width):
# 	print pixels[x, 400]


for x in range(width):
	tstart = time.time()
	for y in range(height):
		pixels[x, y] = memoized(pixels[x, y])
	print "running line", x, 1.0 / (time.time() - tstart)
	
# print im.histogram()
im.save("Recolored.png")