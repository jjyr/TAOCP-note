1.

```
TEMP <- a
a <- b
b <- c
c <- d
d <- TEMP
```

2. 因为 r 是 remainer 不能被 n 整出，所以 r < n, 所以 n < m

3. Algo F:

F1. Divide m by n and let m be the remainer
F2. if m = 0 the algorithm terminates n is answer.
F3. swap m and n, then jump to F1.

4. 

57

8.

| j | theta | phi  | a | b |
| - | ----- | ---- | - | - |
| 0 | "ab"  | "c"  | 1 | 0 |
| 1 | "ac"  | "cb" | 2 | 1 |
| 2 | "b"   | "b"  | 4 | 3 |
| 3 | "c"   | "a"  | 0 | 3 |
| 4 | "c"   | "b"  | 5 | 4 |

- j0: `r <- |m - n|`, c represents `TEMP <- min(m, n)`, the remain `a` or `b` represents reminder `r`;
- j1: set `n <- r`;
- j2: notice `r` is set to `n` in j1, jump to final step if `r` is zero, otherwise jump to next step;
- j3: set `m <- TEMP(min(m, n))`, then go back to j0;
- j4: final step, `r` is zero, the result `n` is represents in inner letter "c", this step convert "c" to "b", to according the output format.
