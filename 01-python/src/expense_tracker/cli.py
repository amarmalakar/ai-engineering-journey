import argparse
import asyncio

from expense_tracker.models import (
    delete_expense,
    filter_by_category,
    make_expense,
    total_amount,
)
from expense_tracker.storage import default_path, load_expenses_async, save_expenses


def build_parser():
    parser = argparse.ArgumentParser(description="Track expenses")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="add an expense")
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--note", default="")

    delete = commands.add_parser("delete", help="delete an expense by id")
    delete.add_argument("--id", type=int, required=True)

    listing = commands.add_parser("list", help="list expenses")
    listing.add_argument("--category")

    total = commands.add_parser("total", help="sum expenses")
    total.add_argument("--category")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    path = default_path()
    expenses = asyncio.run(load_expenses_async(path))

    if args.command == "add":
        created = make_expense(
            expenses,
            amount=args.amount,
            category=args.category,
            note=args.note,
        )
        expenses.append(created)
        save_expenses(expenses, path)
        print(f"added #{created.id} {created.category} {created.amount:.2f}")
        return

    if args.command == "delete":
        expenses = delete_expense(expenses, args.id)
        save_expenses(expenses, path)
        print(f"deleted #{args.id}")
        return

    if args.command == "list":
        rows = (
            filter_by_category(expenses, args.category) if args.category else expenses
        )
        if not rows:
            print("no expenses")
            return
        for item in rows:
            print(f"#{item.id}  {item.amount:.2f}  {item.category}  {item.note}")
        return

    label = args.category or "all"
    print(f"{label}: {total_amount(expenses, args.category):.2f}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        raise SystemExit(f"error: {exc}")
