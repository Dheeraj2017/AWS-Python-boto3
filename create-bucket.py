# create a new bucket in amazon s3
import boto3

#create the boto3 client
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6', aws_secret_access_key = '9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')

#create bucket with unique name
s3.create_bucket(Bucket='clinmdmcelebal1')
