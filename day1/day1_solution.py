def solve_day1(input_file):
    """
    Solve Day 1: Secret Entrance
    
    Process rotation instructions for a dial (0-99) starting at position 50.
    Count how many times the dial lands on 0 after each rotation.
    """
    with open(input_file, 'r') as f:
        instructions = [line.strip() for line in f if line.strip()]
    
    position = 50  # Starting position
    zero_count = 0  # Count of times dial points to 0
    
    for instruction in instructions:
        direction = instruction[0]  # 'L' or 'R'
        distance = int(instruction[1:])  # Number of clicks
        
        if direction == 'L':
            # Rotate left (toward lower numbers)
            position = (position - distance) % 100
        else:  # direction == 'R'
            # Rotate right (toward higher numbers)
            position = (position + distance) % 100
        
        # Check if dial points to 0 after this rotation
        if position == 0:
            zero_count += 1
    
    return zero_count


if __name__ == "__main__":
    result = solve_day1("day1_input.txt")
    print(f"The password is: {result}")
