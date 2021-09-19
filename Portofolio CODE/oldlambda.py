import json
import boto3

def lambda_handler(event, context):
  print(str(event))
  try:
    httpmethod = event['requestContext']['http']['method']
    if httpmethod == 'GET':
        email = event['queryStringParameters']['Email']
        name = event['queryStringParameters']['Name']
        subject = event['queryStringParameters']['Subject']
        message = event['queryStringParameters']['Message']
        data = '''
            <br>
        ''' + "Sender's email is: " + email + "\n" + message
        body = f"<html>Hello from mylambda! EMAIL SENT!<p>email={email}<p>name={name}<p>subject={subject}<p>message={message}</html>"
        client = boto3.client('ses')
        payload = { "Subject": { "Data": subject }, "Body": { "Html": { "Data" : data } } }
        resp = client.send_email(Source = "kaydrien@gmail.com", Destination = { "ToAddresses": ["kaydrien.johnson@gmail.com"] }, Message = payload )
        print(str(resp))
  except:
    pass
  body = 'Hello from Lambda! key1=abc and key2=123'
  return {
        'statusCode': 200,
        'body': json.dumps(body),
        'headers': { 'Content-Type': 'text/html', 'Access-Control-Allow-Origin': '*' }
  }
