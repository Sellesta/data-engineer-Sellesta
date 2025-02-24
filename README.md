# Speechify Data Engineer Test

This technical test is designed to evaluate your skills in implementing data structures and algorithms, writing SQL queries, and integrating them into a practical system.

## Task Details

### Task Checklist

1. **LRU Cache Implementation**
   - Location: `src/cache/lru_cache.py`
   - A Least Recently Used (LRU) cache implementation with O(1) time complexity for both get and set operations

2. **Array Threshold Problem**
   - Location: `src/array_threshold.py`
   - Finds the number of sub-arrays of size k whose average is greater than or equal to threshold
   - Time Complexity: O(n), Space Complexity: O(1)

3. **Longest Substring Without Repeating Characters**
   - Location: `src/longest_substring.py`
   - Finds the length of the longest substring without repeating characters
   - Time Complexity: O(n), Space Complexity: O(min(m,n)) where m is the size of the character set

### Setup & Run Instructions
```bash
# List all commands
make help

# Install dependencies & setup virtual environment
make setup

# Run Individual Tests
make test-lru          # Test LRU Cache implementation
make test-array        # Test Array Threshold problem
make test-substring    # Test Longest Substring problem

# Run All Tests
make test

# Helpers: Linting, Type Checking, Formatting
make lint
make type-check
make format
make check-all
```

### Time to Implement

1 Hour 30 Minutes

Suggested Breakdown:
- 30 Minutes: Implement LRU Cache
- 30 Minutes: Implement Array Threshold
- 30 Minutes: Implement Longest Substring

## Development Guidelines

### Do's

- Write clean, maintainable, and well-documented code.
- Please follow the best practices and coding standards.
- Test cases are provided for all methods; use them to ensure that your code is correct and meets our requirements.
- You are free to use any official documentation or language references.
- You can use the debugging tools and native IDE features (only standard Auto-Completion)

### Don'ts

- Do NOT use any external libraries for the implementation.
- DO NOT use any Coding Assistants like GitHub Copilot, ChatGPT, etc or any other AI based tools.
- DO NOT visit direct blogs or articles related to implementation of the tasks.
- DO NOT use StackOverflow or any other forum websites.
