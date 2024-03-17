studetScore={
    "akash" : 30,
    "siam" : 80,
    "tuhin" : 90,
    "moni" : 99,
}
print(studetScore)

newStudent="akash"
newScore=100

if newStudent in studetScore:
    studetScore[newStudent]

studetScore[newStudent]=newScore

for student, score in studetScore.items():
    print(f"{student} : {score}")
