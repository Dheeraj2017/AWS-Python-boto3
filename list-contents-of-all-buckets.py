#iterate over buckets and keys
import boto3
from botocore.client import Config
s3 = boto3.resource('s3', aws_access_key_id = 'AKIAI6KLHZTL7BAVG6HA', aws_secret_access_key = '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',config=Config(signature_version='s3v4'))
print("Step1!!!")
for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        print(key.key)
print("Complete!!")

#OUTPUT
"""
Step1!!!
Omitvi.csv
sample_source_1.csv
sample_source_2.csv
sample_source_3.csv
sample_source_4.csv
sample_source_5.csv
test.txt
S1_MIS_new.txt
key-name_1
S1_MIS.txt
key-name_1
S1_MIS.csv
S2_Marina.csv
Test/
Test/S3_MIS.csv
key-name
key-name_1
key-name_manage
Complete!!
"""
