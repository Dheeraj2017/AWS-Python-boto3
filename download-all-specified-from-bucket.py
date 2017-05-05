import sys
import threading

import boto3

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._seen_so_far = 0
        self._lock = threading.Lock()
    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            sys.stdout.write(
                "\r%s --> %s bytes transferred" % (
                    self._filename, self._seen_so_far))
            sys.stdout.flush()

#get the service client
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6HA', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')

# Download object at bucket-name with key-name to tmp.txt
file_list = ['S1_MIS.csv', 'S2_Marina.csv', 'key-name', 'key-name_1', 'key-name_manage']
count = 0
for filename in file_list:
    print(filename)
    s3.download_file("dheerajnew", str(filename), str(filename), Callback=ProgressPercentage(str(filename)))
    count += 1
    print("Done " + str(count))

print("Downloading done!!!@")

#OUTPUT
"""
S1_MIS.csv
S1_MIS.csv --> 13867 bytes transferredDone 1
S2_Marina.csv
S2_Marina.csv --> 9555 bytes transferredDone 2
key-name
key-name --> 17 bytes transferredDone 3
key-name_1
key-name_1 --> 17 bytes transferredDone 4
key-name_manage
key-name_manage --> 17 bytes transferredDone 5
Downloading done!!!@
"""
