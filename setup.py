#!/usr/bin/env python3
"""
Setup script for Surakhshat - AI-Powered Cybersecurity Surveillance System
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def check_node_version():
    """Check if Node.js is installed"""
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        print(f"✅ Node.js {result.stdout.strip()} is installed")
        return True
    except FileNotFoundError:
        print("❌ Node.js is not installed. Please install Node.js 14+ from https://nodejs.org/")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Surakhshat - AI-Powered Cybersecurity Surveillance System")
    print("=" * 70)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
    
    if not check_node_version():
        sys.exit(1)
    
    # Install Python dependencies
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        print("💡 Try: pip install --upgrade pip")
        sys.exit(1)
    
    # Install Node.js dependencies
    if not run_command("npm install", "Installing Node.js dependencies"):
        sys.exit(1)
    
    # Build CSS
    if not run_command("npm run build", "Building Tailwind CSS"):
        sys.exit(1)
    
    # Check if models directory exists
    if not os.path.exists("models"):
        print("⚠️  Models directory not found. Please ensure model files are in the 'models/' directory")
        print("   Required files:")
        print("   - models/border_anomaly_detector.h5")
        print("   - models/RandomForest_ThreatAnalysisAI.pkl")
    else:
        print("✅ Models directory found")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Ensure your ML models are in the 'models/' directory")
    print("2. Run the application: python surakhshat_app.py")
    print("3. Open your browser: http://localhost:5000")
    print("4. Login with: admin/password123 or operator/securepass456")
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main()
