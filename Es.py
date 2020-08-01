from datetime import datetime
from elasticsearch import Elasticsearch
import json 
import os

es = Elasticsearch(['http://ip172-18-0-84-bsellk3oudsg00bp99n0-9200.direct.labs.play-with-docker.com/'])

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'test.json')
#f = open(my_file,'r') 
#data = json.load(f, strict=False) 

file1 = open(my_file, 'r',  encoding="utf8") 
Lines = file1.readlines() 

ii=0
for i in Lines:
    doc = json.loads(i.rstrip("\n"))
    res = es.index(index="test-index", id=ii, body=doc)
    print(res['result'])
    ii=ii+1
  
# Closing file 
file1.close()