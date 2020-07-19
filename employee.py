EmployeeId          = input("plese enter employee id : ")
EmployeeName        = input("plese enter employee name : ")
EmployeeDepartment  = input("plese enter employee department : ")
EmployeeDesignation = input("plese enter employee designation : ")
EmployeeSalary      = int(input("plese enter employee salary : "))

EmployeeSalary = EmployeeSalary + 3000

print("added 3000 as  travelling allowance ",EmployeeSalary)

EmployeeSalary = EmployeeSalary + 15000


print("added 15000 as  Bonus ",EmployeeSalary)


EmployeeSalary = EmployeeSalary - (EmployeeSalary*5/100)

print(" 5 percent proffesional tax substracted from salary ",EmployeeSalary)


EmployeeSalary = EmployeeSalary + (EmployeeSalary*15/100)

print(" 15 percent pf added to salary : ",EmployeeSalary)




print(" Employee ID : ",EmployeeId)
print(" Employee Name : ",EmployeeName)
print(" Employee Department : ",EmployeeDepartment)
print(" Employee Designation : ",EmployeeDesignation)
print(" Total Salary is : ",EmployeeSalary)

input("Press enter to exit ;)")




