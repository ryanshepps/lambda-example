import boto3
import botocore


s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = event["queryStringParameters"].get("bucket")
    file_name = event["queryStringParameters"].get("filename")

    try:
        file = s3.meta.client.get_object(
            Bucket=bucket,
            Key=file_name)["Body"].read()
    except botocore.exceptions.ClientError as error:
        return {
            "statusCode": 500,
            "body": f"There was an issue downloading your file... {error}"
        }

    return {
        'statusCode': 200,
        'body': bytes.decode(file, "utf-8")
    }
