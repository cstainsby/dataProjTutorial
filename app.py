import json 
import torch
from flask import Flask, render_template, request
from model import NeuralNet, predict

app = Flask(__name__)

# Create an instance of the network
input_size = 10
hidden_size = 5
output_size = 2
model = NeuralNet(input_size, hidden_size, output_size)

# reload state into model
model.load_state_dict(torch.load("./model_save/demo.pt"))

@app.route("/", methods=["GET"])
def hello_world():
  return render_template("base.html")

@app.route('/class-model', methods=["POST"])
def my_endpoint():
  req_vector = request.get_json()["vector"]
  print("req_vector", req_vector)
  
  tensor = torch.tensor([[float(fl_num) for fl_num in req_vector]])
  print("tensor", tensor)
  classification = predict(model, tensor)
  print("classIFCI:", classification.tolist()[0])
    
  return {"classification": classification.tolist()[0] }

if __name__ == '__main__':
  app.run(debug=True, port=8000)