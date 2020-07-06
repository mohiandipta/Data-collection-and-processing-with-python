import json
a_string = '\n\n\n{\n "resultCount":25,\n "result": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
d = json.loads(a_string)
print(type(d))
print(d.keys())
print(d['resultCount'])



#### --------for indentation--------####
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1':{'c': 5, 'a': 90, '5': 50}, 'key2':{'b':3, 'c':"yes"}}

print(d)
print('--------')
print(pretty(d))