# Week 3 – Multi-Factor Authentication (MFA) & JWT Validation

## 📌 Objective
To implement secure authentication using OTP (Multi-Factor Authentication) and verify JWT tokens for role-based access control.

---

## 🔐 Tasks Completed

### 1. MFA (OTP) Implementation
- Enabled OTP authentication in Keycloak
- Configured user to complete OTP setup
- Verified login using OTP code

### 2. Application Integration
- Flask application redirects user to Keycloak login
- After authentication, receives authorization code
- Exchanges code for Access Token (JWT)

### 3. JWT Token Validation
- Access Token captured from application
- Token decoded using https://jwt.io
- Verified claims inside token

---

## 🔍 JWT Claims Verified

- Username: `kripal`
- Role: `developer`
- Client ID: `my-app`
- Scope: `profile email`
- Issuer: Keycloak (Infotact Realm)

---

## 📊 Result

- OTP-based login successfully implemented
- Secure authentication flow working
- JWT token correctly contains user identity and roles
- Role-Based Access Control (RBAC) validated

---

## 🛠️ Tools Used

- Keycloak (Identity & Access Management)
- Flask (Python Web Framework)
- JWT.io (Token Decoder)
- Kali Linux

---

## 📸 Screenshots

| Feature | Description |
|--------|------------|
| OTP Setup | QR Code configuration |
| OTP Login | OTP verification screen |
| JWT Decoded | Token claims verification |
| Login Success | Access token display |

---

## 🚀 Conclusion

This week demonstrates secure authentication using MFA and verifies authorization using JWT tokens, ensuring proper identity and access management.
