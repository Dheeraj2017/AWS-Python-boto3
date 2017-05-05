import os
import sys
import threading
import boto3

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s %s / %s  (%.2f%%)" %(
                    self._filename, self._seen_so_far, self._size,
                    percentage
                )
            )
            sys.stdout.flush()

#Get the service client
s3 = boto3.client('s3', aws_access_key_id = 'AI6KLHZTL7BAVG6HA', aws_secret_access_key = 's9fkJEgvm2+koAHFkz2d8/xOzR8/5tlZAp9To')

#upload test.txt to bucket-name at key-name
s3.upload_file("test.txt", "dheerajnew", "key-name_manage", Callback=ProgressPercentage("test.txt"))
print("Done!!!")

#OUTPUT
"""
test.txt 17 / 17.0  (100.00%)
Done!!!
"""
