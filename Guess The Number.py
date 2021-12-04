# Function that read a list of numbers from the user and remove the largest and smallest values (outliers) from it.
def remove_outliers(data,number_of_outliers):
    rearranged_list=sorted(data)
#remove the largest number
    for i in range(number_of_outliers):
        rearranged_list.pop()
# remove the smallest number
    for i in range(number_of_outliers):
        rearranged_list.pop(0)
    return rearranged_list

# Function that check if the number is a perfect number, as well as whether it is positive or negative.
negative=[]
positive=[]
perfect_number=[]
def compare(b):
    total = 0
    for i in range(1,b):
        if b % i == 0:
            total += i
    if total==b and b > 0:
        print(f"Sorry, {b} is too high. Please guess again.")
        positive.append(b)
        perfect_number.append(b)
    elif total==b and b < 0:
        print(f"Sorry, {b} is too low. Please guess again.")
        negative.append(b)
        perfect_number.append(b)
    elif total!=b and b > 0:
        print(f"Sorry, {b} is too high. Please guess again.")
        positive.append(b)
    elif total!=b and b < 0:
        print(f"Sorry, {b} is too low. Please guess again.")
        negative.append(b)

#function to determine the divisor of an integer
def factor(z):
    divisor=[]
    for i in range(1,z):
        if z % i == 0:
            divisor.append(i)
    return sorted(divisor)

def main():
    number_list=[]
    number_from_user=""
    # only give the user 10 chances to guess
    guess_count = 0
    guess_limit = 10
    out_of_guesses = False
    # Continue reading values until the user enters 0. In other words, 0 is the assigned secret number that the user needs to enter.
    while number_from_user!=0 and not(out_of_guesses):
        if guess_count < guess_limit:
            number_from_user = int(input("Enter a number (Hint: range between -10 and 30): "))
            number_list.append(number_from_user)
            compare(number_from_user)
            guess_count+=1
        else:
            out_of_guesses=True
    if out_of_guesses:
        print("You Lose The Game!")
    else:
        print("You Win The Game!")
    # analysis using def compare() // positive, negative or a perfect number
    print("Without the outliers removed, the sorted number list is {}.".format(sorted(number_list)))
    if len(negative) == 0:
        print(f"You have not entered any negative number.")
    else:
        print(f"You have entered {len(negative)} negative number(s). They are {sorted(negative)}.")
    if len(positive) == 0:
        print(f"You have not entered any positive number.")
    else:
        print(f"You have entered {len(positive)} positive number(s), ie {sorted(positive)}.")
    if len(perfect_number) == 0:
        print(f"You have not entered any perfect number. A perfect number is the positive integer that is equal to the sum of its positive divisors, excluding the number itself. \nEg. the divisor for the 6 is {factor(6)}, and the sum of these divisors is equivalent to 6 itself.")
    else:
        print(f"You have entered {len(perfect_number)} perfect number(s). They are {sorted(perfect_number)}. \nA perfect number is the positive integer that is equal to the sum of its positive divisors, excluding the number itself. \nEg. the divisor for the {sorted(perfect_number)[-1]} is {factor(sorted(perfect_number)[-1])}, and the sum of these divisors is equivalent to {sorted(perfect_number)[-1]} itself.")
    # calculate the average of the numbers entered and compare average with of them
    average=sum(number_list)/len(number_list)
    print(f"You have entered {len(number_list)} number(s) and the average of the numbers that you entered is {average}.")
    above_average = []
    below_average = []
    for num in number_list:
        if num >=average:
            above_average.append(num)
        else:
            below_average.append(num)
    print(f"You have entered {len(above_average)} number(s) that are above or equal to the average, ie.{sorted(above_average)}.")
    print(f"You have entered {len(below_average)} number(s) that are below the average, ie.{sorted(below_average)}.")
    if len(number_list)<3 and number_from_user==0:
        if len(number_list)==1:
            print("Awesome, you just won the game with only one trial. There is no outliers. Once again, congratulation for winning the game1")
        elif len(number_list)==2:
            if number_list[0]>number_list[1]:
                print(f"Amazing, you just won the game with only two trials. {number_list[0]} is greater than {number_list[1]}.")
            else:
                print(f"Amazing, you just won the game with only two trials. {number_list[0]} is lower than {number_list[1]}.")
    # Display the list with the outliers removed, followed by the original list.
    else:
        print("With the outliers removed, the sorted number list is {}.".format(remove_outliers(number_list, 1)))
        print(f"The outliers removed were {sorted(number_list)[0]} and {sorted(number_list)[-1]}. {sorted(number_list)[0]} is the smallest number entered while {sorted(number_list)[-1]} is the largest number entered.")
main()

