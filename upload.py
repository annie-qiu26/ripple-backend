import requests
from csv import reader

NAME_INDEX = 2
URL_INDEX = 19
CATERGORY_INDEX = 3

post_url = "http://localhost:5000/api/organization"
post_headers = {"Content-Type": "application/json"}

data_path = "data/output.csv"

with open(data_path) as data:
    data_reader = reader(data)
    header = next(data_reader)
    if header != None:
        for row in data_reader:
            if row[URL_INDEX]:
                post_data = '{"name": "%s", "url": "%s", "category": "%s"}' % (row[NAME_INDEX], row[URL_INDEX], row[CATERGORY_INDEX])
                r = requests.post(post_url, data=post_data, headers=post_headers)                

    