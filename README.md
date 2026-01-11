# kaggle-santa-tour-2019

#🎅 Santa’s Workshop Tour 2019 — Optimization Solver

📌 Overview

This project solves the Santa’s Workshop Tour 2019 Kaggle optimization challenge.
The task is to assign 5,000 families to 100 days so that:

Each family is scheduled as close as possible to their preferred days

Each day has between 125 and 300 visitors

Large fluctuations in daily attendance are avoided

The objective is to minimize the total Kaggle cost, which consists of:

Preference penalties

Daily occupancy penalties

Accounting costs between consecutive days

🧠 Solution Strategy

This project implements a two-stage optimization pipeline:

1. Greedy Capacity-Aware Assignment

Families are first sorted by size (largest families first), because large families are harder to place without breaking daily capacity limits.

Each family is then assigned to its best available preferred day (choice_0 → choice_9) as long as the target day has enough remaining capacity.
This produces a high-quality initial schedule where most families get one of their top choices while keeping daily attendance under control.

Any families that remain unassigned after this step are placed into days with low occupancy to ensure all days move toward the valid range.

This stage guarantees:

Every family is assigned

No day is severely underfilled or overfilled

2. Local Search Improvement

After a valid schedule is built, a local search (hill-climbing) optimization is applied.

For each family, the algorithm:

Tries reassigning the family to each of its 10 preferred days

Recomputes the full Kaggle cost

Keeps the change only if it improves the total score

This step reduces both:

Preference penalties

Accounting penalties

while always keeping the schedule valid.

🧮 Kaggle Cost Function

The project fully implements the official Kaggle scoring system:

Preference Penalty

Families receive increasing penalties when they are assigned further away from their preferred days.

Daily Occupancy Constraints

Days with fewer than 125 or more than 300 people receive a very large penalty.

Accounting Cost

Additional penalties are applied when the number of visitors changes sharply between consecutive days, encouraging smooth daily attendance.

These three components are combined into a single cost function that the optimizer minimizes.

#⚙️ Workflow

Load family preference and size data

Sort families by size

Greedily assign families to preferred days under capacity limits

Fill remaining families into low-occupancy days

Evaluate using the Kaggle cost function

Apply local search to improve the schedule

Export the final optimized submission
