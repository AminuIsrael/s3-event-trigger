import os
import json
import boto3

SENDER_EMAIL = os.environ["SENDER_EMAIL"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]
SUBJECT = "S3 Event Notification"


def lambda_handler(event, context):
    """
    Lambda Function for Sending Data event

    Args:
        event ([type]): Json event
        context ([type]): [description]
    """
    data_response = serialize_event_data(event)
    send_mail(recipient=SENDER_EMAIL,
              sender=RECEIVER_EMAIL,
              subject=SUBJECT,
              html_body=json.dumps(data_response))
    

def serialize_event_data(json_data):
    """
    Extract data from s3 event

    Args:
        json_data ([type]): Event JSON Data
    """
    bucket = json_data["Records"][0]["s3"]["bucket"]["name"]
    timestamp = json_data["Records"][0]["eventTime"]
    s3_key = json_data["Records"][0]["s3"]["object"]["key"]
    s3_data_size = json_data["Records"][0]["s3"]["object"]["size"]
    ip_address = json_data["Records"][0]["requestParameters"][
        "sourceIPAddress"]
    event_type = json_data["Records"][0]["eventName"]
    owner_id = json_data["Records"][0]["s3"]["bucket"]["ownerIdentity"][
        "principalId"]
    
    return_json_data = {
        "event_timestamp": timestamp,
        "bucket_name": bucket,
        "object_key": s3_key,
        "object_size": s3_data_size,
        "source_ip": ip_address,
        "event_type": event_type,
        "owner_identity": owner_id
    }

    return return_json_data

def send_mail(recipient: str,
              sender: str,
              subject: str,
              html_body: str,
              encoding: str = "UTF-8"):
    """
    Send Email address using the Amazon SES service
    NOTE: You need to add the sender email in the list of email addresses using the default sandbox environment

    Args:
        sender (str): Sender email
        recipient (str): Receiver email
        subject (str): Email Subject
        html_body (str): HTML body
    """

    session = boto3.session.Session()
    client = session.client('ses')

    response = client.send_email(Destination={'ToAddresses': [recipient]},
                                 Message={
                                     'Body': {
                                         'Html': {
                                             'Charset': encoding,
                                             'Data': html_body,
                                         }
                                     },
                                     'Subject': {
                                         'Charset': encoding,
                                         'Data': subject,
                                     },
                                 },
                                 Source=sender)
    return response