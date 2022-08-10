from email.policy import default
from operator import index
from getbanksTypes import Output, Query
from getdocumentTypes import getdocumentArgs, Document
from deletedocumentbyidTypes import deletedocumentbyidArgs, DeleteDocument
from createDocumentTypes import createdocumentArgs, DeleteDocument
from updateDocumentfieldTypes import updatedocumentfieldArgs, DeleteDocument
from flask import Flask, request, jsonify
import requests

from elasticsearch import Elasticsearch

app = Flask(__name__)
client = Elasticsearch("http://localhost:9200")

@app.route('/getbanks', methods=['POST'])
def getbanksHandler():
    args = request.get_json()
    es = Elasticsearch(hosts=["http://localhost:9200"])
    # url = 'http://localhost:9200/bank/_search'
    #check if there is an input
    if args['input']:
        value = args['input']['query']
        if  'match' in value:
            if 'operator' in value['match']:
                operator = value['match']['operator']
            else:
                operator = 'or'
            data = { "query": { "match":{ f"{value['match']['field']}": {"query": value['match']['value'], "operator": operator}} }}
            r = es.search(index='bank', body=data)
    else:
        r = es.search(index='bank')
    values = ['took', 'timed_out', 'hits']
    return Output.from_json(r, values).to_json()

@app.route('/getdocument', methods=['POST'])
def getdocumentHandler():
  args = getdocumentArgs.from_request(request.get_json())
  id = args.id
  index = args.index

#   print(index\\)
#   type = args.type
  # Get Document API
  a = client.get(index=index, id=id)
  # business logic here
  return Document.from_json(a).to_json()

@app.route('/deletedocumentbyid', methods=['POST'])
def deletedocumentbyidHandler():
  args = deletedocumentbyidArgs.from_request(request.get_json())
  print(args)
  index = args.index
  id = args.id
  # business logic here
  r = client.delete(index=index, id=id)
  return DeleteDocument.from_json(r).to_json()

@app.route('/createdocument', methods=['POST'])
def createdocumentHandler():
  args = createdocumentArgs.from_request(request.get_json())
#   print(args.args)
  document = args.args
  index = args.index
  id = args.id
  if id:
  # business logic here
    r = client.index(index=index, document=document, id=id)
  else:
     r = client.index(index=index, document=document)
#   print(r , 'yea')
  return DeleteDocument.from_json(r).to_json()

@app.route('/updatedocumentfield', methods=['POST'])
def updatedocumentfieldHandler():
  args = updatedocumentfieldArgs.from_request(request.get_json())
  print(args)
  document = args.fields
  index = args.index
  id = args.id
  # business logic here
  r = client.update(index=index, doc=document, id=id)
  return DeleteDocument.from_json(r).to_json()

if __name__ == '__main__':
  app.run(debug = True, )