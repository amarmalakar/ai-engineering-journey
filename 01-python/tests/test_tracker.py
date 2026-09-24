import asyncio

import pytest

from expense_tracker.models import delete_expense, make_expense, total_amount
from expense_tracker.storage import load_expenses, load_expenses_async, save_expenses


def test_add_filter_and_total(tmp_path):
    path = tmp_path / "expenses.json"
    expenses = []
    expenses.append(make_expense(expenses, amount=10, category="Food", note="a"))
    expenses.append(make_expense(expenses, amount=5, category="travel"))
    save_expenses(expenses, path)

    loaded = load_expenses(path)
    assert [item.id for item in loaded] == [1, 2]
    assert total_amount(loaded, "food") == 10
    assert total_amount(loaded) == 15


def test_delete_missing_id():
    item = make_expense([], amount=10, category="food")
    with pytest.raises(ValueError):
        delete_expense([item], 99)


def test_async_load(tmp_path):
    path = tmp_path / "expenses.json"
    save_expenses([make_expense([], amount=3, category="food")], path)
    loaded = asyncio.run(load_expenses_async(path))
    assert loaded[0].amount == 3
