#Membuat server backend
from back_end import askBot, read_dictionary
from flask import Flask, request
import json

app = Flask(__name__)

dic = read_dictionary("database.txt")

@app.route("/",methods = ['POST'])
def main():
  data = request.form
  algo = data['method']
  query = data['query']

  answer = askBot(query,dic,algo)
  return json.dumps({'data':answer})

if __name__=="__main__":
  app.run(debug=True, port = 5000, host = '127.0.0.1')