credit_card_number = input("What is your credit card number: ")
#American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers
if len(credit_card_number) == 15:
    print("American Express")
elif len(credit_card_number) == 13:
    print("Visa")
elif len(credit_card_number) == 16:
    print("Visa or Mastercard")

two_digit = credit_card_number[0:2]
#American Express numbers start with 34 or 37;
if two_digit == ("34") or two_digit == ("36"):
    print("American Express")
#MasterCard numbers start with 51, 52, 53, 54, or 55 
elif two_digit == ("51") or two_digit == ("52") or two_digit == ("53") or two_digit == ("54") or two_digit == ("55"):
    print("Mastercard")
#Visa numbers start with 4.
elif two_digit[0:1] == ("4"):
    print("Visa") 

#Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
cc_arr = list(credit_card_number)
index = len(cc_arr) - 2
sum_one = 0
while(index >= 0):
    num = int(cc_arr[index]) * 2
    num_list = map(int, str(num))
    for i in (num_list):
        sum_one = sum_one + i
    index = index - 2

index = len(cc_arr) - 1
sum_two = 0
while(index >= 0):
    sum_two = sum_two + int(cc_arr[index])
    index = index - 2
total_sum = sum_one + sum_two
#Add the sum to the sum of the digits that weren’t multiplied by 2.
if total_sum % 10 == 0:
    print("Valid")
else:
    print("Invalid")
#If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!