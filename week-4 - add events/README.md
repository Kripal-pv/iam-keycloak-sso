# Week 4 – Logging & Security Testing

## 📌 Objective
To enable user activity monitoring and perform basic security testing on the authentication system.

---

## 📊 Tasks Completed

### 1. User Event Logging
- Enabled "Save Events" in Keycloak
- Enabled "Admin Events"
- Configured event types:
  - LOGIN
  - LOGIN_ERROR
  - LOGOUT

### 2. Monitoring User Activity
- Verified logs for:
  - Successful login
  - Failed login attempts
  - Logout events
- Observed logs under "User Events" section

---

## 🔐 Security Testing

### ✔ Open Redirect Test
- Attempted to manipulate redirect URI with a malicious URL
- Keycloak blocked the request successfully
- Confirmed system is protected against Open Redirect attacks

### ✔ Session Handling Test
- Logged in → Logged out → Logged in again
- Verified that a new session is created
- Confirmed system is not vulnerable to session fixation

---

## 📊 Result

- Event logging successfully tracks user activities
- System prevents unauthorized redirects
- Secure session management verified

---

## 🛠️ Tools Used

- Keycloak
- Flask (Python)
- Kali Linux

---

## 📸 Screenshots

| Feature | Description |
|--------|------------|
| Event Config | Logging enabled |
| Event Logs | User activity logs |
| Open Redirect Test | Attack blocked |
| Session Test | Secure session handling |

---

## 🚀 Conclusion

Week 4 demonstrates monitoring and security validation of the authentication system. The system successfully logs user activities and protects against common authentication vulnerabilities.
