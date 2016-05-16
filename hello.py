def application(environ,start_response):
	start_response=('200 OK',[('Content-Type','text/plain')])
	body=environ['QUERY_STRING'].replace('&','\n')
	return body
