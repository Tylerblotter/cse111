import math

def main():
    for i in range(12):
        r = radi[i]
        h = heights[i]

        se = compute_storage_efficiency(compute_volume(r, h), compute_surface_area(r,h))
        print(f'#{numbers[i]} {names[i]} {se:.02f}')

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

numbers = [1, 1, 2, 2.5, 3, 5, '6Z', '8Z', 10, 211, 300, 303]
names = ['Picnic', 'Tall', '','','Cylinder','','','short','','','','']
radi = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

main()