import csv


# demand file loading------------------------------------------------------------
# demand_id, type, p_time, due_date

for f in range(10):
    demand_file = open('{0}.txt'.format(f+1), 'r')
    demand_reader = csv.reader(demand_file)

    demand_list = []
    demand_idx = 0
    for demand in demand_reader:
        demand_list.append([demand_idx, demand[0], int(demand[1]), int(demand[2])])
        demand_idx += 1
    demand_list = sorted(demand_list, key=lambda x: x[3])
    #---------------------------------------------------------------------------------

    # macahine initial state----------------------------------------------------------

    machine_states = []
    for i in range(18):
        machine_states.append(['Z',0])
    # print(machine_states)
    #----------------------------------------------------------------------------------

    # FIFO - Scheduling-----------------------------------------------------
    schedule = []

    count = 0
    for demand in demand_list:
        machine_idx = count % 18
        demand_id = demand[0]
        demand_type = demand[1]
        p_time = int(demand[2])
        machine_id = 0
        for m in range(18):
            if demand_type == machine_states[m][0] or machine_states[m][0]=='Z':
                machine_id = m
                break

        
        print(machine_idx, demand)

        
        # machine_id = machine_idx
        c_time = machine_states[machine_id][1]
        machine_setup_type = machine_states[machine_id][0]
        machine_com_time = machine_states[machine_id][1]
        s_time = machine_com_time
        setup = 'X'
        
        if machine_setup_type != 'Z':
            if machine_setup_type == demand_type:
            # No setup
                pass
            else:
            # Yes setup
                s_time = s_time + 2
                setup = 'O'
        c_time = s_time + p_time
        due_date = int(demand[3])
        
        violation_time = min(p_time, max(0, c_time - due_date))
        # print('violation_time',violation_time)
        
        #machine last state change
        machine_states[machine_id][0] = demand_type
        machine_states[machine_id][1] = c_time
        # demand_id, machine_id, type,
        # p_time, s_time, c_time
        # due_date, setup(O,X),  violation_time
        schedule.append([demand_id, machine_id, demand_type, p_time, s_time, c_time, due_date, setup, violation_time])

        count += 1
    #-----------------------------------------------------------------------------------
    # print(schedule)

    f2 = open('{0}.csv'.format(f+1), 'w', newline='')
    wr = csv.writer(f2, delimiter=',')
    wr.writerow([18])
    for d in schedule:
        wr.writerow(d)
    f2.close()
