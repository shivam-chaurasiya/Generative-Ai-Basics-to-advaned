employee_type = "Part-time"

def employee():
    def salary():
        global employee_type
        employee_type = "Full-time"
    salary()

employee()
print("Final employee type:", employee_type)