#importing necessary libraries
from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    #loading saved model here in this python file
    model = joblib.load('model/price_model.pkl')
    #creating data frame of JSON data
    # df = pd.DataFrame(json, index=[0])

    # from sklearn.preprocessing import StandardScaler
    # #performing preprocessing steps
    # scaler = StandardScaler()
    # scaler.fit(df)
    
    # x_scaled = scaler.transform(df)

    # x_scaled = pd.DataFrame(x_scaled, columns=df.columns)
    # y_predict = model.predict(x_scaled)

    res= {"Predicted Price of House" : 5.908}
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0')




# {"Home":{"0":1,"1":2,"2":3,"3":4,"4":5,"5":6,"6":7,"7":8,"8":9},"price":{"0":114300,"1":114200,"2":114800,"3":94700,"4":119800,"5":114600,"6":151600,"7":150700,"8":119200},"carpet_area":{"0":1790,"1":2030,"2":1740,"3":1980,"4":2130,"5":1780,"6":1830,"7":2160,"8":2110},"bedroom_count":{"0":2,"1":4,"2":3,"3":3,"4":3,"5":3,"6":3,"7":4,"8":4},"bathroom_count":{"0":2,"1":2,"2":2,"3":2,"4":3,"5":2,"6":3,"7":2,"8":2},"Offers":{"0":2,"1":3,"2":1,"3":3,"4":3,"5":2,"6":3,"7":2,"8":3},"brick":{"0":"No","1":"No","2":"No","3":"No","4":"No","5":"No","6":"Yes","7":"No","8":"No"},"location":{"0":"East","1":"East","2":"East","3":"East","4":"East","5":"North","6":"West","7":"West","8":"East"}}    