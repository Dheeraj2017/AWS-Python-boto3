# this is for amazon s3 connector in MDM

import boto3

# let's use amazon s3
s3 = boto3.resource('s3', aws_access_key_id = 'IAI6KLHZTL7BAVG6', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')
print(s3)

# for print out all the bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    
