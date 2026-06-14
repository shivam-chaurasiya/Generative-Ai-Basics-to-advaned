tel = {'jack': 4098, 'sape': 4139}

tel['abs'] = 8902

print(tel)

student_stream = dict(science=40, arts= 20, commerce= 45)

student_stream["maths"] = 20
student_stream["bio"] = 20

print(f"students stream like that : {student_stream}")

print(f"listing all the key like that: {list(student_stream)}")

print(f"sorted the key like that: {sorted(student_stream)}")

print(f"membership testing we can do in this manner: {"maths" in student_stream}")