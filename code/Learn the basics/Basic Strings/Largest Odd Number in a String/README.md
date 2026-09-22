# 341. Largest Odd Number in a String


## Problem

Given a string `s`, representing a large integer, the task is to return the **largest-valued odd integer** (as a string) that is a substring of the given string `s`.

The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found return empty string).

## Example 1

**Input:**
```text
s = "5347"
```

**Output:**
```text
"5347"
```

**Explanation:**

The odd numbers formed by the given string are → `5, 53, 533, 5347, 547`.

So the largest among all the possible odd numbers for given string is `5347`.

## Example 2

**Input:**
```text
s = "0214638"
```

**Output:**
```text
"21463"
```

**Explanation:**

The different odd numbers that can be formed by the given string are → `1, 3, 21, 63, 463, 1463, 21463`.

We cannot include `021463` as the number contains leading zero.

So largest odd number in given string is `21463`.

## Constraints

- `1 <= s.length <= 10^3`
- `'0' <= s[i] <= '9'`