tester = {'info':[{"name": "Mohian", 'class standing': 'Junior', 'major': 'Computer science'},{"name": "Dip", 'class standing': 'Senior', 'major': 'Astrophysics'}]}
inner_list = tester['info']
import  json

compri = [d['name'] for d in inner_list]
print(compri)