import boto3

client = boto3.client('dynamodb', region_name='CHANGE_ME')

try:

    resp = client.create_table(
        TableName='CHANGE_ME',
        KeySchema=[{
            'AttributeName': 'CHANGE_ME',
            'KeyType': 'HASH'
        }, {
            'AttributeName': 'phone',
            'KeyType': 'RANGE'
        }],
        AttributeDefinitions=[
            {
                'AttributeName': 'CHANGE_ME',
                'AttributeType': 'CHANGE_ME'  # S | N | B
            },
            {
                'AttributeName': 'CHANGE_ME',
                'AttributeType': 'CHANGE_ME'  # S | N | B
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        })
    print('Table created successfully!')
except Exception as e:
    print('Error!')
    print(e)
