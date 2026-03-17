# 🔐 IAM System using Keycloak (SSO)

## 📌 Overview
This project demonstrates Identity and Access Management (IAM) using Keycloak.  
It enables secure authentication using Single Sign-On (SSO).

---

## 🛠️ Technologies
- Keycloak
- Docker
- Flask
- OpenID Connect (OIDC)

---

## 📅 Week 1 – Identity Setup
- Installed Keycloak
- Created Realm (Infotact)
- Created Users and Roles
- Assigned roles

## 📸 Screenshots
![Realm](screenshots/week1-realm.png)
![User](screenshots/week1-user.png)

---

## 📅 Week 2 – SSO Integration
- Created OIDC client (my-app)
- Configured redirect URIs
- Built Flask app
- Implemented SSO login

## 🔄 Flow
User → App → Keycloak → Login → Redirect → App

## 📸 Screenshots
![Login](screenshots/week2-login.png)
![Output](screenshots/week2-output.png)

---

## 🚀 Run Project

```bash
docker-compose up -d
python3 app.py
