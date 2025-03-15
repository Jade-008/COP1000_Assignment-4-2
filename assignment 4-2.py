#this program calculates an employee productivity bonus and prints the employees name and bonus.

#inputs
employeeName= (input("Enter the employee's name: "))
numShifts= int(input("Enter the number of shifts: "))
numTransactions= int(input("Enter the number of transactions: "))
transactionValue= float(input("Enter transaction dollar value: "))

#calculate the productivity score
productivityScore = (transactionValue / numTransactions) / numShifts

#this function defines the bonus based on the productivity score and returns the bonus amount
def define_bonus(productivityScore):
    if productivityScore >= 200:
       return ("$200.00")
    else:  
        if productivityScore >= 70 and productivityScore <= 199:
            return("$100.00")
        else:
            if productivityScore >= 31 and productivityScore <= 69:
                return("$75.00")
            else:
                if productivityScore <= 30:
                    return("$50.00")  
        
#outputs
print("Employee Name:", employeeName)
print("Employee Bonus = ", define_bonus(productivityScore))