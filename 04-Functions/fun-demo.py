def triangle_area_print(a, h):
    print(a * h / 2)

area = triangle_area_print(10, 10)  # output: 50
print("area:", area)  # area: None   why?

def triangle_area(a, h):
    return a * h / 2

area = triangle_area(10, 10)
print("area:", area)  # area: 50.0


def hello():
    hello_name("World")

def hello_name(name="World"):
    print(f"Hello {name}")

    