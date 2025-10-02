# ❤️ Heart Disease Prediction System

A comprehensive machine learning-powered web application for predicting heart disease risk and providing treatment recommendations.

![Python](https://img.shields.io/badge/python-v3.12.3-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28.1-red.svg)
![Docker](https://img.shields.io/badge/docker-ready-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- **Real-time Prediction**: Advanced machine learning model for heart disease risk assessment
- **Interactive Interface**: User-friendly Streamlit web application
- **Treatment Recommendations**: Comprehensive medical guidance for high-risk patients
- **Docker Support**: Easy deployment with containerization
- **Responsive Design**: Modern, mobile-friendly UI
- **Error Handling**: Robust fallback mechanisms and demo mode

## 🚀 Quick Start

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/ruhul-cse-duet/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   Open your browser and navigate to: `http://localhost:8501`

### Local Development

1. **Prerequisites**
   - Python 3.12.3
   - pip package manager

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📊 Dataset

The application uses the **CVD_2021_BRFSS** dataset which includes:

- **308,836+ records** of health survey data
- **19 features** including demographics, lifestyle, and health conditions
- **Binary target**: Heart Disease (Yes/No)

### Key Features:
- General Health Status
- Medical History (Cancer, Diabetes, Depression, etc.)
- Lifestyle Factors (Exercise, Smoking, Diet)
- Physical Measurements (Height, Weight, BMI)
- Demographics (Age, Sex)

## 🤖 Machine Learning Model

- **Algorithm**: LightGBM (Light Gradient Boosting Machine)
- **Model File**: `models/best_lgb.pkl`
- **Features**: 18 input features for prediction
- **Output**: Binary classification (High Risk / Low Risk)

## 🏥 Treatment Recommendations

For patients identified as high-risk, the system provides:

### Immediate Actions
- Cardiology consultation
- Diagnostic tests (EKG, stress test)
- Vital signs monitoring

### Lifestyle Changes
- Heart-healthy diet plans
- Exercise recommendations
- Smoking cessation support
- Stress management techniques

### Dietary Guidelines
- Mediterranean/DASH diet principles
- Nutritional recommendations
- Portion control guidance

### Monitoring Schedule
- Regular health checkups
- Vital signs tracking
- Progress monitoring

## 🐳 Docker Deployment

### Build Custom Image
```bash
docker build -t heart-disease-app .
```

### Run Container
```bash
docker run -p 8501:8501 heart-disease-app
```

### Docker Compose (Production)
```bash
docker-compose -f docker-compose.yml up -d
```

## 🔧 Configuration

### Environment Variables
- `PYTHONPATH`: Application path
- `PYTHONUNBUFFERED`: Python output buffering

### Port Configuration
- Default: `8501`
- Customizable via Docker port mapping

## 📁 Project Structure

```
heart-disease-prediction/
├── app.py                      # Main Streamlit application
├── models/
│   └── best_lgb.pkl           # Trained LightGBM model
├── CVD_2021_BRFSS.csv         # Dataset
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose setup
├── .github/
│   └── workflows/
│       ├── ci.yml            # CI/CD pipeline
│       └── docker-build.yml  # Docker build automation
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation
```

## 🚀 GitHub Actions

Automated workflows include:

- **Continuous Integration**: Code quality checks, testing
- **Docker Build**: Multi-platform image builds
- **Security Scanning**: Vulnerability assessment
- **Automated Deployment**: Container registry publishing

## 📱 User Interface

### Main Features
- **Patient Information Form**: Comprehensive health data input
- **Real-time Prediction**: Instant risk assessment
- **Treatment Dashboard**: Detailed medical recommendations
- **Statistics Panel**: Dataset insights and model information

### Design Elements
- Modern, responsive design
- Intuitive navigation
- Color-coded risk indicators
- Mobile-friendly interface

## ⚠️ Disclaimer

**IMPORTANT**: This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical decisions.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **BRFSS Dataset**: Behavioral Risk Factor Surveillance System
- **Streamlit**: For the amazing web framework
- **LightGBM**: For the machine learning capabilities
- **Docker**: For containerization support

## 📞 Support
[Ruhul Amin](www.linkedin.com/in/ruhul-duet-cse)

For support, Email: ruhul.cse.duet@gmail.com

Or create an issue in the GitHub repository.

---

**Made with ❤️ for better healthcare predictions**

