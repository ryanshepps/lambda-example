import os
import requests

# ftp
bucket_name = "1091670-harry"
file_name = "GCloudComposer.py"

query = requests.get(f"https://aysv85odkb.execute-api.us-east-2.amazonaws.com/\
default/lambdaftp\
?bucket={bucket_name}\
&filename={file_name}")

if query.status_code == 200:
    os.makedirs("output", exist_ok=True)
    file_content = query.content
    with open(f"output/{file_name}", "wb") as file:
        file.write(file_content)
else:
    print(f"An error ocurred: {bytes.decode(query.content, 'utf-8')}")
