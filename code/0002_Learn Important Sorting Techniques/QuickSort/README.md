# Quick Sorting

Given an array of integers called `nums`, sort the array in non-decreasing order using the **quick sort algorithm** and return the sorted array.

A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

## Example 1

**Input:**
```text
nums = [7, 4, 1, 5, 3]
```

**Output:**
```text
[1, 3, 4, 5, 7]
```

**Explanation:**

```text
1 <= 3 <= 4 <= 5 <= 7
```

Thus the array is sorted in non-decreasing order.

## Example 2

**Input:**
```text
nums = [5, 4, 4, 1, 1]
```

**Output:**
```text
[1, 1, 4, 4, 5]
```

**Explanation:**

```text
1 <= 1 <= 4 <= 4 <= 5
```

Thus the array is sorted in non-decreasing order.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `nums[i]` may contain duplicate values.