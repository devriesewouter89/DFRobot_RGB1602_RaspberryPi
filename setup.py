import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rgb1602',
    version='0.0.1',
    description='installation of Package rgb1602',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/devriesewouter89/DFRobot_RGB1602_RaspberryPi',
    packages=['rgb1602'],
    install_requires=['wiringpi'],
    license='GNU LGPL v3'
)
