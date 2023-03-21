import boto3
import botocore


def lambda_hander(event, context):
    s3 = boto3.resource("s3")
    file = None

    bucket = event.get("bucket")
    file_name = event.get("filename")

    try:
        file = s3.meta.client.get_object(
            Bucket=bucket,
            key=file_name)["Body"].read()
    except botocore.exceptions.ClientError as error:
        return {"error": f"There was an issue downloading your file... {error}"}

    response = {"file": file}
    return response
