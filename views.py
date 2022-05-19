from simba_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Content:
    def __call__(self, request):
        return '200 OK', render('content.html', date=request.get('date', None))


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', date=request.get('date', None))


class About:
    # {'method': 'GET', 'request_params': {'id': '1', 'category': '10'}}
    def __call__(self, request):
        # return '200 OK', render('about.html', date=request.get('date', None))
        return '200 OK', 'about'
