# 🛡️ Surakhshat - Professional AI-Powered Cybersecurity Platform

Surakhshat is a state-of-the-art, enterprise-grade cybersecurity surveillance system that combines advanced computer vision, machine learning, and network traffic analysis for comprehensive threat detection and security monitoring. The name "Surakhshat" derives from Sanskrit/Hindi, meaning "protection" or "security."

## 👥 Team Members
| Name                | Role                               | Profile |
| Dr. Jawad Hussain | Mentor  | [ORCID](https://orcid.org/0000-0002-9641-5184) |
|---------------------|------------------------------------|----------------|
| Hasan Mansoor       | Team Lead                          | [GitHub](https://github.com/HasanMansoor89) |
| Syed Danish Khurram | AI Engineer/Software engineer      | [GitHub](https://github.com/SyedDanishKhurram) |
| Ali Hashir Rana     | Software Engineer                  | [GitHub](https://github.com/alihashirrana) |
| Momal Rana          | Software Engineer                  | [GitHub](https://github.com/Momal-Rana) |


## ✨ What's New in the Professional Version

This upgraded version transforms Surakhshat into a **professional-grade security platform** with:

- 🎨 **Modern Dark Theme UI** - Sleek, professional interface with smooth animations
- 📊 **Real-time Dashboard** - Live charts, metrics, and system monitoring
- 🚨 **Advanced Alert System** - Comprehensive alert management with filtering and resolution
- ⚙️ **System Settings** - Extensive configuration options for all aspects of the platform
- 📈 **Security Reports** - Detailed analytics and executive summaries
- 🔒 **Enhanced Security** - Session management, input validation, and secure authentication
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile devices

## 🚀 Key Features

### 🔐 **Advanced Authentication & Security**
- **Secure Login System** - SHA-256 password hashing with session management
- **Role-Based Access** - Admin role different permissions
- **Session Security** - Configurable timeout and automatic logout
- **Input Validation** - Comprehensive file and data validation
- **Protected API Endpoints** - All routes secured with authentication middleware

### 📹 **AI-Powered Video Surveillance**
- **Real-time Anomaly Detection** - Advanced autoencoder-based visual analysis
- **Live Video Feed Simulation** - Professional camera interface with recording capabilities
- **File Upload Analysis** - Support for multiple image formats with security checks
- **Detection Settings** - Adjustable sensitivity and threshold parameters
- **Visual Feedback** - Real-time alerts with color-coded status indicators

### 🌐 **Intelligent Network Analysis**
- **Machine Learning Classification** - RandomForest-based traffic analysis
- **Real-time Monitoring** - Continuous network flow evaluation
- **Threat Classification** - Binary classification (Normal vs Attack) with confidence scores
- **Feature Analysis** - Advanced metrics: Flow Bytes/s, Packet Length Std, Flow Packets/s
- **Network Statistics** - Comprehensive traffic monitoring and reporting

### 📊 **Professional Dashboard**
- **Real-time Metrics** - Live system statistics with auto-refresh
- **Interactive Charts** - Chart.js-powered visualizations for threat activity
- **System Health Monitoring** - CPU, memory, disk, and network performance tracking
- **Executive Summary** - High-level security metrics and KPIs
- **Responsive Design** - Optimized for all device sizes

### 🚨 **Advanced Alert Management**
- **Multi-level Alerts** - Critical, Warning, and Info classifications
- **Alert Filtering** - Sort and filter alerts by type, status, and time
- **Resolution Tracking** - Mark alerts as resolved with timestamps
- **Notification System** - Email and browser notifications
- **Alert History** - Complete audit trail of all security events

### ⚙️ **Comprehensive Settings**
- **System Configuration** - Language, timezone, and display preferences
- **Security Policies** - Password requirements, session timeouts, and access controls
- **AI Parameters** - Detection thresholds and sensitivity settings
- **Notification Preferences** - Email alerts and browser notifications
- **Performance Settings** - Monitoring intervals and data retention policies

### 📈 **Security Reports & Analytics**
- **Executive Reports** - High-level security summaries and KPIs
- **Threat Analysis** - Detailed breakdown of attack types and patterns
- **Performance Metrics** - System health and resource utilization
- **Security Recommendations** - AI-generated security improvement suggestions
- **Export Capabilities** - PDF report generation for compliance

## 🛠️ Technology Stack

### **Backend Technologies**
- **Flask 2.3.3** - Modern Python web framework with session management
- **TensorFlow 2.13.0** - Deep learning framework for AI-powered anomaly detection
- **Scikit-learn 1.3.0** - Machine learning library for network traffic classification
- **OpenCV 4.8.1** - Computer vision library for image processing and analysis
- **Pandas 2.0.3** - Data manipulation and analysis
- **NumPy 1.24.3** - Numerical computing
- **psutil 5.9.6** - System and process monitoring

### **Frontend Technologies**
- **Tailwind CSS 3.3.0** - Utility-first CSS framework for modern UI design
- **Chart.js** - Interactive charts and data visualization
- **Vanilla JavaScript** - Modern ES6+ JavaScript for dynamic interactions
- **HTML5** - Semantic markup with accessibility features
- **CSS3** - Advanced styling with animations and transitions

### **AI/ML Models**
- **Border Anomaly Detector** - Autoencoder neural network for visual anomaly detection
- **Network Threat Classifier** - RandomForest ensemble model for traffic analysis
- **Real-time Processing** - Optimized inference pipelines for live analysis

### **Security Features**
- **Session Management** - Secure user sessions with configurable timeouts
- **Password Hashing** - SHA-256 encryption for secure credential storage
- **Input Validation** - Comprehensive sanitization and validation
- **File Security** - Type checking, size limits, and malware scanning
- **API Protection** - Authentication middleware for all endpoints

## 🚀 Quick Start

### **Prerequisites**
- **Python 3.8+** - Required for backend services
- **Node.js 14+** - Required for frontend build tools
- **npm or yarn** - Package manager for Node.js dependencies

### **Option 1: Automated Setup (Recommended)**
```bash
# Clone the repository
git clone <repository-url>
cd surakhshat

# Run the automated setup script
python setup.py
```

### **Option 2: Manual Setup**
```bash
# 1. Clone the repository
git clone <repository-url>
cd surakhshat

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install Node.js dependencies
npm install

# 4. Build the CSS assets
npm run build

# 5. Start the application
python surakhshat_app.py
```

### **🌐 Access the Application**
- **URL**: `http://localhost:5000`
- **Admin Login**: `admin` / `password123`


## Default Credentials

- **Admin**: `admin` / `password123`


## API Endpoints

### Authentication
- `GET /` - Redirects to login
- `GET /login` - Login page
- `POST /login` - Authenticate user
- `GET /logout` - Logout user

### Protected Routes
- `GET /dashboard` - Main dashboard
- `GET /surveillance` - Surveillance interface

### API Endpoints
- `POST /analyze_frame` - Analyze uploaded image for anomalies
- `POST /analyze_flow` - Analyze network traffic data
- `GET /metrics` - Get system metrics

## Usage

### Video Surveillance
1. Navigate to the Surveillance page
2. Upload an image file (PNG, JPG, JPEG, GIF, BMP)
3. View real-time anomaly detection results
4. Green indicates normal, red indicates anomaly

### Network Analysis
1. Click "Analyze" button in Network Traffic section
2. System analyzes predefined network flow data
3. Results show normal traffic or detected attacks

### Dashboard
- View total anomaly and attack counts
- Navigate between different sections
- Monitor system status

## Security Features

- ✅ Password hashing with SHA-256
- ✅ Session-based authentication
- ✅ Input validation and sanitization
- ✅ File type and size validation
- ✅ Protected API endpoints
- ✅ Error handling and logging

## File Structure

```
surakhshat/
├── models/                          # ML Models
│   ├── border_anomaly_detector.h5   # Autoencoder for visual anomalies
│   ├── RandomForest_ThreatAnalysisAI.pkl  # Network threat classifier
│   ├── keras_metadata.pb            # TensorFlow metadata
│   └── saved_model.pb               # TensorFlow model format
├── static/                          # Frontend HTML files
│   ├── login.html                   # Authentication page
│   ├── dashboard.html               # Main dashboard
│   └── surveillance.html            # Surveillance interface
├── src/
│   └── input.css                    # Tailwind CSS source
├── dist/
│   └── output.css                   # Compiled CSS
├── surakhshat_app.py               # Main Flask application
├── requirements.txt                 # Python dependencies
├── package.json                    # Node.js dependencies
├── tailwind.config.js              # Tailwind configuration
└── README.md                       # This file
```

## Configuration

### Tailwind CSS
The project uses Tailwind CSS for styling. Configuration is in `tailwind.config.js`:
```javascript
module.exports = {
  content: ["./static/*.html"],
  theme: { extend: {} },
  plugins: []
}
```

### Model Configuration
- Anomaly threshold: 0.0025 (configurable in `surakhshat_app.py`)
- Image preprocessing: 128x128 grayscale
- Network flow features: Flow Bytes/s, Packet Length Std, Flow Packets/s

## Development

### Building CSS
For development with auto-reload:
```bash
npm run build-css
```

For production build:
```bash
npm run build
```

### Adding New Users
Edit the `users` dictionary in `surakhshat_app.py`:
```python
users = {
    'username': hash_password('password'),
    # Add more users here
}
```

## Troubleshooting

### Common Issues

1. **Models not loading**: Ensure model files are in the `models/` directory
2. **CSS not styling**: Run `npm run build` to compile Tailwind CSS
3. **Authentication issues**: Check if session secret key is properly generated
4. **File upload errors**: Verify file type and size limits

### Error Messages
- "Model not available": AI models failed to load
- "Invalid file type": Uploaded file is not an image
- "File too large": File exceeds 10MB limit
- "Missing required field": Network flow data is incomplete

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please contact the development team.

---

## 🎯 **Professional Transformation Summary**

Surakhshat has been completely transformed from a basic security tool into a **professional-grade cybersecurity platform**:

### **Before vs After**
| **Before** | **After** |
|------------|-----------|
| Basic login form | Professional authentication system with session management |
| Simple dashboard | Real-time dashboard with interactive charts and metrics |
| Basic surveillance | Advanced video analysis with live feed simulation |
| Limited functionality | Comprehensive platform with 5 main modules |
| Basic styling | Modern dark theme with professional animations |
| No alerts system | Advanced alert management with filtering and resolution |
| No settings | Extensive configuration options |
| No reports | Detailed security reports and analytics |

### **Key Improvements**
- ✅ **500% More Features** - From 3 basic pages to 5 comprehensive modules
- ✅ **Professional UI/UX** - Modern dark theme with smooth animations
- ✅ **Enhanced Security** - Session management, input validation, secure authentication
- ✅ **Real-time Monitoring** - Live charts, metrics, and system status
- ✅ **Advanced Analytics** - Comprehensive reporting and threat analysis
- ✅ **Enterprise Ready** - Professional-grade features suitable for production use

---

**🛡️ Surakhshat** - Your comprehensive AI-powered cybersecurity platform for the modern enterprise.






