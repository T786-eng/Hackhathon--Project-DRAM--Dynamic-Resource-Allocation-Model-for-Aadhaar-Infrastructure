@echo off
REM Activate venv if present and start Streamlit in a new window, then open Chrome
if exist ".venv\Scripts\activate.bat" (
  call .venv\Scripts\activate.bat
)
REM Ensure dependencies installed (optional)
pip install -r requirements.txt >nul 2>&1
start "Streamlit" cmd /k "streamlit run app.py --server.address 127.0.0.1 --server.port 8501"
timeout /t 2 >nul
start "" "chrome" "http://127.0.0.1:8501"
