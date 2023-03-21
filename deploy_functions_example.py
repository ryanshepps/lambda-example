import configparser

import boto3


def authenticate(
        aws_client_name: str,
        relative_config_location: str) -> object:
    aws_config = configparser.ConfigParser()
    aws_config.read(relative_config_location)
    return boto3.client(
        aws_client_name,
        aws_access_key_id=aws_config.get("default", "aws_access_key_id"),
        aws_secret_access_key=aws_config.get("default", "aws_secret_access_key"))


if __name__ == "__main__":
    lambda_client = authenticate("lambda", "./authentication.conf")
    iam_client = authenticate("iam", "./authentication.conf")

    # Create ftp function that downloads an object from s3
    lambda_client.create_function(
        FunctionName="lambdaftp",
        Runtime="python3.9",
        Role="arn:aws:lambda:us-east-2:081138103994:function:lambdaftp",
        Handler="lambda_function.lambda_handler",
    )
