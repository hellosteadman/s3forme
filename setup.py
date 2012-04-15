from distutils.core import setup

setup(
    name='python-s3',
    version='0.2.1',
    author='Jacob Sondergaard',
    author_email='jacob@nehics.com',
    packages=['s3'],
    url='http://bitbucket.org/nephics/python-s3/',
    license='LICENSE.txt',
    description='Python S3 client and query string generator.',
    long_description=open('README.md').read()
)
