#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 3: Lobby
Find maximum joltage from battery banks
"""

from functools import lru_cache


def solve_part1_brute_force(bank):
    """
    Part 1: Find the largest 2-digit number from a bank of batteries.
    Brute force approach: try all pairs of positions.
    """
    max_joltage = 0
    
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form a 2-digit number from positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage


def solve_part1_greedy(bank):
    """
    Part 1 optimized: Find largest 2-digit number greedily.
    Strategy: Find the largest digit, then find the largest digit after it.
    """
    if len(bank) < 2:
        return 0
    
    # Find the largest first digit
    max_first = '0'
    first_idx = -1
    for i in range(len(bank) - 1):  # Must have at least one digit after
        if bank[i] > max_first:
            max_first = bank[i]
            first_idx = i
    
    # Find the largest second digit after the first
    max_second = '0'
    for i in range(first_idx + 1, len(bank)):
        if bank[i] > max_second:
            max_second = bank[i]
    
    return int(max_first + max_second)


def solve_part2_recursive(bank, length, memo=None):
    """
    Part 2: Find the largest N-digit number from a bank.
    Uses memoization to avoid recomputing subproblems.
    
    For each position, we can either:
    - Use that digit as the next digit in our number
    - Skip it and look at subsequent positions
    """
    if memo is None:
        memo = {}
    
    # Base case: if we need 0 digits, result is 0
    if length == 0:
        return 0
    
    # If we don't have enough digits left, impossible
    if len(bank) < length:
        return -1
    
    # Check memo
    key = (bank, length)
    if key in memo:
        return memo[key]
    
    max_value = -1
    
    # Try using each position as the next digit
    for i in range(len(bank) - length + 1):
        # Use bank[i] as the next digit
        digit_value = int(bank[i]) * (10 ** (length - 1))
        
        # Recursively solve for the remaining digits
        if length == 1:
            # Base case: this is the last digit
            remaining = 0
        else:
            # Look for remaining digits in the substring after position i
            remaining = solve_part2_recursive(bank[i + 1:], length - 1, memo)
        
        if remaining >= 0:  # Valid solution found
            total = digit_value + remaining
            max_value = max(max_value, total)
    
    memo[key] = max_value
    return max_value


def solve_part2_dynamic(bank, length):
    """
    Part 2: Dynamic programming approach.
    dp[i][j] = maximum j-digit number we can form starting from position i
    """
    n = len(bank)
    
    # dp[i][j] = max value of j-digit number starting from index i or later
    dp = {}
    
    # Base case: 1-digit numbers
    for i in range(n):
        dp[(i, 1)] = int(bank[i])
    
    # Build up to length-digit numbers
    for num_digits in range(2, length + 1):
        for start_pos in range(n - num_digits + 1):
            max_val = -1
            
            # Try each position as the first digit
            for first_digit_pos in range(start_pos, n - num_digits + 1):
                digit = int(bank[first_digit_pos])
                digit_value = digit * (10 ** (num_digits - 1))
                
                # Find best remaining digits after this position
                if num_digits == 1:
                    total = digit_value
                else:
                    remaining_key = (first_digit_pos + 1, num_digits - 1)
                    if remaining_key in dp:
                        total = digit_value + dp[remaining_key]
                    else:
                        continue
                
                max_val = max(max_val, total)
            
            if max_val >= 0:
                dp[(start_pos, num_digits)] = max_val
    
    return dp.get((0, length), -1)


def solve_puzzle(input_data, part=1):
    """
    Solve the puzzle for the given input.
    
    For Part 1: Find maximum 2-digit joltage from each bank
    For Part 2: Find maximum N-digit joltage (likely larger N)
    """
    banks = [line.strip() for line in input_data.strip().split('\n')]
    total_joltage = 0
    
    for bank in banks:
        if part == 1:
            max_joltage = solve_part1_greedy(bank)
        else:
            # Part 2 typically requires longer sequences
            # Try to determine the optimal length dynamically
            max_joltage = solve_part2_recursive(bank, 12)  # Adjust based on actual puzzle
        
        total_joltage += max_joltage
    
    return total_joltage


def main():
    # Example from puzzle
    example = """987654321111111
811111111111119
234234234234278
818181911112111"""
    
    print("=" * 60)
    print("EXAMPLE TEST - Part 1")
    print("=" * 60)
    
    banks = example.strip().split('\n')
    
    for i, bank in enumerate(banks, 1):
        max_joltage_bf = solve_part1_brute_force(bank)
        max_joltage_greedy = solve_part1_greedy(bank)
        print(f"Bank {i}: {bank}")
        print(f"  Max joltage (brute force): {max_joltage_bf}")
        print(f"  Max joltage (greedy): {max_joltage_greedy}")
        print()
    
    total = solve_puzzle(example, part=1)
    print(f"Total output joltage: {total}")
    print(f"Expected: 357")
    print(f"{'✓ CORRECT!' if total == 357 else '✗ INCORRECT'}")
    print()
    
    print("=" * 60)
    print("TESTING Part 2 Functions")
    print("=" * 60)
    
    # Test the recursive/DP functions
    test_bank = "987654321111111"
    for length in range(2, 6):
        result = solve_part2_recursive(test_bank, length)
        print(f"Max {length}-digit number from '{test_bank}': {result}")
    print()
    
    print("=" * 60)
    print("ACTUAL PUZZLE")
    print("=" * 60)
    
    # Read actual puzzle input
    try:
        with open('input.txt', 'r') as f:
            puzzle_input = f.read().strip()
        
        print("Part 1:")
        part1_answer = solve_puzzle(puzzle_input, part=1)
        print(f"  Total joltage: {part1_answer}")
        print()
        
        print("Part 2:")
        # Note: Part 2 length may need adjustment based on actual puzzle requirements
        banks = puzzle_input.strip().split('\n')
        total = 0
        for bank in banks:
            # Try different lengths if needed - Part 2 typically asks for all digits
            max_joltage = solve_part2_recursive(bank, len(bank))
            total += max_joltage
        print(f"  Total joltage: {total}")
        
    except FileNotFoundError:
        print("Save your puzzle input as 'input.txt' to solve the full puzzle")
    
    print()
    print("Note: Part 2 typically increases the number of batteries to select.")
    print("If Part 2 is unlocked, check the puzzle for the specific requirement!")


if __name__ == '__main__':
    main()