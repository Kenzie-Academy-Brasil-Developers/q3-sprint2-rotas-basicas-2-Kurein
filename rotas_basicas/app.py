from flask import Flask
from datetime import datetime as dt

app = Flask(__name__)

@app.get('/')
def home():
    return {"data": "Hello Flask!"}, 200

@app.get('/current_datetime')
def unprocessed_data():
        curr_hour = dt.now().hour
        msg = "Boa noite!"

        if curr_hour < 12:
            msg = "Bom dia!"

        elif curr_hour < 18:
            msg = "Boa tarde!"
            
        return { "current_datetime": f'{dt.now().strftime("%d/%m/%Y")} {dt.now().strftime("%I:%M:%S %p")}', "message": f"{msg}"}, 200

