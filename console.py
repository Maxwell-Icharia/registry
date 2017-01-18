def registry():
	name = raw_input('What is your name ?')
	if name != str:
		return "Invalid input, try again! " + name
	else:
		number = raw_input(str('What is your mobile phone number?#eg +254736253413 '))
		if len(number) != 13:
			return "Invalid input, try agin! " + number


from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

username = "MaxwellIcharia"
apikey   = "74db14cf1d848056e31b1549c18efa2b6ad6a89b63104ab5ae14c92739b05a1b"


to      = " number"

message = "Hey there " + name + " you are now registered."

gateway = AfricasTalkingGateway(username, apikey)

try:
    
    results = gateway.sendMessage(to, message)
    
    for recipient in results:
        print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                            recipient['status'],
                                                            recipient['messageId'],
                                                            recipient['cost'])
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while sending: %s' % str(e)

