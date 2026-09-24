from dataclasses import dataclass, asdict


@dataclass
class Expense:
    id: int
    amount: float
    category: str
    note: str = ""

    def __post_init__(self):
        if isinstance(self.amount, bool) or not isinstance(self.amount, (int, float)):
            raise ValueError("amount must be a number")
        if self.amount < 0:
            raise ValueError("amount must be >= 0")
        if not str(self.category).strip():
            raise ValueError("category must be a non-empty string")
        self.amount = float(self.amount)
        self.category = self.category.strip().lower()
        self.note = self.note.strip()

    def to_dict(self):
        return asdict(self)


def make_expense(expenses, **fields):
    # print("make_expense:::", expenses)
    # print("fields:::", fields)
    next_id = max((i.id for i in expenses), default=0) + 1
    return Expense(
        id=fields.get("id", next_id),
        amount=fields["amount"],
        category=fields["category"],
        note=fields.get("note", ""),
    )


def filter_by_category(expenses, category):
    wanted = category.strip().lower()
    return [i for i in expenses if i.category == wanted]


def total_amount(expenses, category=None):
    chosen = expenses if category is None else filter_by_category(expenses, category)
    return sum(i.amount for i in chosen)


def delete_expense(expenses, expense_id):
    kept = [i for i in expenses if i.id != expense_id]
    if len(kept) == len(expenses):
        raise ValueError(f"Expense with id {expense_id} not found")
    return kept
