#copy file from one bucket to another bucket(NOTE:- Region must be same)
import boto3
from botocore.client import Config
#get the service client
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6HA', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')
print("TODO done till here!!")
# Copies object located in mybucket at mykey
# to the location otherbucket at otherkey
copy_source = {
    'Bucket': 'clinmdmcelebal',
    'Key': 'key-name_1'
}

print("Done here step2!!!")
s3.copy(copy_source, 'clinmdmcelebal1', 'S1_MIS.txt')
print("Copy done!!!")
