import os
import requests

# ftp
bucket_name = "test-bucket5807738"
file_name = "s3commands.py"

query = requests.get(f"https://aysv85odkb.execute-api.us-east-2.amazonaws.com/\
default/lambdaftp\
?bucket={bucket_name}\
&filename={file_name}")

os.makedirs("output", exist_ok=True)
file_content = query.content
with open(f"output/{file_name}", "wb") as file:
    file.write(file_content)
