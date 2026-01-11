# kaggle-santa-tour-2019

🎅 Santa’s Workshop Tour 2019 — Greedy + Local Search Solver

📌 Overview

This project solves the Santa’s Workshop Tour 2019 Kaggle challenge.
The goal is to assign 5,000 families to 100 days while minimizing:

Preference penalties (assigning families to less-preferred days)

Daily attendance penalties (keeping 125–300 visitors per day)

Accounting penalties (smooth day-to-day attendance)

The final output is a valid Kaggle submission file mapping families to their optimized visiting days.



🧠 Solution Approach

This solver uses a two-stage optimization strategy:


1️⃣ Greedy Capacity-Aware Assignment

Families are sorted by size in descending order, as large families are harder to schedule.

Each family is assigned to their best available preferred day (choice_0 → choice_9) without exceeding daily capacity.

Families that remain unassigned are then placed in days with low occupancy to ensure all days meet minimum and maximum limits.

This produces a strong initial solution where most families get one of their top choices.


2️⃣ Local Search Optimization

After the greedy schedule is built:

The algorithm iterates over each family and each of their 10 preferred days.

If moving a family to a different preferred day reduces the total Kaggle cost, the change is kept.

This hill-climbing process gradually improves preference satisfaction and reduces accounting penalties.

This step ensures the solution is locally optimized while keeping all constraints satisfied.


🧮 Cost Function

The project fully implements the official Kaggle scoring formula:

Preference Penalty
Families incur penalties based on which of their 10 choices they are assigned to.
The farther from the top choice, the higher the penalty.

Daily Occupancy Constraints
Each day must have between 125 and 300 visitors.
Violations are heavily penalized.

Accounting Penalty
Penalizes large day-to-day attendance fluctuations to encourage smooth schedules.

The total cost is the sum of all three components, and the optimizer minimizes this value.


⚙️ Workflow

Load the family preference and size dataset.

Sort families by size.

Assign families greedily to preferred days while respecting capacity limits.

Place any unassigned families into low-occupancy days.

Evaluate the schedule using the Kaggle cost function.

Apply local search to further optimize assignments.

Save the final optimized schedule as submission_<score>.csv.


📂 Output

The CSV submission file contains:
family_id, assigned_day

The filename includes the final score:
submission_<score>.csv

It is ready for direct upload to Kaggle.



🧩 Why This Works

Greedy heuristics produce a valid initial schedule quickly.

Capacity control ensures all constraints are satisfied.

Local search iteratively improves the solution for better preference and accounting scores.

Exact Kaggle cost function ensures the solution is meaningful and competitive.

This makes the solver effective for this large-scale, NP-hard scheduling problem.
