from flask import Flask

app = Flask(__name__, static_folder="img")

@app.route("/")
def stop_harcelement():
    return """
    <html>
        <head>
            <style>
                body {
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: white;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    margin-top: 7%;
                }
                h1 {
                    font-size: 3em;
                    background: rgba(0, 0, 0, 0.3);
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
                }
                .message {
                    font-size: 1.5em;
                    margin: 30px 0 20px 0;
                    background: rgba(0,0,0,0.2);
                    padding: 15px;
                    border-radius: 10px;
                }
                .support {
                    margin-top: 30px;
                    font-weight: bold;
                    font-size: 1.2em;
                    color: #ffe082;
                }
                .image-section {
                    margin: 30px 0;
                }
                img {
                    max-width: 350px;
                    border-radius: 12px;
                    box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>STOP à l'harcèlement</h1>
                <div class="message">
                    Ce n'est pas grave de finir 4ème.<br>
                    Ce qui compte, c'est de rebondir !
                </div>
                <div class="image-section">
                    <img src="/img/adam.png" alt="Soutien à Adamous Bougamus">
                </div>
                <div class="support">
                    Soutiens aux adamous bougamus, merci 💙
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)