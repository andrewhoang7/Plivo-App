#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import plivo
client = plivo.RestClient(auth_id='MAMJDMZGIYNMMZNWU0MJ',auth_token='Y2IwNjczNTdiYjU3MTcyNDZjNDAwMjM2ZjhmZjI2')
response = client.messages.list(
    limit=20,
    offset=0,
    )
print(response)
#prints only the message_uuid
print(response.message_uuid)


