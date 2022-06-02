class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def pechat(prod: point):
    print(f"1 - {prod.x}, 2 - {prod.y}")

def vvod():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    p = point(x, y)
    return p
pechat(vvod())
