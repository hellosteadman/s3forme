# Python S3 client

This package contains a client and a query string generator, which can
be used to interact with the Amazon S3 system. The two main interface
classes are AWSAuthConnection and QueryStringAuthGenerator.

AWSAuthConnection performs http requests with appropriate header
signing.

QueryStringAuthGenerator, has the same interface, but instead of
performing the http request, this class will return urls with the right
query string authentication parameters set.

The latest version of the source code is available from [http://bitbucket.org/nephics/python-s3](http://bitbucket.org/nephics/python-s3). The code is a fork of [the original
client code from Amazon](http://aws.amazon.com/code/134).

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

ListAllMyBucketsResponse list_all_my_buckets() - returns a list of all buckets owned by this AWS Access Key Id


## Dependencies

None other than the standard libraries.


## Limitations

One of the main limitations of these sample AWSAuthConnection implementations
is that the interfaces are not streaming.  This means that you have to pass the
data in as a string or as a byte array and the operation returns a string or a
byte array back.  This is conceptually simpler, and fine for smaller objects,
but large objects, say a couple megabytes or greater, will show poor
performance, since everything is being passed around in memory.  More
sophisticated libraries would pass streams in and out, and would only read the
data on-demand, rather than storing it all in memory (S3 itself would have no
problem with such streaming applications).  Another upshot of this is that the
interfaces are all blocking---that is, you cannot look at the data until all of
it has downloaded.  Again, this is fine for smaller objects, but unacceptable
for larger ones.

These libraries have nearly non-existent error handling.  All errors from lower
libraries are simply passed up.  The response code in the connection object needs
to be checked after each request to verify whether the request succeeded.

Only the java library has proper handling for repeated headers.  The others
assume that each header will have only one value.

It is our intention that these libraries act as a starting point for future
development.  They are meant to show off the various operations and provide an
example of how to negotiate the authentication process.


## License

This software code is made available "AS IS" without warranties of any        
kind.  You may copy, display, modify and redistribute the software            
code either by itself or as incorporated into your code; provided that        
you do not remove any proprietary notices.  Your use of this software         
code is at your own risk and you waive any claim against Amazon               
Digital Services, Inc. or its affiliates with respect to your use of          
this software code. (c) 2006-2007 Amazon Digital Services, Inc. or its             
affiliates.
