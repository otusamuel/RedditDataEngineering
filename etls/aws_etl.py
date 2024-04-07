import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY


def connect_to_s3():
    """
    Establishes a connection to AWS S3 using credentials.

    Returns:
        s3fs.S3FileSystem: An instance of the S3FileSystem class configured
        with specified credentials for AWS S3 access.
    """
    try:
        # Initialize a S3FileSystem object with AWS access keys for authenticated access.
        s3 = s3fs.S3FileSystem(anon=False, key=AWS_ACCESS_KEY_ID, secret=AWS_ACCESS_KEY)
        return s3
    except Exception as e:
        # Print any exceptions encountered during the connection attempt.
        print(e)


def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket: str):
    """
    Checks if an S3 bucket exists, and creates it if it doesn't.

    Parameters:
        s3 (s3fs.S3FileSystem): An instance of the S3FileSystem to interact with AWS S3.
        bucket (str): The name of the bucket to check or create.
    """
    try:
        # Check if the bucket already exists.
        if not s3.exists(bucket):
            # Create the bucket if it does not exist.
            s3.mkdir(bucket)
            print("Bucket created")
        else:
            # Inform the user if the bucket already exists.
            print("Bucket already exists")
    except Exception as e:
        # Print any exceptions that occur during the process.
        print(e)


def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, s3_file_name: str):
    """
    Uploads a file to a specified bucket in AWS S3.

    Parameters:
        s3 (s3fs.S3FileSystem): An instance of the S3FileSystem for file operations.
        file_path (str): The local path of the file to be uploaded.
        bucket (str): The target bucket name in S3.
        s3_file_name (str): The file name under which the file will be stored in S3.
    """
    try:
        # Construct the full S3 path where the file will be uploaded.
        # The file will be placed inside a 'raw' directory within the specified bucket.
        target_path = f'{bucket}/raw/{s3_file_name}'
        # Use the put method to upload the file.
        s3.put(file_path, target_path)
        print('File uploaded to S3')
    except FileNotFoundError:
        # Handle the case where the local file is not found.
        print('The file was not found')
