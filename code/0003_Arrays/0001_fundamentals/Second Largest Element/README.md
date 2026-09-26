# Second Largest Element

Given an array of integers `nums`, return the second-largest element in the array. If the second-largest element does not exist, return -1.

## Example 1:

> **Input:** `nums = [8, 8, 7, 6, 5]`
> **Output:** 7
> 
> **Explanation:**
> The largest value in nums is 8, the second largest is 7

## Example 2:

> **Input:** `nums = [10, 10, 10, 10, 10]`
> **Output:** -1
> 
> **Explanation:**
> The only value in nums is 10, so there is no second largest value, thus -1 is returned

---

**Still unsure what the problem is asking?**
Let's go through a few more examples, step by step, to make it clearer.

[Explain problem]

---

## Constraints:

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `nums` may contain duplicate elements.