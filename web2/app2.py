from flask import Flask

app = Flask(__name__, static_folder="img")

@app.route("/")
def stop_harcelement():
    return """
    <html>
        <head>
            <style>
                body {
                    background: linear-gradient(120deg, #4facfe 0%, #00f2fe 100%);
                    font-family: 'Segoe UI', Arial, sans-serif;
                    color: #222;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    margin: 60px auto;
                    max-width: 500px;
                    background: rgba(255,255,255,0.95);
                    border-radius: 18px;
                    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
                    padding: 40px 30px 30px 30px;
                    text-align: center;
                }
                h1 {
                    color: #0078d7;
                    margin-bottom: 18px;
                }
                h2 {
                    color: #00bfae;
                    margin-bottom: 10px;
                }
                .message {
                    font-size: 1.3em;
                    margin: 24px 0 18px 0;
                    background: #e3f2fd;
                    color: #1565c0;
                    padding: 14px;
                    border-radius: 8px;
                }
                .support {
                    margin-top: 28px;
                    font-weight: bold;
                    font-size: 1.1em;
                    color: #ff9800;
                }
                .image-section {
                    margin: 28px 0;
                }
                img {
                    max-width: 220px;
                    border-radius: 12px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.13);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Serveur 2</h2>
                <h1>Catasnack</h1>
                <div class="message">
                    Venez au catasnack.<br>
                </div>
                <div class="image-section">
                    <img src="/img/raw.png" alt="CATAGROS">
                </div>
                <div class="support">
                    Samet Catasnack , merci 💙
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)