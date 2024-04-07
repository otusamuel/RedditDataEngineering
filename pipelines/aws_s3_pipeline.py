from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME


def upload_s3_pipeline(ti):
    """
    Orchestrates a pipeline to upload a file to an AWS S3 bucket.

    This function retrieves a file path from Airflow's XCom, establishes a connection to AWS S3,
    ensures the target bucket exists, and uploads the file to that bucket.

    Parameters:
    - ti: TaskInstance from Apache Airflow. Used to pull data from previous tasks.
    """
    # Retrieve the file path from the output of a previous task named 'reddit_extraction'.
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

    # Establish a connection to AWS S3 using predefined credentials.
    s3 = connect_to_s3()

    # Ensure the target AWS S3 bucket exists; create it if it does not.
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)

    # Extract the filename from the file_path.
    # For example, if file_path is '/data/reddit/comments.csv', the filename would be 'comments.csv'.
    filename = file_path.split('/')[-1]

    # Upload the file to the specified AWS S3 bucket.
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, filename)
