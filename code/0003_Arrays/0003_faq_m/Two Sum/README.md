# Two Sum

Given an array of integers `nums` and an integer `target`. Return the indices(0 - indexed) of two elements in `nums` such that they add up to `target`.

Each input will have exactly one solution, and the same element **cannot** be used twice. Return the answer in any order.

## Example 1:

> **Input:** `nums = [1, 6, 2, 10, 3], target = 7`
> **Output:** `[0, 1]`
>
> **Explanation:**
> `nums[0] + nums[1] = 1 + 6 = 7`

## Example 2:

> **Input:** `nums = [1, 3, 5, -7, 6, -3], target = 0`
> **Output:** `[1, 5]`
>
> **Explanation:**
> `nums[1] + nums[5] = 3 + (-3) = 0`

---

## Constraints:

*   `2 <= nums.length <= 10^5`
*   `-10^4 <= nums[i] <= 10^4`
*   `-10^8 <= target <= 10^8`
*   Only one valid answer exists.