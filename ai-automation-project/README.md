# AI Automation Project 🚀

This project demonstrates **AI-assisted test automation** using:
- **Cursor / Copilot (Global AI)** → fast code generation & structure
- **Ollama (Local AI)** → secure refinements, negative test cases
- **Human Touch** → final polish & professional framework design

### 🔹 Project Highlights:
- **Playwright + Pytest + Allure** test framework
- **POM structure** (pages, tests, conftest)
- AI-driven workflow:
  1. Global AI → generates initial code
  2. Local AI → refines and secures
  3. Human → integrates and finalizes

---

### ▶️ How to run:
```bash
pip install -r requirements.txt
pytest --alluredir=reports
allure serve reports
```

---

### 📸 Example:
See `tests/test_login_ai.py` – AI-assisted login test.
