from wedding_planner import WeddingPlanner


def test_add_guest(tmp_path):
    data_file = tmp_path / "data.json"
    planner = WeddingPlanner(str(data_file))
    planner.add_guest("Alice")
    planner.add_guest("Bob")
    assert planner.list_guests() == ["Alice", "Bob"]


def test_checklist(tmp_path):
    planner = WeddingPlanner(str(tmp_path / "data.json"))
    planner.add_task("Book venue")
    planner.mark_task_done("Book venue")
    tasks = planner.list_tasks()
    assert tasks[0]["task"] == "Book venue"
    assert tasks[0]["done"] is True


def test_budget(tmp_path):
    planner = WeddingPlanner(str(tmp_path / "data.json"))
    planner.add_vendor("Catering", 1500)
    planner.add_vendor("Flowers", 500)
    assert planner.total_budget() == 2000
