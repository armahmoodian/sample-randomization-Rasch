import random

population_number = int(input("Enter number of total population: "))        # Total number of population
time_slot_number = int(input("Enter number of time points per entry: "))    # Number of time points per entry
sample_number = int(input("Enter number of sample you need: "))             # Number of samples needed

# Ask user to check data structure to make sure it's suitable for this algorithm
print("Ok. so you should have ", int(population_number)*int(time_slot_number),
      " records from 1 to", int(population_number)*int(time_slot_number),
      "and you need ", time_slot_number, "sample groups with ",
      sample_number//time_slot_number, "samples in each. IF NOT DO NOT USE THIS PROGRAM!!!")
while True:
    missed_records_deduction = input("Do you want to deduct missed records before sampling?(y/n): ").lower()
    if missed_records_deduction == "y" or missed_records_deduction == "yes":
        print("Your answer: Yes")
        missed_records = input("Enter missed records index separated by commas(','):\n")
        missed_records_list = [int(item) for item in missed_records.split(',') if item.strip().isdigit()]  # clean entered numbers and asign them to the list
        entry_with_missed_timeslot = [((item - 1) // time_slot_number) + 1 for item in missed_records_list]  # find the entries with missing data
        entry_with_missed_timeslot = list(dict.fromkeys(entry_with_missed_timeslot))    # make a unique list of entries with missing data
        print("The following list will be deducted from sampling:")
        print("missing records: ", missed_records_list)
        print("unique entries with missed time slots: ", entry_with_missed_timeslot)
        break
    if missed_records_deduction == "n" or missed_records_deduction == "no":
        print("Your answer: No")
        missed_records_list = []
        entry_with_missed_timeslot = []
        break

selected_patients = []          # list of patients that selected yet
sample_groups = []             # two dimensional list of selected samples
for x in range(time_slot_number):
    sample_groups.append([])    # populate sample_groups list wth empty lists!


while len(selected_patients) < len(entry_with_missed_timeslot):      # while all samples are not obtained
    rand_p_index = random.randint(0, len(entry_with_missed_timeslot)-1)  # select a random sample
    if entry_with_missed_timeslot[rand_p_index] not in selected_patients:            # check if no other sample from that entry(patient) selected before
        rand_ts = random.randint(0, time_slot_number - 1)  # select a random time slot
        while ((entry_with_missed_timeslot[rand_p_index] - 1) * time_slot_number) + (rand_ts + 1) in missed_records_list:
            rand_ts = random.randint(0, time_slot_number-1)     # select a random time slot
        if len(sample_groups[rand_ts])< sample_number//time_slot_number:    # check if all needed samples for time slot not obtained
            sample_groups[rand_ts].append((entry_with_missed_timeslot[rand_p_index] - 1) * time_slot_number + (rand_ts + 1))      # add random sample to appropriate sample group
            selected_patients.append(entry_with_missed_timeslot[rand_p_index])

while len(selected_patients) < sample_number:      # while all samples are not obtained
    rand_p = random.randint(1, population_number)  # select a random sample
    if rand_p not in selected_patients:            # check if no other sample from that entry(patient) selected before
        rand_ts = random.randint(0, time_slot_number-1)     # select a random time slot
        if len(sample_groups[rand_ts])< sample_number//time_slot_number:    # check if all needed samples for time slot not obtained
            sample_groups[rand_ts].append((rand_p - 1) * time_slot_number + (rand_ts + 1))      # add random sample to appropriate sample group
            selected_patients.append(rand_p)

for x in range(time_slot_number):   # print the result
    print(f'for time point {x+1} use records:')
    print(sample_groups[x])
