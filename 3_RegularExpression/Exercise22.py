# 22. Category names
# Extract the category names of the article.

import gzip
import json
import re

with gzip.open('enwiki-country.json.gz') as data_file:
    for i in data_file:
        data_json = json.loads(i)
        if data_json['title'] == 'United Kingdom':
            str = data_json['text']
    lines = str.split('\n')

    for i in lines:
        if re.match(r'^\[\[Category:.+\]\]$', i):
            # print (i[11:-2])
            print(i.replace('[', '').replace(']', '').replace(':', '').replace('Category', '').replace('|', ''))
    
    data_file.close()
    
