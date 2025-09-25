from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
        <head>
            <style>
                body {
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: white;
                    margin-top: 20%;
                }
                h1 {
                    font-size: 3em;
                    background: rgba(0, 0, 0, 0.3);
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
                }
            </style>
        </head>
        <body>
            <h1>Adam a fini 4ème 🏆</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
