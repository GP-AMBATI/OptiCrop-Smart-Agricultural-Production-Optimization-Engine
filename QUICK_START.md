# 🚀 Quick Start OptiCrop - One Command Solutions

Choose your preferred method below:

---

## **Method 1: Double-Click (Easiest) ⭐**

Simply **double-click one of these files** in your project folder:

### Option A: `start.bat` (Recommended)
- Double-click `start.bat` 
- Two command windows open automatically
- Servers start in ~5 seconds
- Opens http://localhost:5173 in a few seconds

### Option B: `run-all.bat`
- Alternative batch file with similar functionality

---

## **Method 2: One-Line Command**

Open PowerShell in your project folder and run:

```powershell
.\start.bat
```

Or from Command Prompt:
```cmd
start.bat
```

---

## **Method 3: Python Command (Advanced)**

```bash
python start.py
```

---

## **Method 4: Create Windows Shortcut (Pro Tip)**

### Step 1: Create Shortcut
1. Right-click on `start.bat` in your project folder
2. Click "Send to" → "Desktop (create shortcut)"
3. A shortcut appears on your desktop

### Step 2: Run Anytime
- Double-click the shortcut on your desktop
- Project launches automatically!

### Optional: Rename Shortcut
- Right-click shortcut → Rename
- Change to: `OptiCrop` or `🌾 OptiCrop`

---

## **Method 5: Add to Windows PATH (Advanced Users)**

Make `start.bat` runnable from anywhere:

1. Press `Win + X` → "System"
2. Click "Advanced system settings"
3. Click "Environment Variables..."
4. Under "User variables", click "New..."
5. Variable name: `PATH`
6. Variable value: `c:\Users\ashis\Desktop\project`
7. Click OK → OK → OK
8. Restart PowerShell/CMD

Then run from anywhere:
```powershell
cd c:\Users\ashis\Desktop\project
start.bat
```

---

## **What Happens When You Run It**

```
========================================
  OptiCrop Project Launcher
========================================

[1/2] Starting Backend (Flask)...
[2/2] Starting Frontend (React)...

========================================
  OptiCrop is now running!
========================================

Frontend: http://localhost:5173
Backend:  http://localhost:5000
```

✅ Two terminal windows open
✅ Backend starts on port 5000
✅ Frontend starts on port 5173
✅ Ready to use in ~5-10 seconds

---

## **Stopping the Servers**

- **Method 1**: Close either terminal window → Both stop
- **Method 2**: Press `Ctrl+C` in terminal
- **Method 3**: Task Manager → End Task on "node" or "python"

---

## **Accessing Your App**

After running any command above:

1. **Wait 5-10 seconds** for servers to fully start
2. **Open browser**: `http://localhost:5173`
3. You'll see the beautiful OptiCrop UI
4. Fill in the form and click "Generate Recommendation"

---

## **Troubleshooting**

### "Port already in use" error
- Close other applications using ports 5173 or 5000
- Or kill existing processes:
  ```powershell
  # Windows - Kill Node process
  taskkill /IM node.exe /F
  
  # Windows - Kill Python process  
  taskkill /IM python.exe /F
  ```

### "npm command not found"
- Reinstall Node.js from nodejs.org
- Restart terminal/PowerShell

### "python not found"
- Reinstall Python from python.org
- Make sure "Add Python to PATH" is checked

---

## **The QUICKEST Way** ⚡

```
1. Go to: c:\Users\ashis\Desktop\project
2. Double-click: start.bat
3. Wait 5 seconds
4. Go to: http://localhost:5173
5. Done! ✓
```

---

## **Create Desktop Shortcut (My Recommendation)**

1. Right-click `start.bat`
2. "Send to" → "Desktop (create shortcut)"
3. Rename to: "🌾 OptiCrop"
4. Double-click anytime to launch!

Now you have a one-click launcher for your entire project! 🎉
