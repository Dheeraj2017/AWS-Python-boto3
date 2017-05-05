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
s3.download_file(
    "dheerajnew", "S2_Marina.csv", "tmp.csv",
    Callback=ProgressPercentage("tmp.csv"))
print("Downloading done!!!@")
