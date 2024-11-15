
'''
This module interacts with GCS.
'''
from google.cloud import storage

class GcsClient:
    '''GCS Client.'''

    def __init__(self):
        pass

    def download_blob(self, bucket_name, source_blob_name):
        '''Downloads a blob from the bucket.'''
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The ID of your GCS object
        # source_blob_name = "storage-object-name"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        # Construct a client side representation of a blob.
        # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
        # any content from Google Cloud Storage. As we don't need additional data,
        # using `Bucket.blob` is preferred here.
        blob = bucket.blob(source_blob_name)
        print(source_blob_name)
        return blob.download_as_bytes()
