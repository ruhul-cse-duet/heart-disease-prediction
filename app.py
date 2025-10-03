import streamlit as st
import pandas as pd
import pickle
import numpy as np
from datetime import datetime
import os
import warnings
import sys
warnings.filterwarnings('ignore')


# Add Treatment directory to path-----------------------------------------------
sys.path.append(os.path.join(os.path.dirname(__file__), 'Treatment'))

# Import treatment module
try:
    from treatment import get_treatment_recommendations, generate_treatment_plan_pdf
except ImportError:
    # Fallback if module not found
    def get_treatment_recommendations():
        return {"error": "Treatment module not found"}
    
    def generate_treatment_plan_pdf(patient_data, treatment_dir):
        return "Treatment module not available - cannot generate plan"

# Add Data preprocess directory to path-----------------------------------------------
sys.path.append(os.path.join(os.path.dirname(__file__), 'Data preprocess'))
# Import preprocess module function
try:
    from preprocess_scaler import preprocess_input_with_scaling

except ImportError:
    # Fallback if module not found
    def preprocess_input_with_scaling(user_input, sample_df):
        return "preprocess_input_with_scaling module not available"

# Page configuration------------------------------------------------
st.set_page_config(
    page_title="Heart Disease Prediction System",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling--------------------------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# CSS file imported.............
local_css("styles/style.css")
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #A0A3A2; /* light grey-blue */
}

[data-testid="stHeader"] {
    background-color: #DADCE6; /* transparent header */
}

[data-testid="stSidebar"] {
    background-color: #BAA29E; /* white sidebar */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Load model function with error handling for LightGBM
@st.cache_resource
def load_model():
    """
    Load LightGBM model with proper error handling
    """
    try:
        # Try different methods to load the corrupted pickle file
        loading_methods = [
            # Method 1: Standard pickle
            lambda: pickle.load(open('models/best_lgb.pkl', 'rb')),
            # Method 2: With latin1 encoding 
            lambda: pickle.load(open('models/best_lgb.pkl', 'rb'), encoding='latin1'),
            # Method 3: With bytes encoding
            lambda: pickle.load(open('models/best_lgb.pkl', 'rb'), encoding='bytes'),
            # Method 4: Try joblib
            lambda: __import__('joblib').load('models/best_lgb.pkl'),
        ]
        
        for i, method in enumerate(loading_methods, 1):
            try:
                model = method()
                #st.success(f"✅ Model loaded successfully using method {i}")
                return model, None
            except Exception as method_error:
                if i == len(loading_methods):
                    # Last method failed, return error
                    break
                continue
        
        return None, "All model loading methods failed - pickle file may be corrupted"
        
    except Exception as e:
        return None, f"Model loading error: {str(e)}"



#---------------------Main Function------------------------------------------------------
def main():
    # Header
    st.markdown(
        '<h2 class="title-text">❤️ Heart Disease Prediction System</h2>',
        unsafe_allow_html=True)

    # Load model, scaler and data
    model, model_error = load_model()

    if model is None:
        st.warning(f"⚠️ Model loading error: {model_error}")
        st.info("The app will continue with a demo mode using sample predictions.")
    
#--------- Sidebar for user input---------------------------------------------------------------------
    st.sidebar.markdown('<p class="sub-header">📝 Patient Information</p>', unsafe_allow_html=True)

    # Create input fields based on data types
    user_input = {}
    
    # General Health
    user_input['General_Health'] = st.sidebar.selectbox(
        'General Health',
        ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']
    )
    
    # Last Checkup
    user_input['Checkup'] = st.sidebar.selectbox(
        'Last Medical Checkup',
        ['Within the past year', 'Within the past 2 years', 
         'Within the past 5 years', '5 or more years ago', 'Never']
    )
    
    # Exercise
    user_input['Exercise'] = st.sidebar.selectbox(
        'Do you exercise regularly?',
        ['Yes', 'No']
    )
    
    # Health Conditions
    st.sidebar.markdown("**Medical History**")
    user_input['Skin_Cancer'] = st.sidebar.selectbox('Skin Cancer', ['No', 'Yes'])
    user_input['Other_Cancer'] = st.sidebar.selectbox('Other Cancer', ['No', 'Yes'])
    user_input['Depression'] = st.sidebar.selectbox('Depression', ['No', 'Yes'])
    user_input['Diabetes'] = st.sidebar.selectbox('Diabetes', ['No', 'Yes'])
    user_input['Arthritis'] = st.sidebar.selectbox('Arthritis', ['No', 'Yes'])
    
    # Demographics
    st.sidebar.markdown("**Demographics**")
    user_input['Sex'] = st.sidebar.selectbox('Sex', ['Male', 'Female'])
    user_input['Age_Category'] = st.sidebar.selectbox(
        'Age Category',
        ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49',
         '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']
    )
    
    # Physical Measurements
    st.sidebar.markdown("**Physical Measurements**")
    user_input['Height_(cm)'] = st.sidebar.number_input('Height (cm)', min_value=100, max_value=250, value=170)
    user_input['Weight_(kg)'] = st.sidebar.number_input('Weight (kg)', min_value=30, max_value=300, value=70)
    user_input['BMI'] = user_input['Weight_(kg)'] / ((user_input['Height_(cm)'] / 100) ** 2)
    
    # Lifestyle
    st.sidebar.markdown("**Lifestyle Factors**")
    user_input['Smoking_History'] = st.sidebar.selectbox('Smoking History', ['No', 'Yes'])
    user_input['Alcohol_Consumption'] = st.sidebar.slider('Alcohol Consumption (drinks per week)', 0, 100, 0)
    user_input['Fruit_Consumption'] = st.sidebar.slider('Fruit Consumption (servings per week)', 0, 120, 10)
    user_input['Green_Vegetables_Consumption'] = st.sidebar.slider('Green Vegetables (servings per week)', 0, 120, 8)
    user_input['FriedPotato_Consumption'] = st.sidebar.slider('Fried Potato Consumption (servings per week)', 0, 120, 2)


#---------------------------------- Main content area-----------------------------------------
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown('<p class="sub-header">📊 Patient Data Summary</p>', unsafe_allow_html=True)
        
        # Display user input in a nice format
        input_df = pd.DataFrame([user_input])
        st.dataframe(input_df, width='stretch')
        
#------------ Prediction button--------------------------------------------------------
        st.markdown('<div class="center-button">', unsafe_allow_html=True)
        if st.button('🔍 Predict Heart Disease Risk', type='primary', width=250 ):
            st.markdown('</div>', unsafe_allow_html=True)
            # Make prediction
            try:
                if model is not None:
# -----------------Use enhanced preprocessing with scaling for LightGBM--------------------------------
                    input_df= preprocess_input_with_scaling(user_input)
                    
                    if input_df is not None:
                        # Make prediction with LightGBM model
                        prediction = model.predict(input_df)[0]
                        prediction_proba = model.predict_proba(input_df)[0]
                        
                        # Debug information
                        with st.expander("🔍 Debug Information"):
                            st.write("**Input shape:**", input_df.shape)
                            st.write("**Feature names:**", list(input_df.columns))
                            st.write("**Scaled features (first 5):**", input_df.iloc[0, :5].tolist())
                            st.write("**Model type:**", type(model).__name__)
                            #st.write("**Scaler status:**", "✅ Applied" if scaler is not None else "❌ Not applied")
                    else:
                        raise ValueError("Failed to preprocess input data")
                    
                    # Display prediction
                    if prediction == 1 or prediction == 'Yes':
                        st.markdown(f'''
                        <div class="prediction-box positive-prediction">
                            ⚠️ HIGH RISK: Heart Disease Detected<br>
                            Risk Probability: {prediction_proba[1]:.2%}
                        </div>
                        ''', unsafe_allow_html=True)
                        show_treatment = True
                    else:
                        st.markdown(f'''
                        <div class="prediction-box negative-prediction">
                            ✅ LOW RISK: No Heart Disease Detected<br>
                            Risk Probability: {prediction_proba[0]:.2%}
                        </div>
                        ''', unsafe_allow_html=True)
                        show_treatment = False
                        
                else:
                    # Demo mode - simple rule-based prediction
                    risk_factors = 0
                    if user_input['General_Health'] in ['Poor', 'Fair']:
                        risk_factors += 2
                    if user_input['Exercise'] == 'No':
                        risk_factors += 1
                    if user_input['Smoking_History'] == 'Yes':
                        risk_factors += 2
                    if user_input['BMI'] > 30:
                        risk_factors += 1
                    if user_input['Age_Category'] in ['70-74', '75-79', '80+']:
                        risk_factors += 1
                    
                    if risk_factors >= 3:
                        st.markdown('''
                        <div class="prediction-box positive-prediction">
                            ⚠️ HIGH RISK: Potential Heart Disease Risk<br>
                            (Demo Mode - Consult a healthcare professional)
                        </div>
                        ''', unsafe_allow_html=True)
                        show_treatment = True
                    else:
                        st.markdown('''
                        <div class="prediction-box negative-prediction">
                            ✅ LOW RISK: Lower Heart Disease Risk<br>
                            (Demo Mode - Continue healthy lifestyle)
                        </div>
                        ''', unsafe_allow_html=True)
                        show_treatment = False
                
                # Show treatment recommendations if high risk..............................
                if show_treatment:
                    st.markdown('<p class="sub-header">🏥 Comprehensive Treatment Directory</p>', unsafe_allow_html=True)
                    
                    treatment_dir = get_treatment_recommendations()
                    
                    # Create tabs for different treatment categories
                    tab1, tab2, tab3, tab4, tab5 = st.tabs([
                        "🚨 Emergency", 
                        "🔬 Diagnostics", 
                        "💊 Medications", 
                        "🏃‍♂️ Lifestyle", 
                        "📊 Monitoring"
                    ])
                    
                    with tab1:
                        st.markdown('<div class="treatment-box">', unsafe_allow_html=True)
                        emergency = treatment_dir['emergency']
                        st.markdown(f"**Priority:** {emergency['priority']} | **Timeframe:** {emergency['timeframe']}")
                        
                        st.markdown("#### Emergency Actions")
                        for action in emergency['actions']:
                            st.markdown(f"""
                            **{action['action']}**
                            - *Condition:* {action['condition']}
                            - *Urgency:* {action['urgency']}
                            """)
                        
                        # Emergency Planning
                        emergency_plan = treatment_dir['emergency_planning']
                        st.markdown("#### 🚨 Emergency Action Plan")
                        
                        col3, col4 = st.columns(2)
                        with col3:
                            st.markdown("**⚠️ Warning Signs:**")
                            for sign in emergency_plan['action_plan']['warning_signs']:
                                st.markdown(f"• {sign}")
                        
                        with col4:
                            st.markdown("**📞 Immediate Response:**")
                            for response in emergency_plan['action_plan']['immediate_response']:
                                st.markdown(f"• {response}")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with tab2:
                        st.markdown('<div class="treatment-box">', unsafe_allow_html=True)
                        diagnostics = treatment_dir['diagnostic_tests']
                        st.markdown(f"**Priority:** {diagnostics['priority']} | **Timeframe:** {diagnostics['timeframe']}")
                        
                        st.markdown("#### 🫀 Cardiac Assessment Tests")
                        for test in diagnostics['categories']['cardiac_assessment']:
                            st.markdown(f"""
                            **{test['test']}**
                            - *Purpose:* {test['purpose']}
                            - *Frequency:* {test['frequency']}
                            """)
                        
                        st.markdown("#### 🩸 Blood Work")
                        for test in diagnostics['categories']['blood_work']:
                            st.markdown(f"""
                            **{test['test']}**
                            - *Purpose:* {test['purpose']}
                            - *Frequency:* {test['frequency']}
                            """)
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with tab3:
                        st.markdown('<div class="treatment-box">', unsafe_allow_html=True)
                        medications = treatment_dir['medications']
                        st.markdown(f"**Priority:** {medications['priority']} | **Timeframe:** {medications['timeframe']}")
                        
                        st.markdown("#### 💊 Cardiovascular Medications")
                        for med in medications['categories']['cardiovascular']:
                            st.markdown(f"""
                            **{med['type']}**
                            - *Purpose:* {med['purpose']}
                            - *Examples:* {med['examples']}
                            - *Note:* {med['note']}
                            """)
                        
                        st.markdown("#### 🛡️ Preventive Medications")
                        for med in medications['categories']['preventive']:
                            st.markdown(f"""
                            **{med['type']}**
                            - *Purpose:* {med['purpose']}
                            - *Dosage:* {med['dosage']}
                            - *Note:* {med['note']}
                            """)
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with tab4:
                        st.markdown('<div class="treatment-box">', unsafe_allow_html=True)
                        lifestyle = treatment_dir['lifestyle_interventions']
                        st.markdown(f"**Priority:** {lifestyle['priority']} | **Timeframe:** {lifestyle['timeframe']}")

                        st.markdown("#### 🏃‍♂️ Physical Activity Program")
                        for activity in lifestyle['categories']['physical_activity']:
                            lines = [
                                f"**{activity.get('activity', 'Activity')}**",
                                f"- *Recommendation:* {activity.get('recommendation', 'As advised')}",
                                f"- *Examples:* {activity.get('examples', '—')}",
                            ]
                            # optional fields
                            if 'progression' in activity:
                                lines.append(f"- *Progression:* {activity['progression']}")
                            if 'benefits' in activity:
                                lines.append(f"- *Benefits:* {activity['benefits']}")
                            st.markdown("\n".join(lines))
                        
                        st.markdown("#### 🚭 Smoking Cessation")
                        for method in lifestyle['categories']['smoking_cessation']:
                            st.markdown(f"""
                            **{method['method']}**
                            - *Options:* {method['options']}
                            """)
                            if 'success_rate' in method:
                                st.markdown(f"- *Success Rate:* {method['success_rate']}")
                            if 'contact' in method:
                                st.markdown(f"- *Contact:* {method['contact']}")
                        
                        # Nutrition
                        nutrition = treatment_dir['nutrition_therapy']
                        st.markdown("#### 🥗 Nutrition Therapy")
                        
                        col3, col4 = st.columns(2)
                        with col3:
                            st.markdown("**Mediterranean Diet:**")
                            med_diet = nutrition['dietary_approaches']['mediterranean_diet']
                            st.markdown(f"*{med_diet['description']}*")
                            st.markdown(f"**Benefits:** {med_diet['benefits']}")
                            
                        with col4:
                            st.markdown("**DASH Diet:**")
                            dash_diet = nutrition['dietary_approaches']['dash_diet']
                            st.markdown(f"*{dash_diet['description']}*")
                            st.markdown(f"**Benefits:** {dash_diet['benefits']}")
                        
                        st.markdown("**🔺 Foods to Increase:**")
                        for item in nutrition['specific_recommendations']['increase']:
                            st.markdown(f"• **{item['food']}** - {item['frequency']} ({item['benefit']})")
                        
                        st.markdown("**🔻 Foods to Limit:**")
                        for item in nutrition['specific_recommendations']['limit']:
                            st.markdown(f"• **{item['food']}** - {item['limit']} ({item['reason']})")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with tab5:
                        st.markdown('<div class="treatment-box">', unsafe_allow_html=True)
                        monitoring = treatment_dir['monitoring_schedule']
                        st.markdown(f"**Priority:** {monitoring['priority']} | **Timeframe:** {monitoring['timeframe']}")
                        
                        st.markdown("#### 📊 Vital Signs Monitoring")
                        for vital in monitoring['vital_signs']:
                            st.markdown(f"""
                            **{vital['parameter']}**
                            - *Frequency:* {vital['frequency']}
                            - *Target:* {vital['target']}
                            """)
                            if 'device' in vital:
                                st.markdown(f"- *Device:* {vital['device']}")
                            if 'note' in vital:
                                st.markdown(f"- *Note:* {vital['note']}")
                        
                        st.markdown("#### 🧪 Laboratory Tests")
                        for test in monitoring['laboratory_tests']:
                            st.markdown(f"""
                            **{test['test']}**
                            - *Frequency:* {test['frequency']}
                            - *Targets:* {test['targets'] if 'targets' in test else test['target']}
                            """)
                        
                        # Psychological Support
                        psych = treatment_dir['psychological_support']
                        st.markdown("#### 🧠 Psychological Support")
                        for intervention in psych['interventions']:
                            st.markdown(f"""
                            **{intervention['type']}**
                            """)
                            if 'techniques' in intervention:
                                st.markdown(f"- *Techniques:* {', '.join(intervention['techniques'])}")
                            if 'recommendation' in intervention:
                                st.markdown(f"- *Recommendation:* {intervention['recommendation']}")
                            if 'apps' in intervention:
                                st.markdown(f"- *Apps:* {intervention['apps']}")
                            if 'purpose' in intervention:
                                st.markdown(f"- *Purpose:* {intervention['purpose']}")
                            if 'options' in intervention:
                                st.markdown(f"- *Options:* {intervention['options']}")
                            if 'benefits' in intervention:
                                st.markdown(f'*benefits:* {intervention['benefits']}' )
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Critical warning
                    st.markdown("⚠️ **CRITICAL DISCLAIMER**: This treatment directory is for educational purposes only. All medical decisions must be made in consultation with qualified healthcare professionals. Do not start, stop, or modify any treatments without medical supervision.")


#----------------------------# Download treatment plan--------------------------------------
                    st.markdown("---")
                    st.markdown("### 📄 Download Personal Treatment Plan")
                    
                    if st.button("📥 Generate Downloadable Treatment Plan", type="secondary", width='stretch'):
                        try:
                            treatment_plan_text = generate_treatment_plan_pdf(user_input, treatment_dir)
                            
                            # Create download button
                            st.download_button(
                                label="📁 Download Treatment Plan (.txt)",
                                data=treatment_plan_text,
                                file_name=f"heart_disease_treatment_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                                mime="text/plain",
                                width='stretch'
                            )
                            
                            st.success("✅ Treatment plan generated successfully! Click the download button above to save it.")
                            
                            # Show preview of first few lines
                            with st.expander("👀 Preview Treatment Plan"):
                                preview_lines = treatment_plan_text.split('\n')[:20]
                                st.text('\n'.join(preview_lines) + '\n...(continue in downloaded file)')
                                
                        except Exception as e:
                            st.error(f"Error generating treatment plan: {e}")
                
            except Exception as e:
                st.error(f"Error making prediction: {e}")

#-----------------About Section---------------------------------------------------
    with col2:
        st.markdown('<p class="sub-header">ℹ️ About</p>', unsafe_allow_html=True)
        st.markdown("""<div class="sub-header-about">
                <p>This Heart Disease Prediction System uses machine learning to 
                assess the risk of heart disease based on various health and lifestyle factors.</p>
                <h4>Features</h4>
                <ol>
                    <li>Comprehensive health assessment</li>
                    <li>Real-time risk prediction</li>
                    <li>Treatment recommendations</li>
                    <li>Lifestyle guidance</li>
                </ol>
                <p><strong>Disclaimer:</strong> This tool is for educational purposes only and 
                should not replace professional medical advice.</p>
        </div>""", unsafe_allow_html=True)
        
        # Model information
        if model is not None:
            st.success("✅ AI Model Loaded Successfully")
        else:
            st.warning("⚠️ Running in Demo Mode")


        df = pd.read_csv("./dataset/CVD_2021_BRFSS.csv")
        # Statistics
        st.markdown("##### 📊 Dataset Statistics")
        total_records = len(df)
        heart_disease_cases = len(df[df['Heart_Disease'] == 'Yes'])
        st.metric("Total Records", f"{total_records:,}")
        st.metric("Heart Disease Cases", f"{heart_disease_cases:,}")
        st.metric("Risk Rate", f"{(heart_disease_cases/total_records)*100:.1f}%")

if __name__ == "__main__":
    main()
