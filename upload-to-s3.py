#upload a new file in a already existed bucket
data = open('test.txt', 'rb')
#showing error in the next line
s3.Bucket('clinmdm').put_object(Key='test.txt', Body=data)
