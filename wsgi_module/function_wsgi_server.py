from wsgiref.simple_server import make_server


def web_app(environ, start_response):
    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = str.encode('\n'.join(response_body))

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]


with make_server('', 8051, web_app) as server:
    server.serve_forever()
