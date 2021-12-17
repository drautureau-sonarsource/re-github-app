import os
import boto3

client = boto3.client('sns')


def publish_to_topic(topic_arn, payload):
    client.publish(
        TopicArn=topic_arn,
        Message=payload
    )


def verify_integrity():
    # TODO
    pass


def handler(event, context):
    verify_integrity()
    event_type = event['headers']['x-github-event']
    event_body = event['body']
    if event_type == 'release':
        print(f'Forwarding {event_type} body to the release request topic')
        publish_to_topic(os.environ.get('RELEASE_REQUEST_TOPIC_ARN'), event_body)
    else:
        payload = {'event-type': event_type, 'event_body': event_body}
        print(f'Forwarding payload of type {event_type} to the backend topic')
        publish_to_topic(os.environ.get('BACKEND_TOPIC_ARN'), payload)
    return {
        'statusCode': 200
    }
