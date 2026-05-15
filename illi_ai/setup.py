from setuptools import setup 
 
setup( 
    name="illi-ai-professional", 
    version="1.0.0", 
    author="Muhammad Farhan", 
    author_email="farhanhomeschooling519@gmail.com", 
    description="Complete PC & Web Control System with Voice Control and AI Features", 
    url="https://github.com/Farhanillahiclass/illi-ai-assistant", 
    py_modules=["illi_ai"], 
    install_requires=[ 
        "psutil>=5.9.0", 
        "speechrecognition>=3.10.0", 
        "pyttsx3>=2.90", 
        "requests>=2.28.0", 
        "GitPython>=3.1.0", 
        "cryptography>=3.4.0", 
        "numpy>=1.21.0" 
    ], 
    entry_points={ 
        "console_scripts": [ 
            "illi-ai=illi_ai:main", 
        ], 
    }, 
    classifiers=[ 
        "Development Status :: 5 - Production/Stable", 
        "Intended Audience :: End Users/Desktop", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: Microsoft :: Windows", 
        "Programming Language :: Python :: 3", 
        "Topic :: Desktop Environment", 
        "Topic :: System :: Monitoring", 
        "Topic :: Utilities", 
    ], 
    python_requires=">=3.7", 
) 
