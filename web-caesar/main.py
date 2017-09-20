from flask import Flask

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
                    textarea {
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }
                </style>
            </head>
            <body>
                <form action="/add" method="POST">
                    <label ="Rotate by"
                    <input type="text" id="rot" name="rot" value="0"/>
                    <input type="textarea" id="text" name="text"/>
                    <input type="submit"/>
                
            </body>
        </html>   
        """ 

@app.route("/add")
def add():
    request.args.get("Rotate by")
    return 

app.run()