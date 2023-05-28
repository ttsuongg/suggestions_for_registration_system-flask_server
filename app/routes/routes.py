from flask import request, jsonify
from app import app
from app.recommender import SVDModel as RS

@app.route('/train', methods=['POST'])
def train():
    model = RS.TrainModel()
    response = jsonify({'message': 'Model trained successfully'})
    response.status_code = 200
    return response


@app.route('/predict', methods = ['POST'])
def predict():
    MSSV = request.json['mssv']
    DSMonHoc = request.json['dsmonhoc']
    predictions = RS.GetPredictions(DSMonHoc, MSSV)
    response = jsonify({'predictions': predictions})
    response.status_code = 200
    return response
