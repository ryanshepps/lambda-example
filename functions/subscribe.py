import boto3
import botocore

s3 = boto3.resource("s3")

destination_buckets = [
    "1091670-tom",
    "1091670-harry",
    "1091670-dick"
]


def handler(event, context):
    source_file_s3_info = event['Records'][0]['s3']

    source_file_key = source_file_s3_info['object']['key']
    source_file_bucket = source_file_s3_info['bucket']['name']
    source_file_path = {
        "Bucket": source_file_bucket,
        "Key": source_file_key
    }

    for destination_bucket in destination_buckets:
        s3.meta.client.copy(
            Bucket=destination_bucket,
            CopySource=source_file_path,
            Key=source_file_key,
        )
