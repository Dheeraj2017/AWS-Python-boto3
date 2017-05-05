#Download a file from s3 bucket to local system
import boto3

#get the service client
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6HA', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')

#download object at bucket-name with key-name to tmp.txt
s3.download_file("dheerajnew", "S1_MIS.csv", "new.csv")
print("Done downloading!!!")
