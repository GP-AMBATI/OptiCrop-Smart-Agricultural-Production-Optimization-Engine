# OptiCrop - Setup & Running Instructions

## Quick Start Guide

Your OptiCrop application is ready to run! Here's how to get it up and running:

### Option 1: Using Batch Files (Recommended for Windows)

1. **Run Everything at Once:**
   - Double-click the `run-all.bat` file in the project root
   - This will open two command prompt windows:
     - One running the React frontend dev server
     - One running the Flask backend

2. **Wait for the servers to start** (approximately 10-20 seconds)

3. **Open your browser and go to:**
   ```
   http://localhost:5173
   ```

### Option 2: Manual Setup

#### Terminal 1 - Start the Frontend:
```bash
cd c:\Users\ashis\Desktop\project\frontend
npm run dev
```

#### Terminal 2 - Start the Backend:
```bash
cd c:\Users\ashis\Desktop\project
python app.py
```

#### Then open:
```
http://localhost:5173
```

## Architecture Overview

- **Frontend:** React + TypeScript + Tailwind CSS + Vite (running on `http://localhost:5173`)
- **Backend:** Flask API (running on `http://localhost:5000`)
- **API Proxy:** Vite automatically proxies `/predict` requests to the backend

## Features

✅ Beautiful, modern UI with the latest web design standards
✅ Real-time crop recommendations based on soil and weather data
✅ AI-powered predictions using machine learning models
✅ Responsive design that works on all devices
✅ Input validation and error handling

## How to Use

1. Navigate to http://localhost:5173
2. Enter your field conditions:
   - Nitrogen (N) level (mg/kg)
   - Phosphorus (P) level (mg/kg)
   - Potassium (K) level (mg/kg)
   - Temperature (°C)
   - Humidity (%)
   - Soil pH
   - Rainfall (mm)
3. Click "Predict Crop" button
4. Get your crop recommendation with confidence score

## Troubleshooting

### "Port already in use" error
- If port 5173 or 5000 is already in use, close other applications using those ports
- Or update the ports in `frontend/vite.config.ts` and `app.py`

### PowerShell Execution Policy Error
- Use the batch files provided, or
- Open Command Prompt (cmd.exe) instead of PowerShell
- Or run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Frontend not loading
- Check that the backend is running on `http://localhost:5000`
- Check browser console (F12) for any errors
- Make sure all dependencies are installed: `npm install` in the frontend folder

### Backend errors
- Ensure all Python dependencies are installed: `pip install -r requirements.txt`
- Check that the models are trained and artifacts are available

## Project Structure

```
project/
├── frontend/              # React TypeScript frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── App.tsx       # Main app component
│   │   └── main.tsx      # Entry point
│   ├── vite.config.ts    # Vite configuration
│   └── package.json
├── app.py                # Flask backend
├── database.py           # Database models
├── model.py              # ML model
├── requirements.txt      # Python dependencies
└── run-all.bat           # Quick start script
```

## Next Steps

1. ✅ Start both servers using `run-all.bat`
2. ✅ Open http://localhost:5173
3. ✅ Test the crop recommendation form
4. ✅ Deploy to production (e.g., Render, Heroku)

Enjoy using OptiCrop! 🌾
