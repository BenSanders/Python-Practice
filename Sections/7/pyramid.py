def calc_base_area(base_length, base_width):
   return base_length * base_width

''' Your solution goes here '''
def calc_pyramid_volume(base_length,base_width,pyramid_height):
    volume = calc_base_area(base_length,base_width) * pyramid_height * 1/3
    return volume

length = float(input())
width = float(input())
height = float(input())
print('Volume for', length, width, height, "is:", calc_pyramid_volume(length, width, height))