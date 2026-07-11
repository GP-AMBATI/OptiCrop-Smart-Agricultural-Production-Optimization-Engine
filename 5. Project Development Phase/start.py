#!/usr/bin/env python3
"""
OptiCrop Project Launcher
Simple one-command start for the entire application
"""

import subprocess
import os
import sys
import time
import platform

def start_project():
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    print("\n" + "="*50)
    print("  OptiCrop - AI-Powered Crop Recommendation")
    print("="*50 + "\n")
    
    # Start backend
    print("[1/2] Starting Backend (Flask on port 5000)...")
    backend_cmd = [sys.executable, "app.py"]
    backend_process = subprocess.Popen(
        backend_cmd,
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    time.sleep(2)
    
    # Start frontend
    print("[2/2] Starting Frontend (React on port 5173)...")
    frontend_dir = os.path.join(project_root, "frontend")
    
    if platform.system() == "Windows":
        frontend_cmd = "npm run dev"
        frontend_process = subprocess.Popen(
            frontend_cmd,
            cwd=frontend_dir,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    else:
        frontend_cmd = ["npm", "run", "dev"]
        frontend_process = subprocess.Popen(
            frontend_cmd,
            cwd=frontend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    
    print("\n" + "="*50)
    print("  ✓ OptiCrop is now running!")
    print("="*50)
    print("\nFrontend: http://localhost:5173")
    print("Backend:  http://localhost:5000")
    print("\nPress Ctrl+C to stop all servers\n")
    
    try:
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        backend_process.terminate()
        frontend_process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    start_project()
