# 252. Isomorphic Strings


## Problem

Given two strings `s` and `t`, determine if they are **isomorphic**.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

- All occurrences of a character must be replaced with another character while preserving the order of characters.
- No two characters may map to the same character, but a character may map to itself.

## Example 1

**Input:**
```text
s = "egg", t = "add"
```

**Output:**
```text
true
```

**Explanation:**
- `e` in `s` can be replaced with `a` in `t`.
- `g` in `s` can be replaced with `d` in `t`.

Hence all characters in `s` can be replaced to get `t`.

## Example 2

**Input:**
```text
s = "apple", t = "bbnbm"
```

**Output:**
```text
false
```

**Explanation:**

Strings are matched index by index.

- At index `0`, `a` maps to `b`.
- At index `1`, `p` also maps to `b`.

This is invalid because two different characters (`a` and `p`) cannot map to the same character (`b`) in a one-to-one mapping.

Therefore, no valid mapping exists and the output is `false`.

## Example 3

**Input:**
```text
s = "paper", t = "title"
```

**Output:**
```text
true
```

## Constraints

- `1 <= s.length <= 10³`
- `s.length == t.length`
- `s` and `t` consist only of lowercase English letters.