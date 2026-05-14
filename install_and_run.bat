@echo off
chcp 65001 >nul
if not exist .venv (
  python -m venv .venv
)
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python main.py --smoke-test
if errorlevel 1 (
  echo Smoke test failed.
  exit /b 1
)
python main.py
