import xml.etree.ElementTree as et
tree = et.ElementTree(file = 'pokemon_nest.kml')
root = tree.getroot()
for child in root:
	for grandchild in child:
		for place in grandchild:
			print(place.tag)