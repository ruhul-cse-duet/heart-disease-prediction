# 🚀 Deployment Guide

This guide provides comprehensive instructions for deploying the Heart Disease Prediction System.

## 📋 Prerequisites

- Python 3.12.3
- Docker (for containerized deployment)
- Git (for version control)
- 4GB+ RAM recommended
- 2GB+ disk space

## 🐳 Docker Deployment (Recommended)

### 1. Quick Start with Docker Compose

```bash
# Clone the repository
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction

# Start the application
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

### 2. Manual Docker Build

```bash
# Build the image
docker build -t heart-disease-app:latest .

# Run the container
docker run -d \
  --name heart-disease-app \
  -p 8501:8501 \
  -v $(pwd)/models:/app/models:ro \
  -v $(pwd)/CVD_2021_BRFSS.csv:/app/CVD_2021_BRFSS.csv:ro \
  heart-disease-app:latest

# Check logs
docker logs heart-disease-app

# Stop the container
docker stop heart-disease-app
docker rm heart-disease-app
```

## 💻 Local Development Setup

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application

```bash
# Using the launcher script
python run.py

# Or directly with Streamlit
streamlit run app.py

# Or with custom configuration
streamlit run app.py --server.port 8502 --server.address 0.0.0.0
```

## ☁️ Cloud Deployment

### AWS EC2 Deployment

1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Instance type: t3.medium or larger
   - Security group: Allow inbound traffic on port 8501

2. **Setup on EC2**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Docker
   sudo apt install docker.io docker-compose -y
   sudo systemctl start docker
   sudo systemctl enable docker
   sudo usermod -aG docker $USER
   
   # Clone and deploy
   git clone https://github.com/yourusername/heart-disease-prediction.git
   cd heart-disease-prediction
   docker-compose up -d
   ```

### Google Cloud Platform

1. **Cloud Run Deployment**
   ```bash
   # Build and push to Container Registry
   gcloud builds submit --tag gcr.io/PROJECT_ID/heart-disease-app
   
   # Deploy to Cloud Run
   gcloud run deploy heart-disease-app \
     --image gcr.io/PROJECT_ID/heart-disease-app \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --port 8501
   ```

### Azure Container Instances

```bash
# Create resource group
az group create --name heart-disease-rg --location eastus

# Deploy container
az container create \
  --resource-group heart-disease-rg \
  --name heart-disease-app \
  --image your-registry/heart-disease-app:latest \
  --dns-name-label heart-disease-app \
  --ports 8501
```

### Heroku Deployment

1. **Prepare for Heroku**
   ```bash
   # Install Heroku CLI
   # Create Procfile
   echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   
   # Create Heroku app
   heroku create heart-disease-prediction-app
   
   # Deploy
   git push heroku main
   ```

## 🔧 Configuration Options

### Environment Variables

```bash
# Application settings
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true

# Python settings
export PYTHONPATH=/app
export PYTHONUNBUFFERED=1

# Model settings
export MODEL_PATH=models/best_lgb.pkl
export DATA_PATH=CVD_2021_BRFSS.csv
```

### Custom Configuration

Create `.streamlit/config.toml`:
```toml
[server]
port = 8501
address = "0.0.0.0"
headless = true
enableCORS = false

[theme]
primaryColor = "#e74c3c"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8f9fa"
textColor = "#262730"
```

## 🔒 Security Considerations

### 1. HTTPS Configuration

```nginx
# Nginx reverse proxy configuration
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    
    location / {
        proxy_pass http://localhost:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 2. Authentication (Optional)

For production deployments requiring authentication, consider:
- OAuth integration
- LDAP authentication
- Basic authentication with reverse proxy

### 3. Data Security

- Use environment variables for sensitive configuration
- Implement data encryption at rest
- Regular security audits
- Access logging and monitoring

## 📊 Monitoring and Logging

### 1. Application Monitoring

```bash
# Check application health
curl http://localhost:8501/_stcore/health

# View application metrics
docker stats heart-disease-app

# Check resource usage
htop
```

### 2. Log Management

```bash
# View Docker logs
docker logs -f heart-disease-app

# Structured logging with timestamps
docker logs --timestamps heart-disease-app

# Export logs
docker logs heart-disease-app > app.log 2>&1
```

### 3. Health Checks

The application includes built-in health checks:
- Docker health check endpoint
- Streamlit health monitoring
- Resource usage monitoring

## 🔄 Updates and Maintenance

### 1. Update Application

```bash
# Pull latest changes
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### 2. Backup Data

```bash
# Backup models and data
tar -czf backup-$(date +%Y%m%d).tar.gz models/ *.csv

# Backup configuration
cp -r .streamlit/ config-backup/
```

### 3. Database Maintenance

```bash
# Clean up Docker images
docker system prune -f

# Update dependencies
pip install --upgrade -r requirements.txt
```

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port 8501
   netstat -tulpn | grep 8501
   # Kill the process
   sudo kill -9 <PID>
   ```

2. **Model Loading Error**
   - Check model file integrity
   - Verify file permissions
   - Ensure correct Python version compatibility

3. **Memory Issues**
   - Increase Docker memory limits
   - Monitor memory usage
   - Consider data sampling for large datasets

4. **Permission Errors**
   ```bash
   # Fix file permissions
   sudo chown -R $USER:$USER .
   chmod +x run.py
   ```

### Performance Optimization

1. **Resource Limits**
   ```yaml
   # docker-compose.yml
   services:
     heart-disease-app:
       deploy:
         resources:
           limits:
             memory: 2G
             cpus: "1.0"
   ```

2. **Caching Configuration**
   - Enable Streamlit caching
   - Use CDN for static assets
   - Implement Redis for session management

## 📞 Support

For deployment issues:
1. Check the troubleshooting section
2. Review application logs
3. Create an issue on GitHub
4. Contact support team

---

**Happy Deploying! 🚀**

