#Given sphere_radius and pi, compute the volume of a sphere and assign sphere_volume with the volume. Volume of sphere = (4.0 #/ 3.0) π r3
#
#Sample output with input: 1.0
#
#Sphere volume: 4.19

pi = 3.14159
sphere_volume = 0.0

sphere_radius = float(input())

''' Your solution goes here '''
sphere_volume = (((4.0/3.0) * 3.14159) * 1 ** 3)

print('Sphere volume: {:.2f}'.format(sphere_volume))