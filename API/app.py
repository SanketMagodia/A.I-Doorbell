from flask import Flask, request, jsonify
import torch
import numpy as np


model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt', force_reload=True)
app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    file = request.files['image']
    
    print(type(file))
    file.save("temp.jpg")
    results = model("temp.jpg")
    # print(results.print())
    # print(request.form['foo']) # should display 'bar'
    data = {"result":np.squeeze(results.render()).tolist(), "output":list(set(results.pandas().xyxy[0].name.tolist()))}
    return  jsonify(data)# response to your request.

if __name__ == "__main__":
    app.run(debug=True,port=5005)