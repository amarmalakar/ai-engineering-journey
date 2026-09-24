import asyncio
import json
import os
from pathlib import Path

from expense_tracker.models import Expense


def default_path():
    return Path(os.environ.get("EXPENSE_FILE", "data/expenses.json"))


def load_expenses(path=None):
    path = path or default_path()
    if not path.exists():
        return []
    try:
        raw = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}") from exc
    if not isinstance(raw, list):
        raise ValueError("expense file must be a list")
    return [Expense(**item) for item in raw]


def save_expenses(expenses, path=None):
    path = path or default_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [item.to_dict() for item in expenses]
    path.write_text(json.dumps(payload, indent=2) + "\n")


async def load_expenses_async(path=None):
    return await asyncio.to_thread(load_expenses, path)
