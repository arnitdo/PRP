userAge = int(input("Enter age : "))
if (userAge < 18):
    print("You are a minor (under 18)")
else:
    print("You are a major (over 18)")


userGrade = int(input("Enter marks : "))
if userGrade < 35:
    print("You failed! Try again next time!")
elif 35 < userGrade < 70:
    print("You did well!")
else:
    print("Passed with distinction")

