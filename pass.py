#password strength test
import re
def check_password_strength(password):
    score = 0

    if len(password)>=8:
        score +=1
    if re.search("[a-z]",password):
        score+=1
    if re.search("[A-Z]",password):
        score+=1
    if re.search("[0-9]",password):
        score+=1
    if re.search("[!@#$%^&*]",password):
        score+=1
        
    if score <=2:
     return "weak"
    if 3<=score<4:
     return "medium"
    else:
     return "strong" 

password = input ("enter your password : ")
result =check_password_strength(password)

print("password strength : ",result)