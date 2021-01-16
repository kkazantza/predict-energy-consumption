# predict_energy_consumption
Predict energy consumption using persisted(joblib) Random Forest Regression Model. Use Flask to expose a web api and allow external users to access the model's predictions.


--------------------------------------------
GET/ url 
--------------------------------------------

http://127.0.0.1:9181/forecast?heat_index=355.420185&avgT_interior=17.167407&avgRH_interior=50.910741&Season=3&Hour_of_day=17&weekday=0

--------------------------------------------
response 
--------------------------------------------
The response of the get request:
"model_label"
"predicted_value"
	
	
sample:
```
{
  "model_label": "Random Forest Regression Model", 
  "predicted_value": [
    85.2
  ]
}
```
--------------------------------------------
load_forecasting_web.py description
--------------------------------------------

1. necessary packages are imported
2. load the model from load_forecasting_model_v010.joblib
3. creation of the api
4. predict for input values 

Note:
The load_forecasting_model_v010.joblib file is required in the same folder the load_forecasting_web.py will be running.
