def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}  
    cost = 0

    loc = input("Enter Location of Vacuum (A/B): ")
    status_input = input(f"Enter status of {loc}: (0: Clean, 1: Dirty) ")
    otherloc = 'B' if loc == 'A' else 'A'
    other_status = input(f"Enter status of {otherloc}: (0: Clean, 1: Dirty) ")

    if status_input == '1':
        print(f"Location {loc} is Dirty.")
        goal_state[loc] = '0'  
        cost += 1
        print(f'cost of cleaning {loc} '+ str(cost))

    if other_status == '1':
        print(f"Location {otherloc} is Dirty.")
        cost += 1  
        print(f"Moving to Location {otherloc}.")
        goal_state[otherloc] = '0' 
        cost += 1
        print(f'cost of cleaning {otherloc} '+ str(cost))

    print("GOAL STATE:", goal_state)
    print("Performance Measurement:", cost)

vacuum_world()
