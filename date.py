import datetime
days = -1

order = datetime.datetime.now()

print (datetime.datetime.now() < (datetime.datetime.now() - datetime.timedelta(days=days)))