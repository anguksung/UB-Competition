import requests
from pprint import pprint
import json

def accountability():
	#Accountability
	#'https://data.ct.gov/api/views/mdsf-2nsf/rows.json'
	#ACCOUNTABILITY_INDEX = 19

	accountability_url = 'https://data.ct.gov/api/views/mdsf-2nsf/rows.json'
	accountability_request = requests.get(accountability_url)
	datas = json.loads(accountability_request.text)['data']

	NAME_FIELD = 10
	DISTRICT_FIELD = 9
	ADDRESS_FIELD = 11
	ACCOUNTABILITY_INDEX = 19 #11 + 8
	OVERALL_SPI_INDEX = 12 #11 + 5 - 5

	schools = {}

	for school in datas:
		name, _, right= school[NAME_FIELD].partition('_')
		schools[name] = school

	accountability_dict = {}

	for name in schools:
		accountability_dict[name] = schools[name][ACCOUNTABILITY_INDEX]
	
	return accountability_dict#key = accountability index

def spi_overall():
	###
	#SPI overall
	#https://data.ct.gov/api/views/t7dz-qwpn/rows.json
	#OVERALL_SPI_INDEX = 12
	spi_url = 'https://data.ct.gov/api/views/t7dz-qwpn/rows.json'
	spi_request = requests.get(spi_url)
	datas = json.loads(spi_request.text)['data']

	schools = {}

	for school in datas:
		name, _, right= school[NAME_FIELD].partition('_')
		schools[name] = school

	spi_overall_dict = {}

	for name in schools:
		spi_overall_dict[name] = schools[name][OVERALL_SPI_INDEX]

	return spi_overall_dict# key = overall spi

def smart_schools():
	spi = spi_overall()
	acc = accountability()

	smart = {}

	for school in spi:
		spi_score = spi[school]
		acc_score = acc[school]
		smart[school] = (spi_score + acc_score) // 2

	return smart

def convert_to_json(dictionary):
	return json.dumps(dictionary)