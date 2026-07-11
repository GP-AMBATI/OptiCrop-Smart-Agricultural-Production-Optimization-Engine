@echo off
echo Starting OptiCrop application...
echo.
echo 1. Starting Frontend Dev Server...
start cmd /k "cd /d C:\Users\ashis\Desktop\project\frontend && npm run dev"
echo.
echo 2. Starting Backend Flask Server...
start cmd /k "cd /d C:\Users\ashis\Desktop\project && python app.py"
echo.
echo Both servers are starting. Frontend will be available at http://localhost:5173
echo Backend will be available at http://localhost:5000
pause
