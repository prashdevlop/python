from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC135127d735fba2a5a137bee56fc4e903"
# Your Auth Token from twilio.com/console
auth_token  = "13f93e32775ea773561fa2c370e668c1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919687486775", 
    from_="+13097614504",
    body="Prashant from Python!")

print(message.sid)
