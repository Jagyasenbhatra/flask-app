from setuptools import setup, find_packages

setup(
    name="myapp",  
    version="0.1.0",  
    description="A short description of your package",
    long_description=open("README.md").read(),  
    author="Jack",
    author_email="example@example.com",
    url="https://github.com/Jagyasenbhatra/flask-app.git",
    packages=find_packages(),
    install_requires=[
        "flask", 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)