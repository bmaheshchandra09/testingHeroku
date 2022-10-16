from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/predict")
def upload():
  d={}
  d['output'] = "hye"
  return jsonify(d)
if __name__=="__main__":
    app.run()