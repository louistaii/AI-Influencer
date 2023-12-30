@ECHO OFF
echo Installing Dependencies...
pip install -r requirements.txt
pause
cls
python -u "setup.py"
pause
cls
python -u "main.py"

