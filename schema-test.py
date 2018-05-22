
import json
import jsonschema
import os

from jsonschema import validate, Draft6Validator
from jsonschema.exceptions import ValidationError
import json

from iiif_prezi_upgrader import Upgrader

fh = file('schema/Manifest.json')
schema = json.load(fh)
fh.close()
v = Draft6Validator(schema)

fh = file('data/spec-example.json')
instance = json.load(fh)
fh.close()
v.validate(instance)
# walk over all our downloaded stuff...

files = os.listdir('data/remote_cache')
flags= {"ext_ok": False, "deref_links": False}
for f in files:
	if f.endswith('.json'):
		fn = os.path.join('data/remote_cache', f)
		print "processing file: %s" % fn
		upgrader = Upgrader(flags)
		try:
			data = upgrader.process_cached(fn)
		except Exception as e:
			print("Failed to upgrade %s" % fn)
			break
		try:
			v.validate(data)
		except ValidationError as e:
			print("Failed to validate %s" % fn)
			if e.absolute_schema_path[-1] == u'required' and \
				e.message.startswith("u'type'"):
				continue


			print(e.message)
			print(e.absolute_schema_path)
			print(e.absolute_path)
			break
		print "validated!"













if 0:
	fh = file('tests/_top.json')
	data = fh.read()
	fh.close()
	start = json.loads(data)
	startResolver = FileResolver("", start)

	classes = {}
	for x in clss:
		ss = os.listdir('tests/%s' % x)
		l = ["%s/%s" % (x, y) for y in ss if y.endswith('.json')]
		schema = {}
		for fn in l:
			sch = file("tests/%s" % fn)
			data = sch.read()
			sch.close()
			try:
				sjs = json.loads(data)
			except:
				print "Invalid json in schem: %s :(" % fn
				raise
			fresolvr = FileResolver("", sjs)
			schema[fn] = Draft4Validator(sjs, resolver=fresolvr)
		classes[x] = schema

	def resolve(ref):
		c = os.path.split(ref)[0]
		return classes[c][ref]


	def process(instance, validator):

		print validator.schema['title']
		try:
			validator.validate(instance)
		except ValidationError: 
			print v.schema['errorMessage']
			for s in validator.schema.get('onFail', []):
				v = resolve(s['$ref'])
				process(instance, v)
		except Exception:
			raise
		else:
			print "okay"
			for s in validator.schema.get('onSuccess', []):
				v = resolve(s['$ref'])
				process(instance, v)

		for s in validator.schema.get('onResult', []):
			v = resolve(s['$ref'])
			process(instance, v)


	ils = os.listdir('data/')

	for ifn in ils:
		print "Annotation File:  %s" % ifn
		ifh = file("data/examples/%s" % ifn)
		data = ifh.read()
		ifh.close()
		ijs = json.loads(data)	

		v = resolve(start['onResult'][0]['$ref'])
		process(ijs, v)


