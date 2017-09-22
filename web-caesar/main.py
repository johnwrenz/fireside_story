from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
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
                    <label for="rot">Rotate By:</label>
                    <input id="rot" type="text" name="rot" value="0"/>
                    <p><input type="textarea" name="text"/></p>
                    <p><input type="submit"/></p>

                </body>
        </html>   
        """ 

@app.route("/")
def add():
    rotate_by = request.args.get("Rotate")
    return form 

@app.route("/add", methods=['POST'])
def encrypt():
    text = request.form["text"]
    return text

app.run()