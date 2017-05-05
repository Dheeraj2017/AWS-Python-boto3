#upload file to amazon s3 bucket 
import boto3
from botocore.client import Config

data = open('test.txt', 'rb')
s3 = boto3.resource('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To', config=Config(signature_version='s3v4'))
s3.Bucket('clinmdm').put_object(Key='test.txt', Body=data)
print("Done")


#different methods to upload a file 
import boto3
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6HA', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')
# Upload test.txt to bucket-name at key-name

#s3.upload_file("Specifiy the file path want to upload", "bucket-name", "name with which we want to upload to S3")

s3.upload_file("test.txt", "clinmdmcelebal1", "key-name_1")
print("Done")
