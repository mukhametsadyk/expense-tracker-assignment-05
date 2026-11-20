from tracker import ExpenseTracker


def test_add_and_total():
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 1500)
    tracker.add_expense("Transport", 500)

    assert len(tracker.expenses) == 2
    assert tracker.total_amount() == 2000.0


def test_total_by_category():
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 1200)
    tracker.add_expense("food", 800)
    tracker.add_expense("Books", 3000)

    assert tracker.total_by_category("Food") == 2000.0
    assert tracker.total_by_category("Books") == 3000.0


def test_remove_expense():
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 1000)
    tracker.add_expense("Coffee", 600)

    removed = tracker.remove_expense(0)
    assert removed["category"] == "Food"
    assert tracker.total_amount() == 600.0