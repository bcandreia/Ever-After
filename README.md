# Ever-After

A simple command-line wedding planning app.

## Features
- Maintain a guest list
- Track tasks on a wedding checklist
- Record vendors with individual budgets and view total cost

## Usage
Examples below assume a Python interpreter is available.

```bash
# Guests
python -m wedding_planner guest add "Alice"
python -m wedding_planner guest list

# Checklist
python -m wedding_planner task add "Book venue"
python -m wedding_planner task done "Book venue"
python -m wedding_planner task list

# Vendors and budget
python -m wedding_planner vendor add "Catering" 1500
python -m wedding_planner vendor list
python -m wedding_planner vendor total
```

State is persisted to `planner.json` in the repository root.
