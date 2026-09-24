name = "lunch"
amount = 240.5
paid = True
people = 2

expense = {"category": "food", "amount": amount, "note": name}
record = (expense["category"], expense["amount"])
categories = {"food", "travel", "food"}

expenses = [
    {"category": "food", "amount": 240.5, "note": "lunch"},
    {"category": "travel", "amount": 80, "note": "metro"},
    {"category": "food", "amount": 50, "note": "tea"},
]

food = [i for i in expenses if i["category"] == "food"]
labels = {i["category"] for i in expenses}

# print(expense)
# print(record)
# print(categories)
print(food)
# print(labels)
