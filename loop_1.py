# i = 1
# while i<=5 :
#     print('*'*i)
#     i=i+1
# print('done')    


secret_no = 9
i = 0

while i<3:
    guess = int(input("guess no."))
    i+=1
    if guess == secret_no:
        print("You won !!")
        break
else:
     print("you lost")   
    
    
   

         
    
    

    