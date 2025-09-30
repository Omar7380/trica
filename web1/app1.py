from flask import Flask

app = Flask(__name__, static_folder="img")

@app.route("/")
def stop_harcelement():
    return """
    <html>
        <head>
            <style>
                /* ...styles identiques... */
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Serveur 1</h2>
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
    app.run(host="0.0.0.0", port=80)