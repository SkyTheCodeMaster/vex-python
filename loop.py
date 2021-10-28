def loop(self,ms:int=50):
  def decorator(func):
    def wrapper():
      func()
      brain.timer.event(wrapper,ms)
    wrapper()
    return wrapper
  return decorator
