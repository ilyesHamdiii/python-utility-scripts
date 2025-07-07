import string 
import random
characters=list(string.ascii_letters+string.digits+"#*$/.")
def generate_password():
    password_length=int(input(" how long you would like the password "))
    random.shuffle(characters)
    password=[]
    for x in range(password_length):
        password.append(random.choice(characters))
    password="".join(password)
    print(f"your password is {password}")
if __name__=="__main__":
    generate_password()

    