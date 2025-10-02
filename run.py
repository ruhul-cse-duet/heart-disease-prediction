#!/usr/bin/env python3
"""
Heart Disease Prediction System - Launcher Script
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        import pandas
        import numpy
        import sklearn
        import lightgbm
        print("✅ All dependencies are installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_files():
    """Check if required files exist."""
    required_files = [
        "CVD_2021_BRFSS.csv",
        "models/best_lgb.pkl",
        "app.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    
    print("✅ All required files are present.")
    return True

def run_app():
    """Run the Streamlit application."""
    print("🚀 Starting Heart Disease Prediction System...")
    print("🌐 The app will open in your default browser.")
    print("📱 Local URL: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the application.\n")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.headless", "false",
            "--server.runOnSave", "true",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def main():
    """Main launcher function."""
    print("=" * 60)
    print("❤️  Heart Disease Prediction System")
    print("=" * 60)
    
    if not check_dependencies():
        sys.exit(1)
    
    if not check_files():
        print("\n💡 Tip: Make sure you have the dataset and model files in the correct locations.")
        sys.exit(1)
    
    run_app()

if __name__ == "__main__":
    main()

