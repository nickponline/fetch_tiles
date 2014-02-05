import requests
import os
import cv2
import numpy as np

layers = [
	'nickponline.dcqbbjcs', # Our EO layer
	'nickponline.g7642h2a', # Mapbox satelitte layer
]

zoom = 18 
xs = [41866, 41871] # Xcoords
ys = [101378, 101380] #Ycoords
dim = 256 # Tile dimension
url = 'http://a.tiles.mapbox.com/v3/{layer}/{z}/{x}/{y}.png'

for i, layer in enumerate(layers):
	width = (max(xs) - min(xs) + 1) * dim 
	height = (max(ys) - min(ys) + 1) * dim 
	image = np.zeros((height,width,3), np.uint8)
	print "Created new image:", image.shape

	for xi, x in enumerate(xrange(min(xs), max(xs)+1)):
		for yi, y in enumerate(xrange(min(ys), max(ys)+1)):
			uri = url.format(x=x, y=y, z=zoom, layer=layer)	
			print uri
			os.system('wget -O tile.png {uri}'.format(uri=uri))
			tile = cv2.imread('tile.png')
			print "Loading tile: ", tile.shape
			image[yi * dim:yi * dim + dim, xi * dim:xi * dim + dim] = tile[:, :]

	cv2.imwrite('{}.png'.format(i), image)