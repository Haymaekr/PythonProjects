from twilio.rest import Client 
 
account_sid = 'AC3152f22d5edf016029813dc1772a890d' 
auth_token = '8ee8c5f3a0d4c41256807d5ef6b0b4f9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12013409691',  
                              body='THIS actually works huh',      
                              to='+919480228566' 
                          ) 
 
print(message.sid)