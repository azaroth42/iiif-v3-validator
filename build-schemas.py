import json
import copy

# Construct complete schemas from the components

def main_to_def(orig):
	def_js = copy.deepcopy(orig)
	del def_js['$schema']
	del def_js['$id']
	del def_js['$title']
	del def_js['$schema']
	del def_js['definitions']
	del def_js['properties']['@context']
	return def_js


### Load up the base files and make definitions versions of them
fh = open('schema/common.json')
common_js = json.load(fh)
fh.close()

fh = open('schema/Collection.json')
collection_js = json.load(fh)
fh.close()
collection_def_js = main_to_def(collection_js)

fh = open('schema/Manifest.json')
manifest_js = json.load(fh)
fh.close()

fh = open('schema/Canvas.json')
canvas_js = json.load(fh)
fh.close()
canvas_def_js = main_to_def(canvas_js)

fh = open('schema/Range.json')
range_js = json.load(fh)
fh.close()
range_def_js = main_to_def(range_js)


### Construct Collection
collection_js['definitions'] = common_js['definitions']
collection_js['definitions']['collection'] = collection_def_js

### Construct Manifest
manifest_js['definitions'] = common_js['definitions']
manifest_js['definitions']['canvas'] = canvas_def_js
manifest_js['definitions']['range'] = range_def_js


### Construct Canvas
canvas_js['definitions'] = common_js['definitions']


### Construct Range
range_js['definitions'] = common_js['definitions']
range_js['definitions']['range'] = range_def_js


### Write out schemas
# These versions are now not human readable
# as they have lost all whitespace and order
fh = open('schema/Manifest_system.json', 'w')
json.dump(manifest_js, fh)
fh.close()


