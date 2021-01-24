# Predict Energy Consumption
Predict energy consumption using persisted(joblib) Random Forest Regression Model. Flask is used to expose a web api and allow external users to access the model's predictions.

--------------------------------------------
###### Required files

1. load_forecasting_model_v010.joblib
2. load_forecasting_web.py


### Run python load_forecasting_web.py to load the model amd predict for input values

###### Example GET/ url 

http://127.0.0.1:9181/forecast?heat_index=355.420185&avgT_interior=17.167407&avgRH_interior=50.910741&Season=3&Hour_of_day=17&weekday=0


###### Sample response 


```
{
  "model_label": "Random Forest Regression Model", 
  "predicted_value": [
    85.2
  ]
}
```

