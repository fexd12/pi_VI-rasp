from setuptools import find_packages, setup

setup(
    name="raspPi",
    version="1.0",
    description="",
    packages=find_packages(),
    install_requires=[
        'RPi.GPIO',
        'spidev',
        'python-dotenv'
        ]
)
