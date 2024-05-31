from setuptools import setup, find_packages

setup(
    name='my_nlp_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'tensorflow',
        'transformers'
    ],
    description='A package for NLP data generation using BERT',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_nlp_package',  # Replace with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)