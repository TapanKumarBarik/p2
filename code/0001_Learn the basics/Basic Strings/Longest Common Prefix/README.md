# 79. Longest Common Prefix


## Problem

Write a function to find the **longest common prefix string** amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Example 1

**Input:**
```text
str = ["flowers", "flow", "fly", "flight"]
```

**Output:**
```text
"fl"
```

**Explanation:**

All strings given in array contain common prefix `"fl"`.

## Example 2

**Input:**
```text
str = ["dog", "cat", "animal", "monkey"]
```

**Output:**
```text
""
```

**Explanation:**

There is no common prefix among the given strings in array.

## Constraints

- `1 <= str.length <= 200`
- `1 <= str[i].length <= 200`
- `str[i]` contains only lowercase English letters.