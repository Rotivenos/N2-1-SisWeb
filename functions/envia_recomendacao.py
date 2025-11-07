import json

def lambda_handler(event, context):
    try:
        recommendations = json.loads(event['body'])

        send_recommendations_to_user(recommendations)

        return {
            'statusCode': 200,
            'body': json.dumps('Recomendações enviadas com sucesso.')
        }

    except Exception as e:
        print(f"Erro ao enviar recomendações: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao enviar recomendações.')
        }

def send_recommendations_to_user(recommendations):
    print(f"Enviando recomendações: {recommendations}")