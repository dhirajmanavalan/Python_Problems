marks = []

for i in range(5):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

avg = sum(marks) / 5

if avg >= 90:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Average:", avg)
print("Grade:", grade)

# 📊 4. Student Grade Analyzer