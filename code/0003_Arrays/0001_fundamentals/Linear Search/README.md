# Linear Search

Given an array of integers `nums` and an integer `target`, find the smallest index (0-based indexing) where the `target` appears in the array. If the target is not found in the array, return `-1`.

## Example 1

**Input:**
```text
nums = [2, 3, 4, 5, 3], target = 3
```

**Output:**
```text
1
```

**Explanation:**

The first occurrence of `3` in `nums` is at index `1`.

## Example 2

**Input:**
```text
nums = [2, -4, 4, 0, 10], target = 6
```

**Output:**
```text
-1
```

**Explanation:**

The value `6` does not occur in the array, hence the output is `-1`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= target <= 10^4`