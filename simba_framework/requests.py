# Get requests
class GetRequests:

    @staticmethod
    def parse_input_data(data):
        result = {}
        if data:
            # Divide parameters with &
            params = data.split('&')
            for item in params:
                # Divide key and value with =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        # Receive request parameters
        queri_string = environ['QUERY_STRING']
        # Convert parameters to dictionary
        request_params = GetRequests.parse_input_data(queri_string)
        return request_params

# Post requests
class PostRequests:

    @staticmethod
    def parse_input_data(data):
        result = {}
        if data:
            # Divide parameters with &
            params = data.split('&')
            for item in params:
                # Divide key and value with =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env):
        # Get body length
        content_length_data = env.get('CONTENT_LENGTH')
        # Convert to int
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)
        # Read data if there (env['wsgi.input'] -> <class '_io.BufferedReader'>), start reading mode

        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data):
        result = {}
        if data:
            # Decorating data
            data_str = data.decode(encoding='utf-8')
            print(f'String after decoding - {data_str}')
            # Collecting them to dictionary
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        # Receiving data
        data = self.get_wsgi_input_data(environ)
        # Converting data to dictionary
        data = self.parse_wsgi_input_data(data)
        return data
