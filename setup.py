from setuptools import setup, find_packages 

with open('README.md', 'r',encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '1.7.0'
DESCRIPTION = 'ML module'

setup(
    name="MLHybridX",
    version=VERSION,
    author="Deepak and Sudheer",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(), 
    install_requires=['sklearn', 'pandas', 'numpy'],
    keywords=['train', 'split', 'df', 'predict'],
    classifiers=[
        "Development Status :: 1 - Planning", 
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)