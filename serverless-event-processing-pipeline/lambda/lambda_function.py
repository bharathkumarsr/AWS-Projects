import json
import os
import boto3
import traceback
from urllib.parse import unquote_plus
from datetime import datetime

# AWS Clients
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

# Environment Variables
TABLE_NAME = os.environ["TABLE_NAME"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    print("========== Lambda Started ==========")
    print(json.dumps(event, indent=2))

    try:

        for record in event["Records"]:

            bucket = record["s3"]["bucket"]["name"]

            object_key = unquote_plus(record["s3"]["object"]["key"])

            print(f"Bucket      : {bucket}")
            print(f"Object Key  : {object_key}")

            # Read object metadata
            response = s3.head_object(
                Bucket=bucket,
                Key=object_key
            )

            file_size = response["ContentLength"]
            content_type = response.get("ContentType", "Unknown")
            etag = response["ETag"].replace('"', "")

            upload_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

            item = {
                "FileName": object_key,
                "Bucket": bucket,
                "FileSize": str(file_size),
                "ContentType": content_type,
                "ETag": etag,
                "UploadTime": upload_time,
                "Status": "Processed"
            }

            print("Writing item to DynamoDB...")
            print(item)

            table.put_item(Item=item)

            print("Item successfully stored.")

            message = f"""
Serverless Event Processing

File processed successfully.

Bucket Name : {bucket}

File Name : {object_key}

File Size : {file_size} bytes

Content Type : {content_type}

Upload Time : {upload_time}

Status : SUCCESS
"""

            print("Publishing SNS Notification...")

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="Serverless Event Processing",
                Message=message
            )

            print("SNS Notification Sent Successfully")

        print("========== Lambda Completed ==========")

        return {
            "statusCode": 200,
            "body": json.dumps("Success")
        }

    except Exception as e:

        print("========== ERROR ==========")
        print(str(e))
        print(traceback.format_exc())

        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }
