Marks = {
    "DEEP" : 500,
    "PRIYA": 600,
    "REETA" : 400,
    0:"DEEPANSHI"
}
#print(Marks.items())
#print(Marks.keys())
Marks.update({"DEEP": 80, "Renuka" :100})
print(Marks)
print(Marks.get("DEEP2"))
#print(Marks["DEEP2"]) #RETURN ERROR
print(Marks.clear())
print(Marks)