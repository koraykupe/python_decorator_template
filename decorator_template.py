from functools import wraps

def decorator_name(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    # Do something before calling the decorated function
    return func(*args, **kwargs)
return wrapper
