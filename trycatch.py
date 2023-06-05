
def tax():
    income=int(input("enter your income"))
    try:

        #if income is lower than the 2.5l then no tax
        if income<=250000:
            tax=0
        #if income higher than 2.5l and lower than 5l then 5% tax
        elif income>=500000:
            tax=(income-250000)*0.05
        else:
            tax=(income-1000000)*0.25

    # if user enter the string then rise the error
    except:
        print("print valid Amount")
    print(tax)
tax()