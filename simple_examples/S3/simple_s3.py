import boto3

# Create an S3 client
s3_client = boto3.client('s3')


def list_buckets():
    """List all S3 buckets."""
    response = s3_client.list_buckets()
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")


def list_objects(bucket_name, prefix):
    """List objects in a specific S3 bucket and path."""
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    print(f"\nObjects in s3://{bucket_name}/{prefix}:")
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"  {obj['Key']}")
    else:
        print("No objects found.")


def download_file(bucket_name, key, download_path):
    """Download a specific file from S3."""
    s3_client.download_file(bucket_name, key, download_path)
    print(f"Downloaded {key} to {download_path}.")

# List all buckets
list_buckets()

# List objects in the specified S3 path
bucket_name = 'dff-file-example'
prefix = 'some_files/GoT/'
list_objects(bucket_name, prefix)

# Download a specific file (characters_basic.json)
file_key = 'some_files/GoT/characters_basic.json'
download_path = 'characters_basic.json'
download_file(bucket_name, file_key, download_path)
