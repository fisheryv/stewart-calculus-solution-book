<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 67</h4>

1. If $g(x) = 2x + 1$ and $h(x) = 4x^2 + 4x + 7$, find a function $f$ such that $f \circ g = h$. (Think about what operations you would have to perform on the formula for $g$ to end up with the formula for $h$.)

2. If $f(x) = 3x + 5$ and $h(x) = 3x^2 + 3x + 2$, find a function $g$ such that $f \circ g = h$.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

1.  $$
    \begin{aligned}
    h(x) &= (f \circ g) = f(g(x)) \\
    4x^2 + 4x + 7 &= f(2x + 1) \\
    (2x+1)^2 + 6 &= f(2x + 1) \\
    t^2+6 &= f(t)
    \end{aligned}
    $$

    Therefore, $f(x) = x^2+6$

2.  $$
    \begin{aligned}
    h(x) &= (f \circ g) = f(g(x)) \\
    3x^2 + 3x + 2 &= 3g(x) + 5 \\
    3g(x) &= 3x^2 + 3x - 3 \\
    g(x) &= x^2+x-1
    \end{aligned}
    $$

    Therefore, $g(x) = x^2+x-1$

</div>

