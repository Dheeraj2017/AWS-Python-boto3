#list all the contents of amamzon s3 buckets
import boto3
s3 = boto3.resource('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6HA', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')

mybucket = s3.Bucket('dheerajnew')
for file in mybucket.objects.all():
    print(file.key)
 
#OUTPUT
"""
S1_MIS.csv
S2_Marina.csv
Test/
Test/S3_MIS.csv
"""
