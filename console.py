from urllib2 import Request, urlopen, URLError

name = Request('http://nameberry.com/popular_names')

g = raw_input("What is your first name? ")

try:
	response = urlopen(name)
	common = response.read()
	if g in common:
		print 'The name is common'
	else:
		print 'The name is not common'
except URLError, e:
    print 'No Common name, error!:', e