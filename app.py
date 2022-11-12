#1 Import flask
from flask import Flask

#2. create an app, being sure to pass __name__
app = Flask(__name__)

#3. Define what to do when a user goes to the index route
@app.route('/')

#4. Define what to do when a user goes to the /about route
def hello_world():

if __name__=="__main__":
    app.run(debug=True)
