import pandas as pd
import numpy as np

family_df =pd.read_csv("/home/taron/PycharmProjects/Santa_pap_project/family_data.csv")

family_df.sort_values("n_people", ascending=False, inplace=True)


day_member = np.zeros(101)


family_df['day'] = 0

# print(family_df["n_people"].sum())







for family in family_df.itertuples():
    if day_member[family.choice_0] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_0
        day_member[family.choice_0] += family.n_people


for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_1] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_1
        day_member[family.choice_1] += family.n_people


for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_2] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_2
        day_member[family.choice_2] += family.n_people

for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_3] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_3
        day_member[family.choice_3] += family.n_people

for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_4] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_4
        day_member[family.choice_4] += family.n_people


for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_5] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_5
        day_member[family.choice_5] += family.n_people

for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_6] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_6
        day_member[family.choice_6] += family.n_people

for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_7] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_7
        day_member[family.choice_7] += family.n_people


for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_8] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_8
        day_member[family.choice_8] += family.n_people

#
for family in family_df.itertuples():
    if family.day == 0 and day_member[family.choice_9] <= 210: #=125
        family_df.loc[family.Index, 'day'] = family.choice_9
        day_member[family.choice_9] += family.n_people





free_days = np.where(day_member[1:] < 170)[0] +1 #=300




zero_day_rows = family_df.index[family_df["day"] == 0]

day_ptr = 0

for row in zero_day_rows:
    people = family_df.loc[row, "n_people"]


    if day_ptr >= len(free_days):
        print("No more days with <125 capacity.")
        break

    day_idx = free_days[day_ptr]


    if day_member[day_idx] + people <= 210: #=300
        family_df.loc[row, "day"] = day_idx
        day_member[day_idx] += people


        if day_member[day_idx] >= 203: #=300
            day_ptr += 1

    else:

        day_ptr += 1
        if day_ptr >= len(free_days):
            print("No more days with <125 capacity.")
            break

        day_idx = free_days[day_ptr]
        family_df.loc[row, "day"] = day_idx
        day_member[day_idx] += people

        if day_member[day_idx] >= 220: #=300
            day_ptr += 1






# print(day_member)





family_df.sort_values("family_id", ascending=True, inplace=True)
new_df = pd.DataFrame(columns=["family_id","assigned_day"])
new_df["family_id"] = family_df["family_id"].values
new_df["assigned_day"] = family_df["day"].values
new_df.to_csv("Family_call.csv", index=False)






fpath = '/home/taron/PycharmProjects/Santa_pap_project/family_data.csv'
data = pd.read_csv(fpath, index_col='family_id')

fpath = 'Family_call.csv'
submission = pd.read_csv(fpath, index_col='family_id')


family_size_dict = data[['n_people']].to_dict()['n_people']

cols = [f'choice_{i}' for i in range(10)]
choice_dict = data[cols].to_dict()

N_DAYS = 100
MAX_OCCUPANCY = 300
MIN_OCCUPANCY = 125

# from 100 to 1
days = list(range(N_DAYS,0,-1))
def cost_function(prediction):

    penalty = 0

    # We'll use this to count the number of people scheduled each day
    daily_occupancy = {k:0 for k in days}

    # Looping over each family; d is the day for each family f
    for f, d in enumerate(prediction):

        # Using our lookup dictionaries to make simpler variable names
        n = family_size_dict[f]
        choice_0 = choice_dict['choice_0'][f]
        choice_1 = choice_dict['choice_1'][f]
        choice_2 = choice_dict['choice_2'][f]
        choice_3 = choice_dict['choice_3'][f]
        choice_4 = choice_dict['choice_4'][f]
        choice_5 = choice_dict['choice_5'][f]
        choice_6 = choice_dict['choice_6'][f]
        choice_7 = choice_dict['choice_7'][f]
        choice_8 = choice_dict['choice_8'][f]
        choice_9 = choice_dict['choice_9'][f]

        # add the family member count to the daily occupancy
        daily_occupancy[d] += n

        # Calculate the penalty for not getting top preference
        if d == choice_0:
            penalty += 0
        elif d == choice_1:
            penalty += 50
        elif d == choice_2:
            penalty += 50 + 9 * n
        elif d == choice_3:
            penalty += 100 + 9 * n
        elif d == choice_4:
            penalty += 200 + 9 * n
        elif d == choice_5:
            penalty += 200 + 18 * n
        elif d == choice_6:
            penalty += 300 + 18 * n
        elif d == choice_7:
            penalty += 300 + 36 * n
        elif d == choice_8:
            penalty += 400 + 36 * n
        elif d == choice_9:
            penalty += 500 + 36 * n + 199 * n
        else:
            penalty += 500 + 36 * n + 398 * n

    # for each date, check total occupancy
    #  (using soft constraints instead of hard constraints)
    for _, v in daily_occupancy.items():
        if (v > MAX_OCCUPANCY) or (v < MIN_OCCUPANCY):
            penalty += 100000000

    # Calculate the accounting cost
    # The first day (day 100) is treated special
    accounting_cost = (daily_occupancy[days[0]]-125.0) / 400.0 * daily_occupancy[days[0]]**(0.5)
    # using the max function because the soft constraints might allow occupancy to dip below 125
    accounting_cost = max(0, accounting_cost)

    # Loop over the rest of the days, keeping track of previous count
    yesterday_count = daily_occupancy[days[0]]
    for day in days[1:]:
        today_count = daily_occupancy[day]
        diff = abs(today_count - yesterday_count)
        accounting_cost += max(0, (daily_occupancy[day]-125.0) / 400.0 * daily_occupancy[day]**(0.5 + diff / 50.0))
        yesterday_count = today_count

    penalty += accounting_cost

    return penalty

# Start with the sample submission values
best = submission['assigned_day'].tolist()
start_score = cost_function(best)

new = best.copy()
# loop over each family
for fam_id, _ in enumerate(best):
    # loop over each family choice
    for pick in range(10):
        day = choice_dict[f'choice_{pick}'][fam_id]
        temp = new.copy()
        temp[fam_id] = day # add in the new pick
        if cost_function(temp) < start_score:
            new = temp.copy()
            start_score = cost_function(new)

submission['assigned_day'] = new
score = cost_function(new)
submission.to_csv(f'submission_{score}.csv')
print(f'Score: {score}')