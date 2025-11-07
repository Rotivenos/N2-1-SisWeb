import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Recommendations')

def lambda_handler(event, context):

    user_id = event['Records'][0]['body']

    try:
        response = table.get_item(Key={'userId': user_id})

        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps('Usuário não encontrado.')
            }

        user_data = response['Item']
        recommendations = generate_recommendations(user_data)

        return {
            'statusCode': 200,
            'body': json.dumps(recommendations)
        }

    except Exception as e:
        print(f"Erro ao consultar o DynamoDB: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao processar a requisição.')
        }

def generate_recommendations(user_data):
    products = user_data.get('purchasedProducts', [])
    recommendations = []

    for product in products:
        recommendations.append({
            'productId': product['id'],
            'productName': f"Recomendação para {product['name']}"
        })

    return recommendations
