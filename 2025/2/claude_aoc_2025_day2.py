#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 2: Gift Shop
Find invalid product IDs (numbers that are a pattern repeated twice)
"""

import re


def is_invalid_part1(n):
    """
    Part 1: Check if a number is made of a sequence repeated exactly twice.
    Examples: 55, 6464, 123123 are invalid
    
    Strategy: Check if the number string can be split in half and both halves match.
    """
    s = str(n)
    length = len(s)
    
    # Must be even length to be split in half
    if length % 2 != 0:
        return False
    
    # Split in half and compare
    mid = length // 2
    left_half = s[:mid]
    right_half = s[mid:]
    
    return left_half == right_half


def is_invalid_part1_regex(n):
    """
    Alternative Part 1 solution using regex.
    Pattern (.+)\1$ means: capture any pattern, then match it again at the end.
    """
    s = str(n)
    return bool(re.match(r'^(.+)\1$', s))


def is_invalid_part2(n):
    """
    Part 2: Check if a number is made of ANY pattern repeated ANY number of times.
    Examples: 55, 123123123, 77777 are all invalid
    
    Strategy: Try all possible pattern lengths (1 to half the string length).
    For each pattern length, check if repeating that pattern creates the full number.
    """
    s = str(n)
    length = len(s)
    
    # Try each possible repeating pattern length
    for pattern_len in range(1, length // 2 + 1):
        # Only valid if the pattern divides evenly into the total length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            
            # Check if repeating the pattern creates the original number
            if pattern * repetitions == s:
                return True
    
    return False


def is_invalid_part2_regex(n):
    """
    Alternative Part 2 solution using regex.
    Pattern ^(.+?)\1+$ means: 
    - (.+?) captures the shortest pattern (non-greedy)
    - \1+ matches that pattern repeated one or more times
    - Together they ensure the whole string is just repetitions
    """
    s = str(n)
    return bool(re.match(r'^(.+?)\1+$', s))


def parse_ranges(input_line):
    """
    Parse the comma-separated ranges like "11-22,95-115"
    Returns list of (start, end) tuples
    """
    ranges = []
    parts = input_line.strip().split(',')
    
    for part in parts:
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            ranges.append((int(start), int(end)))
    
    return ranges


def solve_part1(input_line):
    """
    Part 1: Find invalid IDs (patterns repeated exactly twice)
    """
    ranges = parse_ranges(input_line)
    total = 0
    invalid_count = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_part1(num):
                total += num
                invalid_count += 1
    
    return total, invalid_count


def solve_part2(input_line):
    """
    Part 2: Find invalid IDs (any repeating pattern)
    """
    ranges = parse_ranges(input_line)
    total = 0
    invalid_count = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_part2(num):
                total += num
                invalid_count += 1
    
    return total, invalid_count


def main():
    # Example from puzzle
    example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    
    print("=" * 60)
    print("EXAMPLE TEST")
    print("=" * 60)
    
    # Part 1 example
    total1, count1 = solve_part1(example)
    print(f"Part 1:")
    print(f"  Invalid IDs found: {count1}")
    print(f"  Sum: {total1}")
    print(f"  Expected: 1227775554")
    print(f"  {'✓ CORRECT!' if total1 == 1227775554 else '✗ INCORRECT'}")
    print()
    
    # Show some example invalid IDs
    print("Example invalid IDs from Part 1:")
    print(f"  11 (1 twice): {is_invalid_part1(11)}")
    print(f"  22 (2 twice): {is_invalid_part1(22)}")
    print(f"  99 (9 twice): {is_invalid_part1(99)}")
    print(f"  6464 (64 twice): {is_invalid_part1(6464)}")
    print(f"  123123 (123 twice): {is_invalid_part1(123123)}")
    print(f"  101 (not a pattern): {is_invalid_part1(101)}")
    print()
    
    # Test Part 2 patterns
    print("Example patterns for Part 2:")
    print(f"  55 (5 × 2): {is_invalid_part2(55)}")
    print(f"  123123 (123 × 2): {is_invalid_part2(123123)}")
    print(f"  777 (7 × 3): {is_invalid_part2(777)}")
    print(f"  12121212 (12 × 4): {is_invalid_part2(12121212)}")
    print(f"  123 (no pattern): {is_invalid_part2(123)}")
    print()
    
    print("=" * 60)
    print("ACTUAL PUZZLE")
    print("=" * 60)
    
    # Read actual puzzle input
    try:
        with open('input.txt', 'r') as f:
            puzzle_input = f.read().strip()
        
        total1, count1 = solve_part1(puzzle_input)
        print(f"Part 1:")
        print(f"  Invalid IDs found: {count1}")
        print(f"  Answer: {total1}")
        print()
        
        total2, count2 = solve_part2(puzzle_input)
        print(f"Part 2:")
        print(f"  Invalid IDs found: {count2}")
        print(f"  Answer: {total2}")
        
    except FileNotFoundError:
        print("Save your puzzle input as 'input.txt' to solve the full puzzle")


if __name__ == '__main__':
    main()
