# 🕵️ Shadow Route Scanner (Obscurity-Buster)

![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

An asynchronous Proof of Concept (PoC) scanner designed to expose the dangers of **"Security by Obscurity"** by hunting down unauthenticated and hidden API endpoints in development environments.

## 📖 The Backstory: Why Did I Build This?

This project was born out of a real-world penetration testing engagement. While analyzing a massive corporate infrastructure, I discovered that the development team relied entirely on keeping their API URLs undocumented to ensure security. By assuming "nobody knows the URLs," they left critical endpoints without any authentication layers. 

I built this local laboratory to demonstrate exactly how easily a threat actor can bypass such flawed architectures using asynchronous concurrency and a simple wordlist.

**Read the full penetration testing log and case study:**
* 🇬🇧 **English (Hashnode):** [The "Security by Obscurity" Fallacy: How I Took Over a Corporate Infrastructure by Browsing Folders](https://asyali-beep.hashnode.dev/the-security-by-obscurity-fallacy-how-i-took-over-a-corporate-infrastructure-by-browsing-folders)
* 🇹🇷 **Türkçe (LinkedIn):** [Security by Obscurity Yanılgısı: Kurumsal Bir Altyapıyı Klasör Gezerek Nasıl Teslim Aldım?](https://www.linkedin.com/pulse/security-obscurity-yan%C4%B1lg%C4%B1s%C4%B1-kurumsal-bir-altyap%C4%B1y%C4%B1-klas%C3%B6r-eren-eaief/?trackingId=WLMe6IhTS5qKErG9Xxl%2FFg%3D%3D)

> **Core Philosophy:** Hiding an endpoint is not a substitute for proper authentication. **Zero Trust** is the only reliable architecture.

---

## 🏗️ Repository Structure

This repository is designed as a self-contained local laboratory. It includes both the vulnerable target and the scanning engine.

* `scanner.py` — The asynchronous scanning engine (PoC)
* `test_server.py` — A vulnerable Flask dummy server
* `requirements.txt` — Python dependencies
* `wordlists/common.txt` — Dictionary of common hidden/forgotten endpoints

## 🚀 Quick Start & Local Lab

You can test the methodology safely in your local environment using the included dummy server.

### 1. Install Dependencies
Clone the repository and install the required Python libraries:

```bash
git clone [https://github.com/Asyali-beep/shadow-route-scanner.git](https://github.com/Asyali-beep/shadow-route-scanner.git)
cd shadow-route-scanner
pip install -r requirements.txt
```

### 2. Start the Vulnerable Server
Run the dummy server. This Flask application simulates an environment with both properly secured endpoints and hidden, unauthenticated endpoints.

```bash
python test_server.py
```
*(The server will start on http://127.0.0.1:5000)*

### 3. Run the Shadow Route Scanner
Open a new terminal window and launch the asynchronous scanner to hunt down the vulnerabilities on the local server:

```bash
python scanner.py
```

## 🎯 Example Output

The scanner analyzes HTTP status codes to detect access control failures in real-time. 

```text
--- Shadow Route Scanner (Local Proof of Concept) ---
Target: [http://127.0.0.1:5000](http://127.0.0.1:5000)

[+] Secure (Protected): [http://127.0.0.1:5000/api/secure/data](http://127.0.0.1:5000/api/secure/data) | Status: 401
[!] VULNERABILITY (No Auth): [http://127.0.0.1:5000/api/internal/backup](http://127.0.0.1:5000/api/internal/backup) | Status: 200 OK
[-] Not Found: [http://127.0.0.1:5000/api/admin/metrics](http://127.0.0.1:5000/api/admin/metrics) | Status: 404
[!] VULNERABILITY (No Auth): [http://127.0.0.1:5000/api/dev/debug](http://127.0.0.1:5000/api/dev/debug) | Status: 200 OK
```

* **Green (`401/403`):** The endpoint correctly requires authentication.
* **Red (`200 OK`):** The endpoint is active and lacks authentication (CRITICAL).

## ⚠️ Disclaimer

This project, including the scanner and wordlists, is created strictly for **educational purposes and local Proof of Concept (PoC) testing**. The `scanner.py` is hardcoded to target `localhost`. Do not modify this code to scan external networks, servers, or infrastructures without explicit, written authorization from the owners.
