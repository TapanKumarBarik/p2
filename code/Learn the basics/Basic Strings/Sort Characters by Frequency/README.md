# 303. Sort Characters by Frequency

## Problem

You are given a string `s`. Return the array of unique characters sorted by **highest to lowest occurring characters**.

If two or more characters have the same frequency, then arrange them in **alphabetical order**.

## Example 1

**Input:**
```text
s = "tree"
```

**Output:**
```text
['e', 'r', 't']
```

**Explanation:**

The occurrences of each character are:

```text
e → 2
r → 1
t → 1
```

The `r` and `t` have the same occurrences, so we arrange them by alphabetical order.

## Example 2

**Input:**
```text
s = "raaajj"
```

**Output:**
```text
['a', 'j', 'r']
```

**Explanation:**

The occurrences of each character are:

```text
a → 4
j → 2
r → 1
```

## Constraints

- `1 <= s.length <= 10⁴`
- `s` consists of only lowercase English characters.