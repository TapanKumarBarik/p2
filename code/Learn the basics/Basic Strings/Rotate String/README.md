# 324. Rotate String

## Problem

Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of shifts on `s`.

A shift consists of moving the **leftmost character** of `s` to the **rightmost position**.

For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

## Example 1

**Input:**
```text
s = "abcde", goal = "cdeab"
```

**Output:**
```text
true
```

**Explanation:**

After 2 shifts:

```text
abcde → bcdea → cdeab
```

## Example 2

**Input:**
```text
s = "abcde", goal = "acdeb"
```

**Output:**
```text
false
```

**Explanation:**

No number of shift operations can convert `s` into `goal`.

## Constraints

- `1 <= s.length <= 100`
- `1 <= goal.length <= 100`
- `s` and `goal` consist only of lowercase English letters.