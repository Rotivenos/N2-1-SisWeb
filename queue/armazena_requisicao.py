import json
import boto3


sqs = boto3.client('sqs')
queue_url = 'https://recommendationQueue.com'

def lambda_handler(event, context):
    try:
        user_id = event['user_id']

        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=user_id
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Requisição enfileirada com sucesso!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao enfileirar requisição: {str(e)}')
        }
