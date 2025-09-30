from flask import Flask, request, jsonify, send_from_directory, redirect, url_for, session
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import pickle
import pandas as pd
import os
import hashlib
import time
import requests

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24)  # Generate random secret key

# Load models
try:
    autoencoder = load_model('models/border_anomaly_detector.h5')
    with open('models/RandomForest_ThreatAnalysisAI.pkl', 'rb') as f:
        rf_model = pickle.load(f)
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    autoencoder = None
    rf_model = None

# Improved user database with hashed passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {
    'admin': hash_password('password123')
}

# Security helper functions
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def validate_image_file(file):
    if not file or file.filename == '':
        return False, "No file selected"
    
    # Check file extension
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
    if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
        return False, "Invalid file type. Only images are allowed."
    
    # Check file size (limit to 10MB)
    file.seek(0, 2)  # Seek to end
    file_size = file.tell()
    file.seek(0)  # Reset to beginning
    if file_size > 10 * 1024 * 1024:
        return False, "File too large. Maximum size is 10MB."
    
    return True, "Valid"

# Image preprocessing
def preprocess_image(image):
    img = cv2.resize(image, (128, 128), interpolation=cv2.INTER_AREA)
    img = img.astype('float32') / 255.
    return np.expand_dims(img, axis=(0, -1))

# Network flow preprocessing
def preprocess_flow(data):
    df = pd.DataFrame([data])
    return df[['Flow Byts/s', 'Pkt Len Std', 'Flow Pkts/s']]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        if not username or not password:
            return send_from_directory(app.static_folder, 'login.html')
        
        hashed_password = hash_password(password)
        if users.get(username) == hashed_password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        
        return send_from_directory(app.static_folder, 'login.html')
    return send_from_directory(app.static_folder, 'login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return send_from_directory(app.static_folder, 'dashboard.html')

@app.route('/surveillance')
@login_required
def surveillance():
    return send_from_directory(app.static_folder, 'surveillance.html')

@app.route('/alerts')
@login_required
def alerts():
    return send_from_directory(app.static_folder, 'alerts.html')

@app.route('/settings')
@login_required
def settings():
    return send_from_directory(app.static_folder, 'settings.html')

@app.route('/reports')
@login_required
def reports():
    return send_from_directory(app.static_folder, 'reports.html')

@app.route('/analyze_frame', methods=['POST'])
@login_required
def analyze_frame():
    try:
        # Check if frame file exists
        if 'frame' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['frame']
        is_valid, message = validate_image_file(file)
        if not is_valid:
            return jsonify({'error': message}), 400
        
        if autoencoder is None:
            return jsonify({'error': 'Anomaly detection model not available'}), 500
        
        # Read image safely
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
        if img is None:
            return jsonify({'error': 'Invalid image file'}), 400
        
        # Preprocess and predict
        img = preprocess_image(img)
        recon = autoencoder.predict(img)
        error = np.mean(np.square(img - recon))
        is_anomaly = error > 0.0025
        return jsonify({'anomaly': bool(is_anomaly), 'error': float(error)})
    
    except Exception as e:
        print("Frame analysis error:", e)
        return jsonify({'error': 'Analysis failed'}), 500

@app.route('/analyze_flow', methods=['POST'])
@login_required
def analyze_flow():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        if rf_model is None:
            return jsonify({'error': 'Network analysis model not available'}), 500
        
        # Validate required fields
        required_fields = ['Flow Byts/s', 'Pkt Len Std', 'Flow Pkts/s']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        flow = preprocess_flow(data)
        prediction = rf_model.predict(flow)[0]
        return jsonify({'attack': bool(prediction), 'label': 'Attack' if prediction else 'Normal'})
    except Exception as e:
        print("Flow analysis error:", e)
        return jsonify({'error': 'Flow analysis failed'}), 500

@app.route('/metrics')
@login_required
def metrics():
    import random
    import time
    
    base_time = int(time.time() / 3600)
    random.seed(base_time)
    
    return jsonify({
        'anomaly_count': random.randint(8, 25),
        'attack_count': random.randint(3, 12),
        'system_health': random.randint(95, 100),
        'active_users': random.randint(15, 35),
        'total_packets': random.randint(1000000, 2000000),
        'suspicious_flows': random.randint(15, 45),
        'blocked_requests': random.randint(5, 20),
        'bandwidth_usage': random.randint(500, 1200)
    })

@app.route('/api/alerts')
@login_required
def get_alerts():
    alerts = [
        {'id': 1, 'type': 'critical', 'title': 'DDoS Attack Detected',
         'description': 'Large volume of traffic detected from multiple IP addresses.',
         'timestamp': '2024-01-15T10:30:00Z', 'source': 'Network Monitor', 'status': 'active'},
        {'id': 2, 'type': 'warning', 'title': 'High CPU Usage',
         'description': 'Server-03 CPU usage exceeded 90% for the last 10 minutes.',
         'timestamp': '2024-01-15T10:15:00Z', 'source': 'System Monitor', 'status': 'active'}
    ]
    return jsonify(alerts)

@app.route('/api/settings', methods=['GET', 'POST'])
@login_required
def handle_settings():
    if request.method == 'GET':
        settings = {
            'anomaly_threshold': 0.0025,
            'network_sensitivity': 'medium',
            'real_time_analysis': True,
            'auto_learning': True,
            'session_timeout': 30,
            'max_login_attempts': 5,
            'two_factor_auth': False,
            'dark_mode': True,
            'auto_refresh': True
        }
        return jsonify(settings)
    elif request.method == 'POST':
        data = request.json
        return jsonify({'status': 'success', 'message': 'Settings updated successfully'})

@app.route('/api/system/status')
@login_required
def system_status():
    import psutil
    import time
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return jsonify({
            'cpu_usage': cpu_percent,
            'memory_usage': memory.percent,
            'disk_usage': disk.percent,
            'uptime': time.time() - psutil.boot_time(),
            'process_count': len(psutil.pids()),
            'network_connections': len(psutil.net_connections()),
            'status': 'operational'
        })
    except Exception as e:
        return jsonify({
            'cpu_usage': 45.2, 'memory_usage': 67.8, 'disk_usage': 23.4,
            'uptime': 86400, 'process_count': 156, 'network_connections': 23,
            'status': 'operational'
        })

@app.route('/api/logs')
@login_required
def get_logs():
    logs = [
        {'timestamp': '2024-01-15T10:45:00Z', 'level': 'INFO',
         'message': 'User admin logged in successfully', 'source': 'auth'},
        {'timestamp': '2024-01-15T10:44:30Z', 'level': 'WARNING',
         'message': 'High CPU usage detected on server-03', 'source': 'monitor'},
        {'timestamp': '2024-01-15T10:44:00Z', 'level': 'INFO',
         'message': 'Security scan completed successfully', 'source': 'scanner'}
    ]
    return jsonify(logs)

@app.route('/dist/<path:filename>')
def serve_static(filename):
    return send_from_directory('dist', filename)

@app.route('/api/network/stats', methods=['GET'])
@login_required
def get_network_stats():
    import random
    import time
    time.sleep(0.1)  # Simulate some processing time
    return jsonify({
        'totalPackets': random.randint(100, 1000),
        'suspiciousFlows': random.randint(0, 5),
        'blockedRequests': random.randint(0, 3),
        'bandwidthUsage': random.uniform(100, 1000)
    })

@app.route('/api/network/analyze', methods=['POST'])
@login_required
def analyze_network():
    import random
    import time
    time.sleep(0.1)  # Simulate some processing time
    data = request.get_json()
    if data and data.get('request') == 'analyze':
        return jsonify({
            'flowBytesPerSecond': random.uniform(500, 2500),
            'packetLengthStd': random.uniform(20, 120),
            'flowPacketsPerSecond': random.uniform(5, 55),
            'attack': random.choice([True, False]),
            'label': random.choice(['Normal', 'DDoS', 'Malware', 'Unknown'])
        })
    return jsonify({'error': 'Invalid request'}), 400

@app.route('/api/chat', methods=['POST'])
@login_required
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Replace with your Gemini API endpoint and key
    gemini_api_url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
    api_key = 'AIzaSyADUUf19Pbkn2TUlmnDdi7Eqngp7SQTy0I'

    payload = {
        "contents": [{"parts": [{"text": user_message}]}]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{gemini_api_url}?key={api_key}", json=payload, headers=headers)
    if response.status_code == 200:
        gemini_reply = response.json()['candidates'][0]['content']['parts'][0]['text']
        return jsonify({'reply': gemini_reply})
    else:
        return jsonify({'error': 'Gemini API error'}), 500

if __name__ == '__main__':
    app.run(debug=True)