# import math

# items = int(input('Enter the number of items: '))
# per_box = int(input('Enter the number of items per box: '))

# boxes = items / per_box

# boxes_needed = math.ceil(boxes)

# print(f'For {items} items, packing {per_box} items in each box, you will need {boxes_needed} boxes.')


def area_circle(radius):
    """Compute and return the area of a circle."""
    area = math.pi * radius ** 2
    return area