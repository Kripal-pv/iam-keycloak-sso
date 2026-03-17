from flask import Flask, redirect, request

app = Flask(__name__)

KEYCLOAK_URL = "http://192.168.1.10:8080"
REALM = "Infotact"
CLIENT_ID = "my-app"
REDIRECT_URI = "http://192.168.1.10:5000/callback"

@app.route("/")
def home():
    return redirect(
        f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/auth"
        f"?client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
    )

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"✅ Login Successful! Code: {code}"

app.run(host="0.0.0.0", port=5000)
