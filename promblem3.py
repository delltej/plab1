# variable define
penny_value=1
nikle_value=5
dime_value=10
quater_value=25
pennies_in_dollar=100

penny_value = int(input("please enter the value of pennies:"))
nikle_value = int(input("please enter the value of nikles:"))
dime_value = int(input("please enter the value of dimes:"))
quater_value = int(input("please enter the value of quaters:"))

TotalMoney = penny_value + nikle_value + dime_value + quater_value

if TotalMoney == 100:
    print("congratulations! the amount you enter excatly one dollar! you win the game!")
else:
    if TotalMoney< 100:
        print( "sorry,the amount you enter less than one dollar .")
    elif TotalMoney < 100:
              print("sorry,the amount you enter less than one dollar .")


