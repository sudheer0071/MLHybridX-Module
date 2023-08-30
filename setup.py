from setuptools import setup, find_packages 

with open('README.md', 'r',encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '1.1.0'
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
# "pypi-AgEIcHlwaS5vcmcCJDc3ZTQ4ZTdkLTJkYTUtNDk0Mi1hYjAzLTAwNDkzZmZkYmY3NAACKlszLCI1MTUyZWU2Ny04MGMzLTQwMzItOWI5Ny1mOWI5ZDFmZmUwZGUiXQAABiD4gvLAQ3JGXbnOjyuzM5gZNoyd0WdQ2KYoe3bP7EAJnQ"



# ///////////////// TOKEN for test.pypi /////////////////////////////

# username = __token__
# "pypi-AgENdGVzdC5weXBpLm9yZwIkMDA3OWYzNDctNTVhNS00MWFjLTg4MjAtMjMyZjYyOGQ1ZTkzAAIRWzEsWyJtbGh5YnJpZHgiXV0AAixbMixbIjNjMmIxNWFlLWRhZmYtNGM3Ny05YTMyLWFhNDc2N2QxMWVmNiJdXQAABiAgaTP3DlblEPDgpKLErsaeCtxB5ZN1RCikKSjZ3VO-Iw"

