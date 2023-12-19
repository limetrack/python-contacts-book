# -- Decorator for input error handling
def input_error(parentError = None):
    def error_handler(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, KeyError, IndexError, KeyboardInterrupt) as error:
                print(parentError if parentError else error) # Check
        return inner
    return error_handler

# -- Validations
class ValidationError(Exception):
    pass

# -- Decorator for validation handling
def validation_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as err:
            print(err)

    return inner
