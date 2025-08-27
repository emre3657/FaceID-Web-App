# Face ID Login

![maintenance: inactive](https://img.shields.io/badge/maintenance-inactive-lightgrey)
![stack: flask](https://img.shields.io/badge/stack-Flask-blue)
![db: mysql](https://img.shields.io/badge/db-MySQL-orange)

A web application that demonstrates **Face ID–based authentication** built with **Python (Flask)**.  
The app supports the standard email/username + password login flow and augments it with **face recognition**.  
A lightweight **anti-spoofing model** is included to reduce login attempts with printed/video faces.

> **Maintenance:** Not actively maintained. This repository is kept for reference/demos.  
> **Security:** This is **not** production-ready. Accuracy and liveness detection are limited.

---

## Features
- Username/email + password login
- Face enrollment: capture and encode face features, then store in DB
- Face verification at login (threshold-based matching)
- **Anti-spoofing model**: detects fake faces (prints/screens) — not 100% accurate
- MySQL persistence (single table storing user and face feature vectors)

---

## How it works (high level)
1. **Enroll:** User captures face via webcam; the app extracts face embeddings and stores them (as JSON) in MySQL alongside the user.
2. **Login:** On login, a fresh face capture is compared against stored embeddings. If similarity is above a threshold **and** anti-spoofing check passes, the session is allowed.
3. **Anti-spoofing:** A YOLO-based model trained with ~5k fake and ~5k real images (Google Colab) flags spoof attempts. This reduces but does not eliminate attacks.

---

## Tech Stack
- **Python 3.10**
- **Flask**
- **MySQL**
- **dlib / face-recognition / OpenCV** (face detection & embeddings)
- **YOLO** (anti-spoofing / liveness heuristic)
- Optional: **Anaconda/Miniconda** for isolated environment

---

## Requirements
- VS Code (or any editor)
- Python **3.10.x**
- MySQL Server & MySQL Workbench
- (Windows) Visual Studio 2022 **C/C++ Desktop Development** tools (needed for some wheels like `dlib`)
- (Optional) Conda/Miniconda

---

## Setup (Conda recommended)

```bash
# 1) Verify conda
conda --version    # e.g. conda 25.5.1

# 2) Create env
conda create -n faceid python=3.10 -y
conda activate faceid

# 3) Install dependencies (CPU by default)
pip install -r requirements.txt
```

### (Optional) GPU build for PyTorch
Edit `requirements.txt`:
```
torch==2.2.1        -> torch==2.2.1+cu121
torchvision==0.17.1 -> torchvision==0.17.1+cu121
torchaudio==2.2.1   -> torchaudio==2.2.1+cu121
```
Then:
```bash
pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cu121
```

---

## Database (MySQL)

Create a database (any name), then a table **`faceid`** with columns:
- `user_id`
- `username`
- `email`
- `password`  _(store hashed in real apps)_
- `face_features` _(JSON string with embeddings)_
- `token`
- `about`

> In production, normalize users vs. biometric templates; use salts/pepper, strict access controls, audit trails, and encryption at rest.

---

## Configuration

Create a `.flaskenv` (or `.env`) file in the project root:

```
FLASK_ENV=development
FLASK_APP=main.py
FLASK_DEBUG=True
SECRET_KEY=your_secret_key

DB_HOST=your_db_host
DB_PORT=your_db_port
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```

---

## Run

**Option A — Flask CLI**
```bash
conda activate faceid
flask run
```

**Option B — Python entry**
```bash
conda activate faceid
python main.py
```

The app usually starts at `http://127.0.0.1:5000/`.

---

## Notes on Accuracy & Security
- The anti-spoofing model **is not 100% accurate**. Thresholds may require tuning per environment.
- Do **not** deploy this as a sole authentication factor in production. Use MFA, rate limiting, logging, and lockouts.
- Ensure **legal compliance** (biometric privacy laws vary by region). Obtain explicit user consent and provide data deletion options.

---

## Roadmap (if development resumes)
- Improve liveness detection (blink, depth cues)
- Harden training & evaluation with balanced datasets
- Proper password hashing (Argon2/bcrypt) & session security
- Modular DB schema (users, embeddings, attempts, audit)
- Add tests and CI

## License
MIT
