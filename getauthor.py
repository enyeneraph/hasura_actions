from getauthorTypes import getauthorArgs, Author
from getbook_by_idTypes import getbook_by_idArgs, Book
from getbooksTypes import Books
from getauthorsTypes import Authors
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/getauthor', methods=['POST'])
def getauthorHandler():
  args = getauthorArgs.from_request(request.get_json())
  #check that the attribute, id of args is valid(an integer)
  if type(args.id) != int :
    return 'id invalid'
  # business logic here
  r = requests.get(f'http://localhost:5000/api/v1/authors/{args.id}').json()
  return Author.from_json(r).to_json()

@app.route('/getbook_by_id', methods=['POST'])
def getbook_by_idHandler():
  args = getbook_by_idArgs.from_request(request.get_json())
  print(args)
  if type(args.id) != str :
    return jsonify({'error':'args invalid'})
  r = requests.get(f'http://localhost:5000/api/v1/books/{args.id}').json()
  # business logic here
  return Book.from_json(r).to_json()

@app.route('/getbooks', methods=['POST'])
def getbooksHandler():
  # business logic here
  r = requests.get('http://localhost:5000/api/v1/books').json()
  # business logic here
  return Books(r).to_json()

@app.route('/getauthors', methods=['POST'])
def getauthorsHandler():
  r = requests.get('http://localhost:5000/api/v1/books').json()
  # business logic here
  return Authors(r).to_json()

if __name__ == '__main__':
  app.run(debug = True, port = '505')