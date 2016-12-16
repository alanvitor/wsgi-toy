def application(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return ["Toy Web Server with an Application\n"]