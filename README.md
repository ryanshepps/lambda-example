# Lambda Example

## Task 1

This code is deployed via a zip file through Lambda's console. The lambda function can be found in `functions/ftp.py`. To run this application, you can need to `pip install -r requirements.txt`, then you can run `python lambdaftp.py` which uses the Lambda function's API gateway to run the function. You can also modify lambdaftp to point to a bucket/file that you need.

## Task 2

This code is deployed via the Elastic Search Registry in AWS Lambda. The Dockerfile to build the image can be found in `Dockerfile`. Once the image is built, you can deploy the image to ECR via the command line. You then need to pull the latest image into the lambda function where it will run the changes. The actual Lambda function can be found in `functions/subscribe.py`.