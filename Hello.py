from random import *
string = input("Input \"shutdownAll\" command for emergency!!! : ")
if(string=='shutdownAll'):
    company = input("company name ex)SEMA : ")
    shutdownpasswd = str(randint(100000, 999999)) # random key generate
    print("Are you sure shutdown all system of " + company + "? then please input : \"Shutdown" + company + shutdownpasswd + "\"")
    shutdownkey = input()
    if(shutdownkey == "Shutdown"+company+shutdownpasswd): # check key input is correct
        print("shutdown started")   
        # run shutdown all ansible command
    else:
        print("shutdown canceled.")
else:
    print("shutdown canceled.")