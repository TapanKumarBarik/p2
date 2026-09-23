# 52. Valid Anagram


## Problem

Given two strings `s` and `t`, return `true` if `t` is an **anagram** of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Example 1

**Input:**
```text
s = "anagram", t = "nagaram"
```

**Output:**
```text
true
```

**Explanation:**

We can rearrange the characters of string `s` to get string `t` as the frequency of all characters from both strings is the same.

## Example 2

**Input:**
```text
s = "dog", t = "cat"
```

**Output:**
```text
false
```

**Explanation:**

We cannot rearrange the characters of string `s` to get string `t` as the frequency of all characters from both strings is not the same.

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of only lowercase English letters.