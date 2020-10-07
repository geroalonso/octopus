from twilio.rest import Client
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

with open('whatever.txt','r') as nom:
     all_lines = nom.readlines()
     targets = {}
     for i in all_lines:
         l = i.split()
         if len(l) > 2:
             targets[l[0]] = l[1] + ' ' +  l[2]
         else:
             targets[l[0]] = l[1]

for i in targets:
    if targets[i] != '':
        content = 'Hello ' + targets[i]
    else:
        content = 'Hello'
    message = client.messages \
    .create(
    body = content,
    from_= '+12058097133',
    to = i
    )
