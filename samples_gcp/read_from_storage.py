from google.cloud import storage
def read_from_blob(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("r") as csv_file:
        for line in csv_file.readlines():
            print(line)

if __name__ == "__main__":
    read_from_blob(
        bucket_name="jsenacas",
        blob_name="indexProcessed",
    )