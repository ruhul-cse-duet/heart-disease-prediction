def get_treatment_recommendations():
    """
    Returns a comprehensive treatment directory organized by category,
    priority, and specific medical conditions.
    """
    treatment_directory = {
        "emergency": {
            "priority": "IMMEDIATE",
            "timeframe": "Within 24 hours",
            "actions": [
                {
                    "action": "Emergency Room Visit",
                    "condition": "Chest pain, shortness of breath, or severe symptoms",
                    "urgency": "Call 911 immediately"
                },
                {
                    "action": "Cardiology Consultation",
                    "condition": "High-risk prediction result",
                    "urgency": "Schedule within 24-48 hours"
                }
            ]
        },
        
        "diagnostic_tests": {
            "priority": "HIGH",
            "timeframe": "Within 1-2 weeks",
            "categories": {
                "cardiac_assessment": [
                    {
                        "test": "Electrocardiogram (EKG/ECG)",
                        "purpose": "Detect heart rhythm abnormalities",
                        "frequency": "Immediate, then as needed"
                    },
                    {
                        "test": "Echocardiogram",
                        "purpose": "Assess heart structure and function",
                        "frequency": "Baseline, then annually"
                    },
                    {
                        "test": "Stress Test",
                        "purpose": "Evaluate heart function under stress",
                        "frequency": "As recommended by cardiologist"
                    }
                ],
                "blood_work": [
                    {
                        "test": "Lipid Panel",
                        "purpose": "Check cholesterol and triglyceride levels",
                        "frequency": "Every 3-6 months"
                    },
                    {
                        "test": "HbA1c",
                        "purpose": "Monitor blood sugar control",
                        "frequency": "Every 3 months if diabetic"
                    },
                    {
                        "test": "C-Reactive Protein (CRP)",
                        "purpose": "Assess inflammation levels",
                        "frequency": "Annually or as needed"
                    }
                ]
            }
        },
        
        "medications": {
            "priority": "HIGH",
            "timeframe": "As prescribed by physician",
            "categories": {
                "cardiovascular": [
                    {
                        "type": "ACE Inhibitors/ARBs",
                        "purpose": "Lower blood pressure, protect heart",
                        "examples": "Lisinopril, Losartan",
                        "note": "Prescription required"
                    },
                    {
                        "type": "Statins",
                        "purpose": "Lower cholesterol",
                        "examples": "Atorvastatin, Simvastatin",
                        "note": "Monitor liver function"
                    },
                    {
                        "type": "Beta-blockers",
                        "purpose": "Control heart rate and blood pressure",
                        "examples": "Metoprolol, Carvedilol",
                        "note": "Gradual dosage adjustment"
                    }
                ],
                "preventive": [
                    {
                        "type": "Aspirin",
                        "purpose": "Blood clot prevention",
                        "dosage": "Low-dose (81mg) daily",
                        "note": "Consult doctor before starting"
                    }
                ]
            }
        },
        
        "lifestyle_interventions": {
            "priority": "ESSENTIAL",
            "timeframe": "Start immediately, lifelong commitment",
            "categories": {
                "physical_activity": [
                    {
                        "activity": "Aerobic Exercise",
                        "recommendation": "150 minutes moderate intensity per week",
                        "examples": "Brisk walking, swimming, cycling",
                        "progression": "Start with 10-15 minutes, gradually increase"
                    },
                    {
                        "activity": "Strength Training",
                        "recommendation": "2-3 sessions per week",
                        "examples": "Weight lifting, resistance bands, bodyweight exercises",
                        "progression": "Start with light weights, focus on form"
                    },
                    {
                        "activity": "Flexibility & Balance",
                        "recommendation": "Daily stretching, 2-3 yoga sessions weekly",
                        "examples": "Yoga, tai chi, stretching routines",
                        "benefits": "Stress reduction, improved mobility"
                    }
                ],
                "smoking_cessation": [
                    {
                        "method": "Nicotine Replacement Therapy",
                        "options": "Patches, gum, lozenges",
                        "success_rate": "Doubles quit success rate"
                    },
                    {
                        "method": "Prescription Medications",
                        "options": "Varenicline (Chantix), Bupropion (Zyban)",
                        "note": "Consult healthcare provider"
                    },
                    {
                        "method": "Behavioral Support",
                        "options": "Quitlines, support groups, counseling",
                        "contact": "1-800-QUIT-NOW"
                    }
                ]
            }
        },
        
        "nutrition_therapy": {
            "priority": "ESSENTIAL",
            "timeframe": "Immediate implementation",
            "dietary_approaches": {
                "mediterranean_diet": {
                    "description": "Proven to reduce cardiovascular risk",
                    "key_components": [
                        "High olive oil consumption",
                        "Abundant fruits and vegetables",
                        "Whole grains and legumes",
                        "Fish and seafood 2-3 times per week",
                        "Limited red meat and processed foods"
                    ],
                    "benefits": "30% reduction in cardiovascular events"
                },
                "dash_diet": {
                    "description": "Dietary Approaches to Stop Hypertension",
                    "key_components": [
                        "Low sodium (less than 2,300mg daily)",
                        "Rich in potassium, calcium, magnesium",
                        "Emphasizes fruits, vegetables, whole grains",
                        "Low-fat dairy products",
                        "Limited saturated fats and cholesterol"
                    ],
                    "benefits": "Significant blood pressure reduction"
                }
            },
            "specific_recommendations": {
                "increase": [
                    {"food": "Fatty fish", "frequency": "2-3 times per week", "benefit": "Omega-3 fatty acids"},
                    {"food": "Leafy greens", "frequency": "Daily", "benefit": "Folate, potassium, nitrates"},
                    {"food": "Berries", "frequency": "Daily", "benefit": "Antioxidants, fiber"},
                    {"food": "Nuts", "frequency": "1 oz daily", "benefit": "Healthy fats, protein, fiber"}
                ],
                "limit": [
                    {"food": "Sodium", "limit": "Less than 2,300mg daily", "reason": "Blood pressure control"},
                    {"food": "Saturated fats", "limit": "Less than 7% of calories", "reason": "Cholesterol management"},
                    {"food": "Added sugars", "limit": "Less than 25g daily", "reason": "Weight and diabetes control"},
                    {"food": "Alcohol", "limit": "1 drink/day (women), 2 drinks/day (men)", "reason": "Blood pressure and weight"}
                ]
            }
        },
        
        "monitoring_schedule": {
            "priority": "ONGOING",
            "timeframe": "Regular intervals",
            "vital_signs": [
                {
                    "parameter": "Blood Pressure",
                    "frequency": "Daily at home, weekly with healthcare provider",
                    "target": "Less than 130/80 mmHg",
                    "device": "Validated home BP monitor"
                },
                {
                    "parameter": "Weight",
                    "frequency": "Daily, same time each day",
                    "target": "BMI 18.5-24.9",
                    "note": "Sudden weight gain may indicate fluid retention"
                },
                {
                    "parameter": "Heart Rate",
                    "frequency": "Daily, especially during exercise",
                    "target": "Resting HR 60-100 bpm",
                    "device": "Heart rate monitor or fitness tracker"
                }
            ],
            "laboratory_tests": [
                {
                    "test": "Lipid Panel",
                    "frequency": "Every 3-6 months initially, then annually",
                    "targets": "LDL <100 mg/dL, HDL >40 mg/dL (men), >50 mg/dL (women)"
                },
                {
                    "test": "HbA1c",
                    "frequency": "Every 3 months if diabetic, annually if pre-diabetic",
                    "target": "<7% for most diabetics, <5.7% for non-diabetics"
                }
            ]
        },
        
        "psychological_support": {
            "priority": "IMPORTANT",
            "timeframe": "As needed",
            "interventions": [
                {
                    "type": "Stress Management",
                    "techniques": ["Meditation", "Deep breathing", "Progressive muscle relaxation"],
                    "recommendation": "20 minutes daily",
                    "apps": "Headspace, Calm, Insight Timer"
                },
                {
                    "type": "Cognitive Behavioral Therapy",
                    "purpose": "Address anxiety, depression, health behaviors",
                    "provider": "Licensed mental health professional",
                    "duration": "8-12 sessions typically"
                },
                {
                    "type": "Support Groups",
                    "options": ["Heart disease support groups", "Online communities", "Cardiac rehabilitation programs"],
                    "benefits": "Peer support, shared experiences, motivation"
                }
            ]
        },
        
        "emergency_planning": {
            "priority": "CRITICAL",
            "timeframe": "Immediate preparation",
            "action_plan": {
                "warning_signs": [
                    "Chest pain or discomfort",
                    "Shortness of breath",
                    "Pain in arms, back, neck, jaw, or stomach",
                    "Cold sweat, nausea, lightheadedness"
                ],
                "immediate_response": [
                    "Call 911 immediately",
                    "Chew aspirin if not allergic (ask 911 dispatcher)",
                    "Stop all activity and rest",
                    "Have someone stay with you"
                ],
                "preparation": [
                    "Keep emergency contacts readily available",
                    "Maintain updated medication list",
                    "Know location of nearest emergency room",
                    "Inform family members of symptoms to watch for"
                ]
            }
        }
    }
    
    return treatment_directory


def generate_treatment_plan_pdf(patient_data, treatment_dir):
    """
    Generate a personalized treatment plan text that can be downloaded
    """
    from datetime import datetime
    
    plan_text = f"""
PERSONALIZED HEART DISEASE TREATMENT PLAN
{'='*50}

PATIENT INFORMATION:
- General Health: {patient_data.get('General_Health', 'N/A')}
- Age Category: {patient_data.get('Age_Category', 'N/A')}
- BMI: {patient_data.get('BMI', 'N/A'):.1f if 'BMI' in patient_data else 'N/A'}
- Exercise: {patient_data.get('Exercise', 'N/A')}
- Smoking History: {patient_data.get('Smoking_History', 'N/A')}

EMERGENCY ACTIONS (IMMEDIATE PRIORITY)
{'='*40}
Timeframe: {treatment_dir['emergency']['timeframe']}

Emergency Actions:
"""
    
    for action in treatment_dir['emergency']['actions']:
        plan_text += f"""
- {action['action']}
  Condition: {action['condition']}
  Urgency: {action['urgency']}
"""
    
    plan_text += f"""

WARNING SIGNS TO WATCH FOR:
"""
    for sign in treatment_dir['emergency_planning']['action_plan']['warning_signs']:
        plan_text += f"• {sign}\n"
    
    plan_text += f"""

IMMEDIATE RESPONSE IF SYMPTOMS OCCUR:
"""
    for response in treatment_dir['emergency_planning']['action_plan']['immediate_response']:
        plan_text += f"• {response}\n"
    
    plan_text += f"""

DIAGNOSTIC TESTS (HIGH PRIORITY)
{'='*35}
Timeframe: {treatment_dir['diagnostic_tests']['timeframe']}

Cardiac Assessment Tests:
"""
    
    for test in treatment_dir['diagnostic_tests']['categories']['cardiac_assessment']:
        plan_text += f"""
- {test['test']}
  Purpose: {test['purpose']}
  Frequency: {test['frequency']}
"""
    
    plan_text += f"""

Blood Work Tests:
"""
    for test in treatment_dir['diagnostic_tests']['categories']['blood_work']:
        plan_text += f"""
- {test['test']}
  Purpose: {test['purpose']}
  Frequency: {test['frequency']}
"""
    
    plan_text += f"""

LIFESTYLE INTERVENTIONS (ESSENTIAL)
{'='*35}
Timeframe: {treatment_dir['lifestyle_interventions']['timeframe']}

Physical Activity Program:
"""
    
    for activity in treatment_dir['lifestyle_interventions']['categories']['physical_activity']:
        plan_text += f"""
- {activity['activity']}
  Recommendation: {activity['recommendation']}
  Examples: {activity['examples']}
  Progression: {activity['progression']}
"""
    
    plan_text += f"""

NUTRITION PLAN:
Mediterranean Diet Benefits: {treatment_dir['nutrition_therapy']['dietary_approaches']['mediterranean_diet']['benefits']}

Foods to Increase:
"""
    for item in treatment_dir['nutrition_therapy']['specific_recommendations']['increase']:
        plan_text += f"• {item['food']} - {item['frequency']} ({item['benefit']})\n"
    
    plan_text += f"""
Foods to Limit:
"""
    for item in treatment_dir['nutrition_therapy']['specific_recommendations']['limit']:
        plan_text += f"• {item['food']} - {item['limit']} ({item['reason']})\n"
    
    plan_text += f"""

MONITORING SCHEDULE (ONGOING)
{'='*30}

Vital Signs to Monitor:
"""
    for vital in treatment_dir['monitoring_schedule']['vital_signs']:
        plan_text += f"""
- {vital['parameter']}
  Frequency: {vital['frequency']}
  Target: {vital['target']}
"""
        if 'device' in vital:
            plan_text += f"  Device: {vital['device']}\n"
    
    plan_text += f"""

Laboratory Tests Schedule:
"""
    for test in treatment_dir['monitoring_schedule']['laboratory_tests']:
        plan_text += f"""
- {test['test']}
  Frequency: {test['frequency']}
  Targets: {test.get('targets', test.get('target', 'As per physician'))}
"""
    
    plan_text += f"""

PSYCHOLOGICAL SUPPORT
{'='*20}
"""
    for intervention in treatment_dir['psychological_support']['interventions']:
        plan_text += f"""
- {intervention['type']}
"""
        if 'recommendation' in intervention:
            plan_text += f"  Recommendation: {intervention['recommendation']}\n"
        if 'apps' in intervention:
            plan_text += f"  Recommended Apps: {intervention['apps']}\n"
    
    plan_text += f"""

IMPORTANT DISCLAIMERS:
{'='*20}
• This treatment plan is generated for educational purposes only
• All medical decisions must be made in consultation with qualified healthcare professionals
• Do not start, stop, or modify any treatments without medical supervision
• In case of emergency, call 911 immediately
• Keep this plan updated with your healthcare provider

Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    
    return plan_text
