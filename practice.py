# temp = int(input("What is the temperature? "))
# if 90 <= temp:
#     print("hot. do not go outside")
# elif 65 <= temp and temp < 90:
#     print("get your jacket on")
# elif 32 < temp < 10:
#     print("put your coat on")
# else:
#     print("Too cold. do not goo outside")

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("Waiting number : {0}".format(waiting_no))

# starbucks = ["Iron man", "Tor", "I am Grut"]
# for customer in starbucks:
#     print("{0}, Coffee is ready".format(customer))

# customer = "Tor"
# index = 5
# while index >= 1:
#     print("{0}, Coffee is ready. We will call you {1} more times".format(customer, index))
#     index -=1
#     if index == 0:
#         print("Your coffee is not available") 

# customer = "Iron Man"
# person = "Unknown"
# while person != customer:
#     print("{0}, Your coffee is ready.".format(customer))
#     person = input("What is your name? ")

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("You're not supposed to attend the class. stand up number {0}".format(student))
        break
    print("{0}, Read your book".format(student))