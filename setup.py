from setuptools import setup, find_packages

setup(
    name='code_line_counter',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library to count lines of code excluding comments and empty lines.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YourUsername/CodeLineCounter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


