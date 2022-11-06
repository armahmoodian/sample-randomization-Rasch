population_number = int(input("Enter number of total population:"))
time_slot_number = int(input("Enter number of time points per entry:"))
sample_number = int(input("Enter number of sample you need:"))
print("Ok. so you should have ", int(population_number)*int(time_slot_number), " records from 1 to", int(population_number)*int(time_slot_number),".and you need ", time_slot_number, "sample groups with ",sample_number//time_slot_number,"samples in each")

# patient_number = 100
# time_slot_number = 5
selected_patients = []
# sample_groupes = {'timeslot_1': [], 'timeslot_2': [], 'timeslot_2': [], 'timeslot_4': [], 'timeslot_5': [], }
sample_groupes = []
for x in range(time_slot_number):
    sample_groupes.append([])
# sample_groupes = {}
import random
# print(random.randint(1, patient_number))
while len(selected_patients) < sample_number:
    rand_p = random.randint(1, population_number)
    if rand_p not in selected_patients:     #check if new sample selected
        rand_ts = random.randint(0, time_slot_number-1)
        if len(sample_groupes[rand_ts])< sample_number//time_slot_number:
        # selected_patients.append((rand_p-1)*time_slot_number+rand_ts)
            sample_groupes[rand_ts].append((rand_p-1)*time_slot_number+(rand_ts+1))
            selected_patients.append(rand_p)
# selected_patients.sort()
for x in range(time_slot_number):
    print(f'for time point {x+1} use recordes:')
    print(sample_groupes[x])
