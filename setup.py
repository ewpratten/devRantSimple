from setuptools import setup


setup(
    name='devRantSimple',
    version='1.0',
    description='A simple devRant api wrapper for the lazy people',
    long_description=open("README.rst").read(),
    url='https://github.com/Ewpratten/devRantSimple',
    author='Evan Pratten',
    author_email='ewpratten@gmail.com',
    license='MIT',
    packages=['devRantSimple'],
    install_requires=['requests', 'enum34'],
    zip_safe=False)