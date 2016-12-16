
class WSGIMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, custom_start_response)


class MyHeaderMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        def custom_start_response(status, headers):
            headers.append(('X-My-Header', "Made by MyHeaderMiddleware"))
            return start_response(status, headers)

        return self.app(environ, custom_start_response)
