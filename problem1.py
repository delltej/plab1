#given values
cleaning_rate=60
cavity_filling=200
x_ray=100
#when the bill of a patient is more than $200, give the user 5% discount
disc1=0.05
# more than $300, give a 10% discount
disc2=0.1
tax_rate=0.15
#getting the inputs 
name=input("enter the patient's name :")
cleaning= input("was cleaning performed ?")
cavity=input("was cavity filling performed ?")
xray=input("was X ray  performed ?")
#defining the function
def calculate(name, cleaning, cavity, xray):
    print("the patients name is :",name) 
    total=0
    # for cleaning
    if(cleaning=="y"):
        total=total+cleaning_rate
        print("the cleaning was also done")
    else:
        print("cleaning not done")
        #for cavity
    
    if(cavity=="y"):
        total=total+cavity_filling
        print("the cavity filling was done")
    else:
        print("cavity feeling was not done ")
        
    if(xray=="y"):
        total=total+x_ray
        print("x ray was done")
    else:
        print(" x ray was not done ")
        