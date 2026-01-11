# kaggle-santa-tour-2019

🎅 Santa’s Workshop Tour 2019 – Optimization Project

📌 Problem Overview

Santa’s Workshop Tour 2019 is a Kaggle optimization challenge where 5,000 families must be scheduled to visit Santa over 100 days (Day 1 to Day 100).

Each family provides 10 preferred days.
Assigning a family to a day that is not among their top preferences results in a penalty cost.

Additionally, every day must satisfy attendance constraints:

Minimum visitors per day: 125

Maximum visitors per day: 300

If daily attendance is unbalanced, an accounting penalty is applied.
The goal is to minimize the total cost:

Total Cost=Preference Penalty+Accounting Penalty
Total Cost=Preference Penalty+Accounting Penalty
🎯 Objective

The task is to find an assignment of families to days such that:

Families are assigned as close as possible to their preferred days

Daily attendance stays within limits

Large fluctuations between consecutive days are avoided

The total cost is minimized

This makes the problem a large-scale constrained combinatorial optimization problem.

📊 Dataset

The Kaggle dataset provides:

A list of 5,000 families

For each family:

Family size

10 preferred days (choice_0 to choice_9)

Each family must be assigned exactly one day.

💡 Solution Approach
