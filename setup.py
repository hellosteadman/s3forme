from distutils.core import setup

setup(
	name = 's3form3',
	version = '0.1',
	author = 'Mark Steadman',
	author_email = 'marksteadman@me.com',
	packages = ['s3forme'],
	url = 'https://github.com/mrmarksteadman/s3forme',
	license = 'LICENSE.txt',
	description = 'Python S3for.me client and querystring generator.',
	long_description = open('README.md').read()
)