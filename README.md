# Python S3for.me client

This package contains a client and a querystring generator, which can
be used to interact with the S3for.me system, which is based on Amazon S3's API. The two main
interface classes are S3fmAuthConnection and QueryStringAuthGenerator.

S3fmAuthConnection performs HTTP requests with appropriate header signing.

QueryStringAuthGenerator has the same interface, but instead of
performing the HTTP request, this class will return URLs with the right
querystring authentication parameters set.

The latest version of the source code is available from <https://github.com/mrmarksteadman/s3forme>.
The code is a fork of [the Amazon S3 client code from nephics](https://github.com/nephics/python-s3).

## Basic Operations

### Object requests

GetResponse get(bucket_name, key_name) - retrieves an object
GetResponse get_acl(bucket_name, key_name) - returns the xml acl doc
Response put(bucket_name, key_name, object) - writes an object
Response put_acl(bucket_name, key_name, aclXMLDoc) - sets the xml acl doc
Response delete(bucket_name, key_name) - deletes an object

### Bucket requests

Response create_bucket(bucket_name) - creates a bucket
Response create_located_bucket(bucket_name, location) - creates a bucket with a location constraint  
ListResponse list_bucket(bucket_name) - lists a bucket's contents
LocationResponse get_bucket_location(bucketName) - return the location-constraint of this bucket
GetResponse get_bucket_acl(bucket_name) - returns the xml representation of this bucket's access control list
Response put_bucket_acl(bucket_name, acl_xml_doc) - sets xml representation of the bucket acl
Response delete_bucket(bucket_name) - delete an empty bucket
GetResponse get_bucket_logging(bucket_name) - returns the xml representation of this bucket's access logging configuration
Response put_bucket_logging(bucket_name, logging_xml_doc) - sets the xml representation of the bucket logging configuration

ListAllMyBucketsResponse list_all_my_buckets() - returns a list of all buckets owned by this S3for.me Access Key ID

## Dependencies

None other than the standard libraries.

## Limitations

A previous limitation of the S3fmAuthConnection implementation was that
the request response was stored as a byte array in memory. This was
fine for smaller objects, but large objects, say a couple megabytes or
greater, will show poor performance, since everything is being passed
around in memory.  With version 0.2.0 this has changed: Response sizes
over a predefined limit are now (by default) automatically spooled to a
temporary file. This implies that data of an S3Object is available via a
file like interface (not as a byte string as in previous versions).

The S3fmAuthConnection requests are all blocking - that is, the request
will continue until all response data is downloaded, and you cannot look
at the request is complete.

There is very little error handling. All errors from lower libraries are
simply passed up. The response code in the connection object needs to be
checked after each request to verify whether the request succeeded.

There is no support for repeated headers, it is assumed that each header
will have only one value.

It is our intention that these libraries act as a starting point for
future development.  They are meant to show off the various operations
and provide an example of how to negotiate the authentication process.

## License

This software code is made available "AS IS" without warranties of any		
kind.  You may copy, display, modify and redistribute the software			
code either by itself or as incorporated into your code; provided that		
you do not remove any proprietary notices.  Your use of this software		 
code is at your own risk and you waive any claim against Amazon			   
Digital Services, Inc. or its affiliates with respect to your use of		  
this software code. (c) 2006-2007 Amazon Digital Services, Inc. or its			 
affiliates.