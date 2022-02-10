# 20. Read JSON documents
# Read the JSON documents and output the body of the article about the United Kingdom. Reuse the output in problems 21-29.

import gzip
import json

with gzip.open('enwiki-country.json.gz') as data_file:
    for i in data_file:
        data_json = json.loads(i)
        if data_json['title'] == 'United Kingdom':
            print(data_json['text'])
    
    data_file.close()