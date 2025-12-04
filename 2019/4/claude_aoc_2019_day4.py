#!/usr/bin/env python3
"""
Advent of Code 2019 - Day 4: Secure Container
Find valid passwords in a range based on specific criteria
"""

from collections import Counter


def has_adjacent_digits(password):
    """
    Part 1: Check if password has two adjacent matching digits.
    Example: 122345 has 22
    """
    s = str(password)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def never_decreases(password):
    """
    Check if digits never decrease from left to right.
    Example: 111123 is valid, 223450 is not (5 > 0 is a decrease)
    """
    s = str(password)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


def has_exact_double(password):
    """
    Part 2: Check if password has at least one group of exactly 2 adjacent digits.
    The digits must not be part of a larger group.
    
    Examples:
    - 112233: Valid (has three groups of exactly 2)
    - 123444: Invalid (4 appears 3 times in a row)
    - 111122: Valid (has exactly 2 twos at the end, even though 1 appears 4 times)
    """
    s = str(password)
    
    # Count consecutive runs of each digit
    i = 0
    while i < len(s):
        current_digit = s[i]
        count = 1
        
        # Count how many times this digit repeats
        while i + count < len(s) and s[i + count] == current_digit:
            count += 1
        
        # If we found exactly 2 in a row, it's valid
        if count == 2:
            return True
        
        i += count
    
    return False


def has_exact_double_counter(password):
    """
    Alternative Part 2 solution using Counter and grouping.
    More Pythonic but same logic.
    """
    s = str(password)
    
    # Group consecutive digits
    groups = []
    i = 0
    while i < len(s):
        current = s[i]
        count = 1
        while i + count < len(s) and s[i + count] == current:
            count += 1
        groups.append((current, count))
        i += count
    
    # Check if any group has exactly 2
    return any(count == 2 for digit, count in groups)


def is_valid_part1(password):
    """
    Part 1 validation:
    1. Six-digit number (handled by range)
    2. Two adjacent digits are the same
    3. Digits never decrease
    """
    return has_adjacent_digits(password) and never_decreases(password)


def is_valid_part2(password):
    """
    Part 2 validation:
    1. Six-digit number (handled by range)
    2. Has at least one group of exactly 2 adjacent matching digits
    3. Digits never decrease
    """
    return has_exact_double(password) and never_decreases(password)


def solve(range_start, range_end):
    """
    Count valid passwords in the given range for both parts.
    """
    part1_count = 0
    part2_count = 0
    
    for password in range(range_start, range_end + 1):
        if is_valid_part1(password):
            part1_count += 1
        
        if is_valid_part2(password):
            part2_count += 1
    
    return part1_count, part2_count


def main():
    print("=" * 60)
    print("EXAMPLE TESTS")
    print("=" * 60)
    
    # Part 1 examples
    print("Part 1 Examples:")
    test_cases_p1 = [
        (111111, True, "double 11, never decreases"),
        (223450, False, "decreasing pair 50"),
        (123789, False, "no double"),
    ]
    
    for password, expected, reason in test_cases_p1:
        result = is_valid_part1(password)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {password}: {result} - {reason}")
    
    print()
    
    # Part 2 examples
    print("Part 2 Examples:")
    test_cases_p2 = [
        (112233, True, "all repeated digits are exactly two digits long"),
        (123444, False, "repeated 44 is part of larger group of 444"),
        (111122, True, "contains a double 22, even though 1 repeats more"),
    ]
    
    for password, expected, reason in test_cases_p2:
        result = is_valid_part2(password)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {password}: {result} - {reason}")
    
    print()
    print("=" * 60)
    print("ACTUAL PUZZLE - Range: 248345-746315")
    print("=" * 60)
    
    # Your puzzle input
    range_start = 248345
    range_end = 746315
    
    part1_answer, part2_answer = solve(range_start, range_end)
    
    print(f"\nPart 1 Answer: {part1_answer}")
    print(f"Part 2 Answer: {part2_answer}")
    
    print()
    print("=" * 60)
    print("DETAILED ANALYSIS")
    print("=" * 60)
    
    # Show some example valid passwords
    print("\nFirst 10 valid passwords (Part 1):")
    count = 0
    for password in range(range_start, range_end + 1):
        if is_valid_part1(password):
            print(f"  {password}")
            count += 1
            if count >= 10:
                break
    
    print("\nFirst 10 valid passwords (Part 2):")
    count = 0
    for password in range(range_start, range_end + 1):
        if is_valid_part2(password):
            print(f"  {password}")
            count += 1
            if count >= 10:
                break
    
    # Show some examples that pass Part 1 but fail Part 2
    print("\nExamples that pass Part 1 but fail Part 2:")
    count = 0
    for password in range(range_start, range_end + 1):
        if is_valid_part1(password) and not is_valid_part2(password):
            s = str(password)
            print(f"  {password} - has groups with 3+ matching digits")
            count += 1
            if count >= 5:
                break


if __name__ == '__main__':
    main()
