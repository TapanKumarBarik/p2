# Left Rotate Array by One

Given an integer array `nums`, rotate the array to the **left** by **one**.

**Note:** There is no need to return anything, just modify the given array.

## Example 1:

> **Input:** `nums = [1, 2, 3, 4, 5]`
> **Output:** `[2, 3, 4, 5, 1]`
>
> **Explanation:**
> Initially, `nums = [1, 2, 3, 4, 5]`
> Rotating once to left → `nums = [2, 3, 4, 5, 1]`

## Example 2:

> **Input:** `nums = [-1, 0, 3, 6]`
> **Output:** `[0, 3, 6, -1]`
>
> **Explanation:**
> Initially, `nums = [-1, 0, 3, 6]`
> Rotating once to left → `nums = [0, 3, 6, -1]`

---

## Constraints:

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`