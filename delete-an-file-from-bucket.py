#delete an file from a S3 bucket
import boto3
from botocore.client import Config
#get the service client
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6HA', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To',config=Config(signature_version='s3v4'))
print("TODO done till here!!")

s3.delete_object(Bucket='clinmdm', Key='test.txt')
print("Delete done!!!")
