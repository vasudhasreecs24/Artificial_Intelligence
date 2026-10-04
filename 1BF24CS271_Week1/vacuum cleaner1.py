# Vacuum Cleaner Agent

# ---------------- SIMPLE REFLEX AGENT ----------------

def simple_reflex_agent(room_a, room_b, position):

    print("\n--- Simple Reflex Agent ---")

    while True:

        print("\nVacuum is in Room", position)

        # If current room is dirty -> Suck
        if position == 'A' and room_a == 'Dirty':
            print("Room A is Dirty -> Suck")
            room_a = 'Clean'

        elif position == 'B' and room_b == 'Dirty':
            print("Room B is Dirty -> Suck")
            room_b = 'Clean'

        # If current room is clean -> Move
        elif position == 'A' and room_a == 'Clean':
            print("Room A is Clean -> Move Right")
            position = 'B'

        elif position == 'B' and room_b == 'Clean':
            print("Room B is Clean -> Move Left")
            position = 'A'

        # Check whether both rooms are clean
        if room_a == 'Clean' and room_b == 'Clean':
            print("\nBoth rooms are Clean!")
            break

    print("Final Room A:", room_a)
    print("Final Room B:", room_b)
    print("Final Vacuum Position:", position)


# ---------------- GOAL BASED AGENT ----------------

def goal_based_agent(room_a, room_b, position):

    print("\n--- Goal Based Agent ---")

    while room_a != 'Clean' or room_b != 'Clean':

        print("\nVacuum is in Room", position)

        # If current room is dirty -> Suck
        if position == 'A' and room_a == 'Dirty':
            print("Room A is Dirty -> Suck")
            room_a = 'Clean'

        elif position == 'B' and room_b == 'Dirty':
            print("Room B is Dirty -> Suck")
            room_b = 'Clean'

        # If A is clean but B is dirty -> Move to B
        elif position == 'A' and room_a == 'Clean' and room_b == 'Dirty':
            print("Room A is Clean, Room B is Dirty -> Move Right")
            position = 'B'

        # If B is clean but A is dirty -> Move to A
        elif position == 'B' and room_b == 'Clean' and room_a == 'Dirty':
            print("Room B is Clean, Room A is Dirty -> Move Left")
            position = 'A'

    print("\nGoal Achieved!")
    print("Both rooms are Clean")
    print("Final Vacuum Position:", position)


# ---------------- MAIN PROGRAM ----------------

print("========== VACUUM CLEANER ==========")

room_a = input("Enter status of Room A (Clean/Dirty): ").strip().capitalize()
room_b = input("Enter status of Room B (Clean/Dirty): ").strip().capitalize()

position = input("Enter initial vacuum location (A/B): ").strip().upper()

print("\n========== INITIAL STATE ==========")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Location: Room", position)

# Run Simple Reflex Agent
simple_reflex_agent(room_a, room_b, position)

# Run Goal Based Agent
goal_based_agent(room_a, room_b, position)