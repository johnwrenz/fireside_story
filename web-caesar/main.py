from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form ="""
    <!DOCTYPE html>

        <html>
            <head>
                <style>
                    form {
                        background-color: #eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 16px sans-serif;
                        border-radius: 10px;
                    }
                    <textarea> {
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }
                </style>
            </head>
            <body>
                <form action="/add" method="POST">
                    <label>Rotate By:</label>
                    <input type="text" name="rot" value="0"/>
                    <p><input type="textarea" name="text"/></p>
                    <p><input type="submit"/></p>

                encrypt    

                
            </body>
        </html>   
        """ 

@app.route("/")
def add():
    request.args.get("Rotate")
    return form 

@app.route("/")
def encrypt():

app.run()