from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    install_requires=["openai","langchain","streamlit","python-dotdev","PyPDF2"],
    packages=find_packages()
)