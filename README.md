# 🔐 IAM System using Keycloak (SSO, MFA & Security)

## 📌 Project Overview
This project demonstrates the implementation of an Identity and Access Management (IAM) system using Keycloak. It includes secure authentication, Single Sign-On (SSO), Multi-Factor Authentication (MFA), JWT validation, and security monitoring.

---

## 🛠️ Technologies Used
- Keycloak (IAM)
- Flask (Python)
- Docker
- OpenID Connect (OIDC)
- JWT (JSON Web Token)
- Kali Linux

---

## 📅 Project Breakdown

### 🔹 Week 1 – Identity Setup
- Installed Keycloak using Docker
- Created Realm (Infotact)
- Created Users and Roles
- Assigned roles to users

---

### 🔹 Week 2 – SSO Integration
- Created OIDC client (my-app)
- Configured redirect URIs
- Developed Flask application
- Implemented login redirection
- Received authorization code

---

### 🔹 Week 3 – MFA & JWT Validation
- Enabled OTP-based MFA
- Configured user authentication flow
- Generated Access Token (JWT)
- Decoded JWT using jwt.io
- Verified:
  - Username
  - Roles
  - Client ID
  - Scope

---

### 🔹 Week 4 – Logging & Security Testing
- Enabled user event logging
- Captured login, logout, and login failure events
- Verified event logs
- Performed security testing:
  - Open Redirect protection
  - Session handling validation

---

## 🔄 Authentication Flow

User → Application → Keycloak → Login → Redirect → Application → Access Granted

---

## 🔐 Key Features

- Centralized Authentication (IAM)
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)
- JWT-based Authorization
- Role-Based Access Control (RBAC)
- Event Logging & Monitoring
- Basic Security Testing

---

## 📸 Screenshots

- Keycloak Setup (Week 1)
- Login & SSO Flow (Week 2)
- OTP & JWT Verification (Week 3)
- Event Logs & Security Tests (Week 4)

---

## 🚀 How to Run

### 1. Start Keycloak
```bash
docker-compose up -d
