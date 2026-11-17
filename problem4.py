from json import load
from statistics import mean

with open("students.json") as f:
    data = load(f)
    
best = max(data, key=lambda student : student['grade'])
worst = min(data, key=lambda student : student['grade'])


grades = [student['grade'] for student in data]

avg = round(mean(grades), 2)
print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {avg}")
