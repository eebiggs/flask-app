from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the current hour
    current_hour = datetime.now().hour
    
    # Set greeting based on the time of day
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return f'{greeting}, MSOE! My name is Eliana. The current hour is {current_hour}.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)