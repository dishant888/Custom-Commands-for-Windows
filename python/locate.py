import sys, webbrowser

url = 'https://www.google.com/maps/search/'

if len(sys.argv) > 1:
	# get address from cmd
	address = ' '.join(sys.argv[1:])
	webbrowser.open(url+address)