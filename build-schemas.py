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
	def_js['required'].remove('@context')
	return def_js

### Load up the base files and make definitions versions of them
fh = open('source_schema/common.json')
common_js = json.load(fh)
fh.close()

fh = open('source_schema/Collection.json')
collection_js = json.load(fh)
fh.close()
collection_def_js = main_to_def(collection_js)

fh = open('source_schema/Manifest.json')
manifest_js = json.load(fh)
fh.close()

fh = open('source_schema/Canvas.json')
canvas_js = json.load(fh)
fh.close()
canvas_def_js = main_to_def(canvas_js)

fh = open('source_schema/Range.json')
range_js = json.load(fh)
fh.close()
range_def_js = main_to_def(range_js)

fh = open('source_schema/AnnotationPage.json')
annopage_js = json.load(fh)
fh.close()
annopage_def_js = main_to_def(annopage_js)

fh = open('source_schema/AnnotationCollection.json')
annocoll_js = json.load(fh)
fh.close()

fh = open('source_schema/Annotation.json')
anno_js = json.load(fh)
fh.close()
anno_def_js = main_to_def(anno_js)

### Construct Collection
collection_js['definitions'] = common_js['definitions']
collection_js['definitions']['collection'] = collection_def_js
collection_js['definitions']['annotationPage'] = annopage_def_js
 
### Construct Manifest
manifest_js['definitions'] = common_js['definitions']
manifest_js['definitions']['canvas'] = canvas_def_js
manifest_js['definitions']['range'] = range_def_js
manifest_js['definitions']['annotationPage'] = annopage_def_js

### Construct Canvas
canvas_js['definitions'] = common_js['definitions']
canvas_js['definitions']['annotationPage'] = annopage_def_js

### Construct Range
range_js['definitions'] = common_js['definitions']
range_js['definitions']['range'] = range_def_js
range_js['definitions']['annotationPage'] = annopage_def_js

### Construct Annotation Page

annopage_js['definitions'] = common_js['definitions']
annopage_js['definitions']['annotation'] = anno_def_js

### Construct Annotation


### Construct Annotation Collection
annocoll_js['definitions'] = common_js['definitions']


### Write out schemas to use in practice
# These versions are now not human readable
# as they have lost all whitespace and order

fh = open('schema/Collection_system.json', 'w')
json.dump(collection_js, fh)
fh.close()

fh = open('schema/Manifest_system.json', 'w')
json.dump(manifest_js, fh)
fh.close()

fh = open('schema/Canvas_system.json', 'w')
json.dump(canvas_js, fh)
fh.close()

fh = open('schema/Range_system.json', 'w')
json.dump(range_js, fh)
fh.close()

fh = open('schema/AnnotationPage_system.json', 'w')
json.dump(annopage_js, fh)
fh.close()

fh = open('schema/Annotation_system.json', 'w')
json.dump(anno_js, fh)
fh.close()
