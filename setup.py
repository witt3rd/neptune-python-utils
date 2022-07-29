import os

from setuptools import setup, find_packages


def read(filename):
    path = os.path.join(os.getcwd(), filename)
    with open(path, 'r') as f:
        return f.read()


install_requires = [
    'gremlinpython==3.5.1',
    'requests',
    'backoff',
    'cchardet',
    'aiodns',
    'idna-ssl',
]

setup(
    name='neptune-python-utils',
    version='0.0.1',
    description='Python 3 library that simplifies using Gremlin-Python to connect to Amazon Neptune.',
    long_description=read('README.md'),
    author='Ian Robinson',
    url='https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils',
    packages=find_packages(),
    install_requires=install_requires,
    license='Apache 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
