import string
import random
if __name__ == "__main__":
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    plen=int(input("enter the length of the password"))
    while True:
        random.shuffle(s)
        password=s[0:plen]
        print(password)

        if (any(char in s1 for char in password)and any(char in s2 for char in password) and any(char in s3 for char in password) and
                any(char in s4 for char in password) and any(char in s1 for char in password[0]) and (sum(char in s3 for char in password)>=4)):
            break


    print("".join(password))