# 🏗️ Code Structure Documentation

This document explains the modular architecture of the Heart Disease Prediction System.

## 📁 Project Structure

```
Heart Disease Prediction Streamlit/
├── 🎯 Main Application
│   ├── app.py                      # Main Streamlit application
│   ├── run.py                      # Application launcher script
│   └── setup.py                    # Package configuration
│
├── 🏥 Treatment Module
│   ├── Treatment/
│   │   ├── __init__.py            # Package initialization
│   │   └── treatment.py           # Treatment recommendations & plan generation
│   
├── 📊 Data & Models
│   ├── dataset/
│   │   └── CVD_2021_BRFSS.csv     # Health survey dataset
│   └── models/
│       └── best_lgb.pkl           # Trained LightGBM model
│
├── 🐳 Docker & Deployment
│   ├── Dockerfile                 # Container configuration
│   ├── docker-compose.yml         # Multi-service orchestration
│   ├── .dockerignore             # Docker build optimization
│   └── streamlit_config.toml     # Streamlit settings
│
├── 🔧 Configuration
│   ├── requirements.txt           # Python dependencies
│   └── .gitignore                # Git ignore rules
│
├── 🤖 CI/CD
│   └── .github/
│       └── workflows/
│           ├── ci.yml            # Continuous Integration
│           └── docker-build.yml  # Docker build automation
│
└── 📚 Documentation
    ├── README.md                 # Main project documentation
    ├── DEPLOYMENT.md             # Deployment guide
    ├── GITHUB_SETUP.md          # GitHub configuration guide
    ├── PROJECT_SUMMARY.md       # Project overview
    └── CODE_STRUCTURE.md        # This file
```

## 🧩 Module Architecture

### 1. **Main Application (`app.py`)**

**Purpose**: Core Streamlit application with UI and prediction logic

**Key Functions**:
- `load_model()`: Load and cache the ML model
- `load_sample_data()`: Load and cache dataset samples
- `preprocess_input()`: Data preprocessing for model input
- `main()`: Main application entry point

**Imports**:
```python
from treatment import get_treatment_recommendations, generate_treatment_plan_pdf
```

### 2. **Treatment Module (`Treatment/treatment.py`)**

**Purpose**: Comprehensive medical treatment recommendations and plan generation

**Key Functions**:
- `get_treatment_recommendations()`: Returns structured treatment directory
- `generate_treatment_plan_pdf()`: Creates downloadable treatment plans

**Structure**:
```python
treatment_directory = {
    "emergency": {...},           # Immediate actions
    "diagnostic_tests": {...},    # Medical tests and assessments  
    "medications": {...},         # Cardiovascular medications
    "lifestyle_interventions": {...}, # Physical activity, nutrition
    "monitoring_schedule": {...}, # Ongoing monitoring protocols
    "psychological_support": {...}, # Mental health support
    "emergency_planning": {...}   # Emergency action plans
}
```

### 3. **Package Initialization (`Treatment/__init__.py`)**

**Purpose**: Makes Treatment directory a proper Python package

**Exports**:
- `get_treatment_recommendations`
- `generate_treatment_plan_pdf`

## 🔄 Data Flow

```
1. Patient Input (Streamlit UI)
   ↓
2. Data Preprocessing (app.py)
   ↓
3. ML Model Prediction (app.py)
   ↓
4. Treatment Recommendations (Treatment/treatment.py)
   ↓
5. UI Display & Download (app.py)
```

## 🎯 Benefits of This Structure

### **1. Separation of Concerns**
- **UI Logic**: Handled in `app.py`
- **Medical Logic**: Isolated in `Treatment/` module
- **Configuration**: Separate files for different aspects

### **2. Maintainability**
- **Modular Design**: Easy to update treatment protocols
- **Clear Dependencies**: Explicit imports and structure
- **Documentation**: Each module has clear purpose

### **3. Scalability**
- **Easy Extension**: Add new treatment categories
- **Plugin Architecture**: New modules can be added
- **Testing**: Modules can be tested independently

### **4. Professional Standards**
- **Medical Accuracy**: Treatment protocols in dedicated module
- **Code Quality**: Clean imports and structure
- **Documentation**: Comprehensive guides and comments

## 🛠️ Development Guidelines

### **Adding New Treatment Categories**

1. **Update `treatment.py`**:
```python
# Add new category to treatment_directory
"new_category": {
    "priority": "HIGH",
    "timeframe": "As needed",
    "interventions": [...]
}
```

2. **Update UI in `app.py`**:
```python
# Add new tab or section for the category
with tab_new:
    # Display new category information
```

### **Adding New Functions**

1. **Create in appropriate module**:
```python
# In Treatment/treatment.py
def new_treatment_function():
    """New treatment-related functionality"""
    pass
```

2. **Export in `__init__.py`**:
```python
from .treatment import get_treatment_recommendations, generate_treatment_plan_pdf, new_treatment_function
__all__ = ['get_treatment_recommendations', 'generate_treatment_plan_pdf', 'new_treatment_function']
```

3. **Import in `app.py`**:
```python
from treatment import get_treatment_recommendations, generate_treatment_plan_pdf, new_treatment_function
```

### **Testing Structure**

```python
# Test the treatment module
import sys
sys.path.append('Treatment')
from treatment import get_treatment_recommendations

# Test function
treatment_data = get_treatment_recommendations()
assert isinstance(treatment_data, dict)
assert 'emergency' in treatment_data
```

## 🔍 Import Resolution

### **Development Environment**
```python
# app.py uses sys.path modification for development
sys.path.append(os.path.join(os.path.dirname(__file__), 'Treatment'))
from treatment import get_treatment_recommendations, generate_treatment_plan_pdf
```

### **Docker Environment**
```dockerfile
# Dockerfile sets PYTHONPATH for container
ENV PYTHONPATH="${PYTHONPATH}:/app/Treatment"
```

### **Error Handling**
```python
# Graceful fallback if module not found
try:
    from treatment import get_treatment_recommendations, generate_treatment_plan_pdf
except ImportError:
    # Fallback implementations
    def get_treatment_recommendations():
        return {"error": "Treatment module not found"}
```

## 🎯 Best Practices

### **1. Module Design**
- ✅ Single responsibility per module
- ✅ Clear function naming
- ✅ Comprehensive documentation
- ✅ Error handling

### **2. Import Strategy**
- ✅ Explicit imports in `__init__.py`
- ✅ Fallback mechanisms for missing modules
- ✅ Path configuration for different environments

### **3. Data Structure**
- ✅ Consistent dictionary structure
- ✅ Clear hierarchical organization
- ✅ Standardized field names
- ✅ Comprehensive information

### **4. Documentation**
- ✅ Function docstrings
- ✅ Module-level documentation
- ✅ Structure explanation
- ✅ Usage examples

---

## 🚀 Getting Started

### **For Developers**
1. Read this structure document
2. Examine `Treatment/treatment.py` for medical logic
3. Study `app.py` for UI integration
4. Review import patterns and error handling

### **For Medical Professionals**
1. Focus on `Treatment/treatment.py` for medical accuracy
2. Review treatment categories and recommendations
3. Validate medical protocols and terminology
4. Suggest improvements for clinical accuracy

### **For DevOps**
1. Understand Docker configuration
2. Review CI/CD pipelines
3. Check environment variable handling
4. Validate deployment configurations

**The modular structure ensures professional, maintainable, and scalable healthcare software! 🏥**
