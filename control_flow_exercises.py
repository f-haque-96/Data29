
user_prompt = True

while user_prompt:
    age = input("what is your age? ")
    if age.isdigit():
        if int(age)<117:
            break
            #user_prompt = False
        else:
            print ("incorret age")
    else:
        print("please provide your age in digits")

print (f"your age is: {age}")