__version__ = '0.1.0'
__author__ = 'Jacob Sondergaard'
__url__ = 'http://bitbucket.org/nephics/python-s3'
__doc__ = '''

    S3 client and query string generator

    This package contains a client and a query string generator, which can
    be used to interact with the Amazon S3 system. The two main interface
    classes are AWSAuthConnection and QueryStringAuthGenerator.

    AWSAuthConnection performs http requests with appropriate header
    signing.

    QueryStringAuthGenerator, has the same interface, but instead of
    performing the http request, this class will return urls with the right
    query string authentication parameters set.

'''

from S3 import (AWSAuthConnection, QueryStringAuthGenerator, S3Object,
        Location, CallingFormat)
