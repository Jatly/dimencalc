from setuptools import setup, find_packages

setup(
    name='dimencalc',  # The name of your library
    version='1.0.0',  # Version of your release
    description='A Python library to calculate area, perimeter, volume, and surface area',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jatly',
    author_email='jatly.aj.29@gmail.com',
    url='https://github.com/Jatly/dimencalc.git',  # Your project repository URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python versions your package supports
)
