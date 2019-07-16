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
