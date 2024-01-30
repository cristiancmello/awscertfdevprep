import logging

import boto3

boto3.set_stream_logger("boto3.resources", logging.DEBUG)
boto3.set_stream_logger("botocore", logging.DEBUG)

# Configurando inicializacao de client com hardcoding de AWS Credentials e Region
# Não recomendado por: exposicao de credentials num repositorio publico
# polly = boto3.client(
#     'polly',
#     region_name='us-east-1',
#     aws_access_key_id='AKIA...',
#     aws_secret_access_key='ZON6VF...'
# )

# Configurando inicializaco de client com AWS Credentials and Region carregado de ~/.aws/credentials e ~/.aws/config
polly = boto3.client('polly')

result = polly.synthesize_speech(Text='Hello World', OutputFormat='mp3', VoiceId='Aditi')

audio = result['AudioStream'].read()
with open('helloworld.mp3', 'wb') as file:
    file.write(audio)
