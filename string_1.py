# course = "siddique"
# print('adsd' in course)

# is_hot = True
# if is_hot:
#     print('it is a hot day')
# print('Enjoy your day')    

weight = int(input('Enter weight? '))
unit =  input('Enter L or K')
if unit.upper() == "L":
    convert = weight*0.45
    print(f"you are {convert} kilos") 
else:
    convert = weight//0.45  
    print(f"you are {convert} kilos") 
      
