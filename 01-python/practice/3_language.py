import asyncio

expenses = [
    {"category": "food", "amount": 240.5, "note": "lunch"},
    {"category": "travel", "amount": 80, "note": "metro"},
    {"category": "food", "amount": 50, "note": "tea"},
]
# print(expenses)


class Expense:
    def __init__(self, amount, category, note=""):
        # print("Initializing Expense:::", self)
        # print(amount, category, note)
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("amount must be a number")
        if amount < 0:
            raise ValueError("amount must be >= 0")
        self.amount = float(amount)
        self.category = category.strip().lower()
        self.note = note

def make_expense(amount, category, **extra):
    return Expense(amount, category, extra.get("note", ""))

async def preview(items):
    await asyncio.sleep(0)
    return [item["category"] for item in items]


try:
    bad = Expense("twelve", "food")
except ValueError as exc:
    print("caught:", exc)

lunch = make_expense(240.5, "Food", note="lunch")
print(lunch.amount, lunch.category, lunch.note)
print(asyncio.run(preview(expenses)))