from time import time


# Structural pattern - Decorator
class AppRoute:

    def __init__(self, routes, url):
        """Save values of parameters"""
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        """Decorator themselves"""
        self.routes[self.url] = cls()


# Structural pattern - Decorator
class Debug:

    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        """Decorator themselves"""

        # This is support function for decorated every single class method
        def timeit(method):
            # For decorating timeit with decorator class wrapper for each method
            def timed(*args, **kwargs):
                time_start = time()
                result = method(*args, **kwargs)
                time_end = time()
                delta = time_start - time_end

                print(f'debug -> {self.name} was executed {delta:2.2f} ms')

                return result

            return timed

        return timeit(cls)

# func()
# obj = MyClass()
# obj()
