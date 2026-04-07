from flask import Flask, redirect, request
import requests

app = Flask(__name__)

KEYCLOAK_URL = "http://192.168.1.10:8080"
REALM = "Infotact"
CLIENT_ID = "my-app"
CLIENT_SECRET = "your-client-secret"  # get from Keycloak (Credentials tab)
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

    # Exchange code for token
    token_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(token_url, data=data)
    token_json = response.json()

    access_token = token_json.get("access_token")

    return f"""
    <h2>✅ Login Successful</h2>
    <p><b>Access Token:</b></p>
    <textarea rows="10" cols="100">{access_token}</textarea>
    """

app.run(host="0.0.0.0", port=5000)
