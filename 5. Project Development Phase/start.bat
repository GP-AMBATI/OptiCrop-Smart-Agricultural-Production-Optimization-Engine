@echo off
title OptiCrop - AI-Powered Crop Recommendation
echo.
echo ========================================
echo   OptiCrop Project Launcher
echo ========================================
echo.
echo Starting OptiCrop application...
echo.

cd /d "%~dp0"

echo [1/2] Starting Backend (Flask)...
start "OptiCrop Backend" cmd /k "python app.py"

timeout /t 2 /nobreak

echo [2/2] Starting Frontend (React)...
start "OptiCrop Frontend" cmd /k "cd frontend && npm run dev"

timeout /t 3 /nobreak

echo.
echo ========================================
echo   OptiCrop is now running!
echo ========================================
echo.
echo Frontend: http://localhost:5173
echo Backend:  http://localhost:5000
echo.
echo Both windows will stay open. Close them to stop the servers.
echo Press any key to close this launcher window...
echo.
pause
