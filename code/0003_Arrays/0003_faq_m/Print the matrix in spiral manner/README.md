# Print the matrix in spiral manner

Given an M * N matrix, print the elements in a **clockwise** spiral manner.

Return an array with the elements in the order of their appearance when printed in a spiral manner.

## Example 1:

> **Input:** `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
> **Output:** `[1, 2, 3, 6, 9, 8, 7, 4, 5]`
>
> **Explanation:**
> The elements in the spiral order are 1, 2, 3 → 6, 9 → 8, 7 → 4, 5

## Example 2:

> **Input:** `matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]`
> **Output:** `[1, 2, 3, 4, 8, 7, 6, 5]`
>
> **Explanation:**
> The elements in the spiral order are 1, 2, 3, 4 → 8, 7, 6, 5

---

## Constraints:

*   `m == matrix.length`
*   `n == matrix[i].length`
*   `1 <= m, n <= 100`
*   `-100 <= matrix[i][j] <= 100`