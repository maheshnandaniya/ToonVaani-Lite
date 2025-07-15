# 🐘 ToonVaani-Lite

**ToonVaani-Lite** is a lightweight Django-based offline cartoon storytelling tool for kids.  
It reads stories from a text file, generates audio using AI voice (gTTS), and plays it with visuals.

---

## 💡 Features
- Reads story from `story.txt`
- Generates voice using Google Text-to-Speech (gTTS)
- Plays story + audio on a simple webpage
- Works fully offline (after first run)
- Built for mobile (Termux) and PC

---

## 📦 Requirements

- Python 3.9+
- pip
- Django 4.2
- gTTS
- Pillow

---

## 🛠️ Installation (Mobile via Termux)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/maheshnandaniya/ToonVaani-Lite
cd ToonVaani-Lite
pip install -r requirements.txt
python manage.py runserver
