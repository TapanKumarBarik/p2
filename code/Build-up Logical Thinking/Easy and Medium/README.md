# Pattern Printing: General Approach

## Core Idea

**Pattern printing = find what each row contains.**

For every row `i`, determine:

1. Spaces
2. Stars/elements
3. How the counts change with `i`

Then turn those counts into loops.

## Checklist

```text
1. How many rows?
2. What does the first row look like?
3. What does the last row look like?
4. Spaces per row?
5. Stars/elements per row?
6. Increasing or decreasing?
7. By how much?
8. Can I express it using i?
9. Is it made of smaller patterns?
```

## Common Formulas

| Count | Formula |
|---|---|
| `1, 2, 3...` | `i + 1` |
| `n, n-1, n-2...` | `n - i` |
| `1, 3, 5...` | `2*i + 1` |
| `9, 7, 5...` | `2*n - 2*i - 1` |
| Spaces increasing | `i` |
| Spaces decreasing | `n - i - 1` |

## Example

```text
   *
  ***
 *****
*******
```

For row `i`:

```text
spaces = n - i - 1
stars  = 2*i + 1
```

```python
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))
```

## Complicated Patterns

**Split them into smaller patterns.**

```text
Top half
+
Bottom half
```

### Golden Rule

> **Don't memorize patterns. Find the row formulas.**
