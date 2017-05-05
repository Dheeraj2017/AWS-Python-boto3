# create a new bucket in amazon s3
import boto3

#create the boto3 client
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6', aws_secret_access_key = '9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')

#create bucket with unique name
s3.create_bucket(Bucket='clinmdmcelebal1')

#OUTPUT
"""
{'Location': '/clinmdmcelebal1',
 'ResponseMetadata': {'HTTPHeaders': {'content-length': '0',
   'date': 'Fri, 05 May 2017 06:00:36 GMT',
   'location': '/clinmdmcelebal1',
   'server': 'AmazonS3',
   'x-amz-id-2': 'Yuo3bdsJW4+02S0WJV5ZcZbXMNf191D+fKX/20JK8JRkYCnpiSXUXjespZtF5dyIn5yHyJg/WZ8=',
   'x-amz-request-id': '8E52740B81017E22'},
  'HTTPStatusCode': 200,
  'HostId': 'Yuo3bdsJW4+02S0WJV5ZcZbXMNf191D+fKX/20JK8JRkYCnpiSXUXjespZtF5dyIn5yHyJg/WZ8=',
  'RequestId': '8E52740B81017E22',
  'RetryAttempts': 0}}

"""
