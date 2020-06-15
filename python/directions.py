import sys, webbrowser

url = 'https://www.google.com/maps/dir'

if len(sys.argv) > 1:
	query = ' '.join(sys.argv[1:])
	query = query.replace('from','/',1)
	query = query.replace('to','/',1)
	webbrowser.open(url+query)