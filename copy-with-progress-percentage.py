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
print("TODO done till here!!")
# Copies object located in mybucket at mykey
# to the location otherbucket at otherkey
copy_source = {
    'Bucket': 'clinmdmcelebal1',
    'Key': 'S1_MIS.txt'
}

print("Done here step2!!!")
print(copy_source)
s3.copy(copy_source, 'clinmdmcelebal', 'S1_MIS_new.txt', Callback=ProgressPercentage("clinmdmcelebal/S1_MIS_new.txt"))

print("Done Copy !!!!")

#OUTPUT
"""
TODO done till here!!
Done here step2!!!
{'Bucket': 'clinmdmcelebal1', 'Key': 'S1_MIS.txt'}
clinmdmcelebal/S1_MIS_new.txt --> 17 bytes transferredDone Copy !!!!
"""
