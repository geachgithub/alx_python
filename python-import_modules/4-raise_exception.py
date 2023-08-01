
def raise_exception():
    a = 1 / 'b'
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")