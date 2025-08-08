import argparse
import json
import os
from typing import List, Dict


class WeddingPlanner:
    """Simple in-file wedding planner.

    Data is persisted to a JSON file so that successive CLI calls share
    the same state.  The file location can be customised for testing.
    """

    def __init__(self, data_file: str = "planner.json") -> None:
        self.data_file = data_file
        self.data = self._load()

    # ------------------------------------------------------------------
    # internal helpers
    def _load(self) -> Dict:
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as fh:
                return json.load(fh)
        return {"guests": [], "checklist": [], "vendors": {}}

    def _save(self) -> None:
        with open(self.data_file, "w", encoding="utf-8") as fh:
            json.dump(self.data, fh, indent=2, sort_keys=True)

    # ------------------------------------------------------------------
    # Guests
    def add_guest(self, name: str) -> None:
        if name not in self.data["guests"]:
            self.data["guests"].append(name)
            self._save()

    def remove_guest(self, name: str) -> None:
        if name in self.data["guests"]:
            self.data["guests"].remove(name)
            self._save()

    def list_guests(self) -> List[str]:
        return list(self.data["guests"])

    # ------------------------------------------------------------------
    # Checklist
    def add_task(self, description: str) -> None:
        self.data["checklist"].append({"task": description, "done": False})
        self._save()

    def mark_task_done(self, description: str) -> None:
        for task in self.data["checklist"]:
            if task["task"] == description:
                task["done"] = True
                self._save()
                break

    def list_tasks(self) -> List[Dict[str, bool]]:
        return list(self.data["checklist"])

    # ------------------------------------------------------------------
    # Vendors / Budget
    def add_vendor(self, name: str, budget: float) -> None:
        self.data["vendors"][name] = budget
        self._save()

    def remove_vendor(self, name: str) -> None:
        if name in self.data["vendors"]:
            del self.data["vendors"][name]
            self._save()

    def list_vendors(self) -> Dict[str, float]:
        return dict(self.data["vendors"])

    def total_budget(self) -> float:
        return float(sum(self.data["vendors"].values()))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Wedding planning CLI")
    sub = parser.add_subparsers(dest="category", required=True)

    # Guests
    guest_parser = sub.add_parser("guest", help="manage guests")
    guest_sub = guest_parser.add_subparsers(dest="action", required=True)
    guest_add = guest_sub.add_parser("add", help="add guest")
    guest_add.add_argument("name")
    guest_sub.add_parser("list", help="list guests")
    guest_rm = guest_sub.add_parser("remove", help="remove guest")
    guest_rm.add_argument("name")

    # Checklist
    task_parser = sub.add_parser("task", help="manage checklist")
    task_sub = task_parser.add_subparsers(dest="action", required=True)
    task_add = task_sub.add_parser("add", help="add task")
    task_add.add_argument("description")
    task_sub.add_parser("list", help="list tasks")
    task_done = task_sub.add_parser("done", help="mark task complete")
    task_done.add_argument("description")

    # Vendors
    vendor_parser = sub.add_parser("vendor", help="manage vendors")
    vendor_sub = vendor_parser.add_subparsers(dest="action", required=True)
    vendor_add = vendor_sub.add_parser("add", help="add vendor")
    vendor_add.add_argument("name")
    vendor_add.add_argument("budget", type=float)
    vendor_sub.add_parser("list", help="list vendors")
    vendor_rm = vendor_sub.add_parser("remove", help="remove vendor")
    vendor_rm.add_argument("name")
    vendor_sub.add_parser("total", help="show total budget")

    return parser


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    planner = WeddingPlanner()

    if args.category == "guest":
        if args.action == "add":
            planner.add_guest(args.name)
        elif args.action == "remove":
            planner.remove_guest(args.name)
        elif args.action == "list":
            for guest in planner.list_guests():
                print(guest)

    elif args.category == "task":
        if args.action == "add":
            planner.add_task(args.description)
        elif args.action == "done":
            planner.mark_task_done(args.description)
        elif args.action == "list":
            for task in planner.list_tasks():
                mark = "[x]" if task["done"] else "[ ]"
                print(f"{mark} {task['task']}")

    elif args.category == "vendor":
        if args.action == "add":
            planner.add_vendor(args.name, args.budget)
        elif args.action == "remove":
            planner.remove_vendor(args.name)
        elif args.action == "list":
            for name, budget in planner.list_vendors().items():
                print(f"{name}: ${budget:0.2f}")
        elif args.action == "total":
            print(f"Total budget: ${planner.total_budget():0.2f}")


if __name__ == "__main__":
    main()
