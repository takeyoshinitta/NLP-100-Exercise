# 24. Media references
# Extract references to media files linked from the article.

import gzip
import json
import re

with gzip.open('enwiki-country.json.gz') as data_file:
    for i in data_file:
        data_json = json.loads(i)
        if data_json['title'] == 'United Kingdom':
            str = data_json['text']
    lines = str.split('\n')

    
