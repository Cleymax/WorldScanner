from os import read

import setuptools

with open("README.md") as file:
    long_desc = file.read()

setuptools.setup(
    name='WorldScanner',
    version='1.0.0',
    author='Clément P. (Cleymax)',
    author_email='contact@cleymax.fr',
    description='The best scanner in the minecraft world',
    license='MIT',
    keywords='minecraft,world,scanner,nbt',
    long_description_content_type='text/markdown',
    long_description=long_desc,
    packages=setuptools.find_packages(),
    url='https://github.com/Cleymax/WorldScanner',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
