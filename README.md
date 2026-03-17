# 🔐 IAM System using Keycloak (SSO)

## 📌 Overview
This project demonstrates Identity and Access Management (IAM) using Keycloak.  
It implements Single Sign-On (SSO) so users can log in once and access applications securely.

---

## 🛠️ Technologies Used
- Keycloak
- Docker
- Flask (Python)
- OpenID Connect (OIDC)

---

# 📅 Week 1 – Identity Setup

## ✔ Tasks
- Installed Keycloak using Docker
- Created Realm (Infotact)
- Created Users and Roles
- Assigned roles to user
- Verified login

## 📸 Screenshots

### 🔹 Realm Creation
![Realm](screenshots/week1-realm.png)

### 🔹 User & Role Setup
![User](screenshots/week1-user.png)

---

# 📅 Week 2 – SSO Integration

## ✔ Tasks
- Created OIDC Client (my-app)
- Configured redirect URIs
- Developed Flask app
- Implemented login redirection
- Received authorization code

## 🔄 Authentication Flow
User → App → Keycloak → Login → Redirect → App

## 📸 Screenshots

### 🔹 Keycloak Login
![Login](screenshots/week2-login.png)

### 🔹 Flask App Output
![Output](screenshots/week2-output.png)

---

## 🚀 How to Run

### 1. Start Keycloak
```bash
docker-compose up -d
