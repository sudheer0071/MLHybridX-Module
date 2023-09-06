from setuptools import setup, find_packages 

with open('README.md', 'r',encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '1.3.0'
DESCRIPTION = 'ML module'

setup(
    name="mlhybridx",
    version=VERSION,
    author="Deepak and Sudheer",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(), 
    install_requires=['scikit-learn', 'pandas', 'numpy','seaborn'],
    keywords=['train', 'split', 'df', 'predict'],
    classifiers=[
        "Development Status :: 1 - Planning", 
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ]
)




# ///////////////// TOKEN for pypi /////////////////////////////

# username = __token__
# "pypi-AgEIcHlwaS5vcmcCJGU4NDI3YWM4LWQ5NjctNGRlNC1hYWU2LTc1NTViMmM2YTRlMAACEVsxLFsibWxoeWJyaWR4Il1dAAIsWzIsWyJhOTljMTllOS00ODE3LTQ1YTctYWZiNy0wZTc4ZTFkOTM0ZmYiXV0AAAYgQ0MCt_SWPCee9lFCW669Pc7F8qiM8eD1Vu8fj0O4n90"



# ///////////////// TOKEN for test.pypi /////////////////////////////

# username = __token__
# "pypi-AgENdGVzdC5weXBpLm9yZwIkMDA3OWYzNDctNTVhNS00MWFjLTg4MjAtMjMyZjYyOGQ1ZTkzAAIRWzEsWyJtbGh5YnJpZHgiXV0AAixbMixbIjNjMmIxNWFlLWRhZmYtNGM3Ny05YTMyLWFhNDc2N2QxMWVmNiJdXQAABiAgaTP3DlblEPDgpKLErsaeCtxB5ZN1RCikKSjZ3VO-Iw"

