#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1: Secret Entrance
Safe dial combination puzzle solver
"""

def parse_rotation(line):
    """
    Parse a rotation instruction like 'L68' or 'R48'
    Returns: (direction_multiplier, distance)
        -1 for left (L), +1 for right (R)
    """
    direction = line[0]
    distance = int(line[1:])
    multiplier = -1 if direction == 'L' else 1
    return multiplier, distance


def solve_part1(rotations):
    """
    Part 1: Count how many times the dial stops at 0 after each rotation.
    
    The dial starts at 50 and wraps around (0-99 circular).
    """
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        multiplier, distance = parse_rotation(rotation)
        position = (position + multiplier * distance) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count


def solve_part2(rotations):
    """
    Part 2: Count how many times the dial SHOWS 0 during any rotation.
    This includes both stopping at 0 and passing through 0.
    """
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        multiplier, distance = parse_rotation(rotation)
        
        # For each individual click/step in the rotation
        for _ in range(distance):
            position = (position + multiplier) % 100
            
            if position == 0:
                zero_count += 1
    
    return zero_count


def main():
    # Example from puzzle description
    example = [
        "L68", "L30", "R48", "L5", "R60",
        "L55", "L1", "L99", "R14", "L82"
    ]
    
    print("Example Test:")
    print(f"Part 1 (stops at 0): {solve_part1(example)}")
    print(f"Expected: 3")
    print()
    
    # Read actual puzzle input
    try:
        with open('input.txt', 'r') as f:
            rotations = [line.strip() for line in f if line.strip()]
        
        print("Puzzle Input:")
        part1_answer = solve_part1(rotations)
        print(f"Part 1 Answer: {part1_answer}")
        
        part2_answer = solve_part2(rotations)
        print(f"Part 2 Answer: {part2_answer}")
        
    except FileNotFoundError:
        print("Note: Save your puzzle input as 'input.txt' to solve the full puzzle")
        print("\nYou can also test with the example:")
        print("Example Part 1:", solve_part1(example))
        
        # Show the dial positions for the example
        print("\nDial positions for example:")
        position = 50
        print(f"Start: {position}")
        for rotation in example:
            multiplier, distance = parse_rotation(rotation)
            position = (position + multiplier * distance) % 100
            marker = " <- ZERO!" if position == 0 else ""
            print(f"{rotation}: {position}{marker}")


if __name__ == '__main__':
    main()
