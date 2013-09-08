__version__ = '0.2.1'
__author__ = 'Jacob Sondergaard'
__url__ = 'http://bitbucket.org/nephics/python-s3'
__doc__ = '''

	S3for.me client and querystring generator
	
	This package contains a client and a querystring generator, which can
	be used to interact with the S3for.me system. The two main interface
	classes are S3fmAuthConnection and QueryStringAuthGenerator.

	S3fmAuthConnection performs http requests with appropriate header
	signing.

	QueryStringAuthGenerator, has the same interface, but instead of
	performing the http request, this class will return urls with the right
	querystring authentication parameters set.

'''

from S3forme import S3fmAuthConnection, QueryStringAuthGenerator, S3Object, Location, CallingFormat
