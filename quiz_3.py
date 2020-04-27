# Code a program that generates passwords in each sites

# ex) http://google.com 
# Rule 1) exclude http://
# Rule 2) delete a whole part after the first encountering dot(.)
# Rule 3) Among the remaining characters, first 3-digit + no.of characters + no.of "O" in characters + "!"
# ex) the generated PW: goo62!

url = "http://google.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + "!"
print("The password for {0} is {1}".format(url, password))