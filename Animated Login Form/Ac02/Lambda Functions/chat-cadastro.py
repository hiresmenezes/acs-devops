import json

def lambda_handler(event, context):   
    response = {}
    response["statusCode"]=301
    response["headers"]={
        'Location':'https://chat-mesa-de-bar.s3.amazonaws.com/pag_2-cadastro.html',
        'Access-Control-Allow-Origin': "*"
    }
    data = {}
    #response["body"]=json.dumps(data)
    return response
