# Highest Occurring Element in an Array

## Problem Description

Given an array `nums` of `n` integers, find the **most frequent element** in it, i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the **smallest of them**.

> Please note that this section might seem a bit difficult without prior knowledge of what hashing is, we will soon try to add basic concepts for you! If you know the concepts already please go ahead to give a shot to the problem. Cheers!

## Example 1

**Input:** `nums = [1, 2, 2, 3, 3, 3]`

**Output:** `3`

**Explanation:** The number `3` appears the most (`3` times). It is the most frequent element.

## Example 2

**Input:** `nums = [4, 4, 5, 5, 6]`

**Output:** `4`

**Explanation:** Both `4` and `5` appear twice, but `4` is smaller. So, `4` is the most frequent element.

## Example 3

**Input:** `nums = [2, 4, 3, 2, 5, 4]`

**Output:** `2`

## Constraints

- `1 <= n <= 10⁵`
- `1 <= nums[i] <= 10⁴`