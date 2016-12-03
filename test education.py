import requests
from pprint import pprint
import json

URL = 'https://data.ct.gov/api/views/shww-dhc6/rows.json'
r = requests.get(URL)

datas = json.loads(r.text)['data']

schools = []

NAME_FIELD = 8
DISTRICT_FIELD = 9
ADDRESS_FIELD = 11
ADDRESS_FIELD_LAT = 1
ADDRESS_FIELD_LONG = 2

# def printInfo(school):
# 	print(school[NAME_FIELD])
# 	print(school[DISTRICT_FIELD])
# 	print(school[ADDRESS_FIELD])

# count_schools = 0
# count_public_schools = 0
# count_district = 0

schools = {}

for school in datas:
	if school[ADDRESS_FIELD][ADDRESS_FIELD_LAT]:
		# printInfo(school)
		schools[school[NAME_FIELD]] = school
		# print()
		# count_schools += 1
		# if school[DISTRICT_FIELD] == 'Public Schools':
		# 	count_public_schools += 1
		# if 'District' in school[DISTRICT_FIELD]:
		# 	count_district += 1

# print(len(schools))
# print(count_schools)
# print(count_public_schools)
# print(count_district)
# print(count_public_schools + count_district)

# pprint(schools)

schoolJSON = json.dumps(schools)

print(schoolJSON)

# return schoolJSON
# print(schoolJSON)
# 	if data[0] == 1231:
# 		schools.append(data)

# for school in schools:
# 	for i, info in enumerate(school):
# 		print(i, info)
# 	print(school[NAME_FIELD])
# 	print(school[DISTRICT_FIELD])
# 	print(school[ADDRESS_FIELD])



# print(type(data))
# print(dict(data))

# print(r.content)