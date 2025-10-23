from datetime import datetime
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Please provide the name of an existing contact."
        except IndexError:
            return "Invalid command. Please provide a valid contact name."

    return inner