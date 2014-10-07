#Jarod Pierre Murton
#Code to work out the volume of a swimming pool
#16/9/14

length = print("Please enter the length of the swimming pool: ")
width = print("Please enter the width of the swimming pool: ")
shallow_height = print("Please enter the depth of the shallow end: ")
deep_height = print("Please enter the depth of the deep end: ")

cuboid = length * width * shallow_height

prism = (length * width * deep_height) / 2

volume = cuboid + prism

print(volume)
