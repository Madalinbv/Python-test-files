# ipaddress = input("please inpout an IP address: ")
# print(ipaddress.count("."))
parrot_list=["non pinin","no more", "a stiff", "bereft of live"]

parrot_list.append("norweian blue")
for state in parrot_list:
    print("this parrot is " + state)

even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = even + odd
numbers_in_order = sorted(numbers)
#numbers.sort()
print(numbers_in_order)
if numbers==numbers_in_order:
    print("the lists are equal")
else:
    print("the lists are not equal as number is: {} \nand numbers_in_order"
          " is: {}".format(numbers,numbers_in_order))

if numbers_in_order == sorted(numbers):
    print("the lists are equal")
else:
    print("the lists are not equal as number is: {} \nand numbers_in_order"
          " is: {}".format(numbers,numbers_in_order))