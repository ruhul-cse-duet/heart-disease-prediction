from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="heart-disease-prediction",
    version="1.0.0",
    author="Ruhul Amin",
    author_email="ruhul.cse.duet@gmail.com",
    description="A Streamlit web application for heart disease prediction using machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ruhul-cse-duet/heart-disease-prediction",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "heart-disease-app=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.csv", "*.pkl", "*.toml"],
    },
)

