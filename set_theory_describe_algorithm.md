# Set theory to describe a algorithm

Use a quadruple set to formalize a computational method

`(Q, I, O, f)`

**Q** is a set contains all possible input and output of algorithm, or another describe is Q is a superset contains subsets I and O.

**I** is a set contains all possible input value.

**O** is a set contains all possible output value.

**f** is a function from Q to itself. (f is our algorithm), f should leave O pointwise fixed, `f(q) => q for q in O`.

`(Q, I, O, f)` represent states and rule of computation.

Each input `x` in **I** defines a computational sequence `x0, x1, x2...`:

`x[0] = x and x[k+1] = f(x[k]) for k >= 0`

Once `x[k]` is in **O** the `x[k + 1] = x[k]`, the sequence is terminated.

Some computational sequence may never terminate, the `finiteness` require an algorithm terminates in finite steps for all `x` in I.

For example Algorithm E(euclid algorithm):

Let Q be set of `(n)`, `(m, n)`, `(m, n, r, 1)`, `(m, n, r, 2)` and `(m, n, p, 3)` where `m, n, p` are positive integers and `r` is nonnegative integer. Notice the last three quadruples are internal inputs, represent three steps of our algorithm.

Let I be set of all pairs `(m, n)`.
Let O be subset of all singleton `(n)`.
Let f be defined as follows:

```python
f((m, n)) = (m, n, 0, 1);
f((n)) = (n);
f((m, n, r, 1)) = (m, n, remainder of m devided by n, 2);
f((m, n, r, 2)) = (n) of r = 0, (m, n, r, 3) otherwise;
f((m, n, p, 3)) = (n, p, p, 1).
```

## Markov Algorithm

[Original markov algorithm](https://en.wikipedia.org/wiki/Markov_algorithm)

[An explaination by rudikershaw](https://www.rudikershaw.com/articles/computationalmethod3)

Pre defined:

- `A` a finite set of letters.
- `A*` set of all strings on A.
- `theta` source chars that we want to replace.
- `phi` distinate chars.
- `j` a number that `0 <= j < N`
- `sigma` input string
- `a`
- `b`

for short we use first letter of `phi, theta, sigma`

The **Q**: all `(s, j)` that `s` from `A*`

The **I**: `(s, 0)`

The **O**: `(s, N)`

The **f**:

``` python
f(s, j) = (s, a[j]) if t[j] do not occur in s;
f(s, j) = (al | p[j] | o, b[j]) if al is shortest possible string for s = al | t[j] | o;
f(s, N) = f(s, N).
```

The confuse part is that serveral variables(`a, b, theta, phi`) are introduced without any explaination.

Let's see each step to figure out meaning of these variables.

Rule 1 if the `t[j]` *not occur* in `s`, jump to `a[j]` position.
Rule 2 if the `t[j]` *occur* in `s`, replace the `t[j]` with `p[j]` then jump to `b[j]`.
Rule 3 finish the program.

The intention of `theta` and `phi` is easy to see, `theta` represents patterns, `phi` represents replaced strings.

It is also easy to notice when matching successed the program jump to `b[j]`, and when matching failed the program jump to `a[j]`, we can use `a, b` to control the jump logic.

An example:

| j | theta   | phi         | a | b |
| - | ------- | ----------- | - | - |
| 0 | "Hi"    | "Konichiwa" | 5 | 1 |
| 1 | "one"   | "ichi"      | 2 | 1 |
| 2 | "two"   | "ni"        | 3 | 1 |
| 3 | "three" | "san"       | 4 | 1 |
| 4 | "Bye"   | "Sayonara"  | 5 | 5 |
| 5 | -       | -           | - | - |

In the rule above, we implement an english to japanese translator.

Notice the translator use `a` and `b` to control logic, when `s` does not start with `Hi` and ends with `Bye`, the translator will halt for the impolite input, to archieve this, we set `a[j]` to `5` when `theta[j]` is "Hi" and "Bye", for the other words, we jump back to `1` if matching success, otherwise jump to next pattern.

For the input "Hi bro, one two three! one two three! yo! Bye", this program output "Konichiwa bro, ichi ni san! ichi ni san! yo! Sayonara".
