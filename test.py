import requests

data = {
# LEDs
#     "url": "https://m.media-amazon.com/images/I/518GKwV41pL.__AC_SX300_SY300_QL70_FMwebp_.jpg"
# resistor
#    "url": "https://content.instructables.com/F00/72CL/IRXT3HTJ/F0072CLIRXT3HTJ.jpg"
# ultrasonic_sensor
    "url": "https://m.media-amazon.com/images/I/81i31MLusQL._SX522_.jpg"
# potentiometer
#    "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Electronic-Component-Potentiometer.jpg"
# resistor
#     "url": "https://m.media-amazon.com/images/I/5131jUXEktL._SX522_.jpg" 
}

#url = "http://localhost:8080/2015-03-31/functions/function/invocations"
url = "https://1m8vb0658c.execute-api.us-west-2.amazonaws.com/test/predict"



results = requests.post(url, json=data).json()

print(results)