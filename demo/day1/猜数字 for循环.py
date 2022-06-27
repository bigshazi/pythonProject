# Author:hufei

age_of_oldboy = 56
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("you got it")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!")

else:
    print("输入次数太多了")
