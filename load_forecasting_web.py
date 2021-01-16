from flask import Flask, request, jsonify
from flask import Flask,url_for
from flask import request
from joblib import dump, load

# load the model from disk
loaded_model = load('load_forecasting_model_v010.joblib')
print("model is loaded")


app = Flask(__name__)

@app.route('/forecast/',methods=['GET'])
def forecast():
    heat_index = request.args.get('heat_index')
    avgT_interior = request.args.get('avgT_interior')
    avgRH_interior = request.args.get('avgRH_interior')
    Season = request.args.get('Season')
    Hour_of_day = request.args.get('Hour_of_day')
    weekday = request.args.get('weekday')

    x_test = [[heat_index,avgT_interior,avgRH_interior,Season,Hour_of_day,weekday]]
    print(x_test)
    y_test = [60]
    y_pred=loaded_model.predict(x_test)
    return jsonify({"predicted_value":y_pred.tolist(),"model_label":"Random Forest Regression Model"})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int("9181"), debug=True)