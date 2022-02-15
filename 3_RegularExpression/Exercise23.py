# 23. Section structure
# Extract section names in the article with their levels. For example, the level of the section is 1 for the MediaWiki markup "== Section name ==".

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
        if re.match(r'^=+.+=+$', i):
            s = re.match(r'^(=+)(.+?)=+$', i)
            print (f'name: {format(s.group(2))} \t level: {len(s.group(1)) - 1}')

    data_file.close()
