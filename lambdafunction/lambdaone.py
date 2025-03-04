import random

def random_number_lambda(event, context):
    """
    A Lambda function that returns a random number between 1 and 100
    """
    random_number = random.randint(1, 100)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'random_number': random_number,
            'event': event
        })
    }
