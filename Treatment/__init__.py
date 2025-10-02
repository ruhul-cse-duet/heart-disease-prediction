"""
Heart Disease Treatment Module

This module contains comprehensive treatment recommendations and plan generation
for heart disease patients.

Available functions:
- get_treatment_recommendations(): Returns structured treatment directory
- generate_treatment_plan_pdf(): Generates downloadable treatment plan
"""

from .treatment import get_treatment_recommendations, generate_treatment_plan_pdf

__all__ = ['get_treatment_recommendations', 'generate_treatment_plan_pdf']
__version__ = '1.0.0'
