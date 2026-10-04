# Set Matrix Zeroes

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`. You must do it in place.

## Example 1:

> **Input:** `matrix = [[1,1,1],[1,0,1],[1,1,1]]`
> **Output:** `[[1,0,1],[0,0,0],[1,0,1]]`
>
> **Explanation:**
> Element at position (1,1) is 0, so set entire row 1 and column 1 to 0.

## Example 2:

> **Input:** `matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]`
> **Output:** `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`
>
> **Explanation:**
> There are two zeroes: (0,0) and (0,3).
> * Row 0 → all elements become 0
> * Column 0 and column 3 → all elements become 0

---

## Constraints:

* `m == matrix.length`
* `n == matrix[0].length`
* `1 <= m, n <= 200`
* `-2^31 <= matrix[i][j] <= 2^31 - 1`