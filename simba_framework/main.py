class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:
    """Class Framework - base of framework"""

    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        # Getting the address to which the jump was made
        path = environ['PATH_INFO']

        # Adding closing slash
        if not path.endswith('/'):
            path = f'{path}/'

        # Finding controller (page controller pattern)
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()
        request = {}
        # Adding elements to request (front controller pattern)
        for front in self.fronts_lst:
            front(request)
        # Starting controller with request object
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
