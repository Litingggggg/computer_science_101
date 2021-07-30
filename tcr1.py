'''
import math

length = 8
small_diameter = 6
large_diameter = 7

volume=((math.pi*length)/4)*(small_diameter+(5/8)*(large_diameter-small_diameter))**2
volume=round(volume,2)
bottles=volume/1.5
bottles=math.floor(bottles)
print("The volume of the barrel is approximately %s litre(s)" %(volume))
print("It is possible to fill %s 1.5 litre bottles" %(bottles))

'''

number = 178

tens_digit=number//10
units_digit=number%10

print("The reversed number is: %s%s"%(units_digit,tens_digit))
