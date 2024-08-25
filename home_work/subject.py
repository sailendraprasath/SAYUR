subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))


if (subject1 > 75 and subject2 > 75) or (subject1 > 75 and subject3 > 75) or (subject2 > 75 and subject3 > 75):
    print("Pass")
    print("Subjects with marks greater than 75:")
    if subject1 > 75:
        print(f"Subject 1 is {subject1}")
    if subject2 > 75:
        print(f"Subject 2 is {subject2}")
    if subject3 > 75:
        print(f"Subject 3 is {subject3}")
elif subject1 > 60 and subject2 > 60 and subject3 > 60:
    print(f"you are pass and your mark is Subject1 {subject1}, Subject2 {subject2}, subject3 {subject3}")
elif subject1 == 100:
    print("Pass")
    print("Scored 100 in Subject 1")
elif subject2 == 100:
    print("Pass")
    print("Scored 100 in Subject 2")
elif subject3 == 100:
    print("Pass")
    print("Scored 100 in Subject 3")
else:
    print("Fail")