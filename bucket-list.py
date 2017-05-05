#list buckets using list_buckets function
import boto3

#create an s3 client
s3 = boto3.client('s3', aws_access_key_id = 'AKIAI6KLHZTL7BAVG6', aws_secret_access_key = 'Ds9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')

#call s3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

#OUTPUT
#Bucket List: ['clinmdm', 'dheerajnew']
