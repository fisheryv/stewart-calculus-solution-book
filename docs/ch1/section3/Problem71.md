<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 71</h4>

Let $f(x)$ be a function with domain $\mathbb{R}$. 

1. Show that $E(x) = f(x) + f(-x)$ is an even function.

2. Show that $O(x) = f(x) - f(-x)$ is an odd function.

3. Prove that every function $f(x)$ can be written as a sum of an even function and an odd function.

4. Express the function $f(x) = 2^x + (x - 3)^2$ as a sum of an even function and an odd function.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

1. Function $f$ is an event function if and only if $f(-x) = f(x)$. 

    For $E(x) = f(x) + f(-x)$, we get

    $$
    E(-x) = f(-x)+f(-(-x)) = f(-x) + f(x) = f(x) + f(-x) = E(x)
    $$

    That shows $E(x)$ is an even function. $\blacksquare$

2. Function $f$ is an odd function if and only if $f(-x) = -f(x)$. 

    For $O(x) = f(x) - f(-x)$, we get

    $$
    O(-x) = f(-x)-f(-(-x)) = f(-x) - f(x) = -(f(x) - f(-x)) = -O(x)
    $$

    That shows $O(x)$ is an odd function. $\blacksquare$

3. According to the above 2 conclusions, we know every even function can be expressed as 
    $$E(x) = f(x) + f(-x) \tag{1}$$
    and every even function can be expressed as 
    $$O(x) = f(x) - f(-x) \tag{2}$$

    $(1) + (2)$ yields
    $$
    E(x)+O(x) = f(x) + f(-x) + f(x) - f(-x) = 2f(x) \\
    f(x)=\frac{1}{2}E(x) + \frac{1}{2}O(x)
    $$

    Since function $f(x)$ is arbitary, that shows every function $f(x)$ can be written as a sum of an even function and an odd function. $\blacksquare$

4. According to the conclusions above, for every function $f(x)$, $f(x)=\frac{1}{2}E(x) + \frac{1}{2}O(x)$, where $E(x) = f(x) + f(-x)$ and $O(x) = f(x) - f(-x)$. 

    If $f(x) = 2^x + (x - 3)^2$, we can express

    $$
    \begin{aligned}
    E(x) &= f(x) + f(-x) \\
    &=2^x + (x - 3)^2 + 2^{-x} + (-x - 3)^2 \\
    &=2^x + 2^{-x} + 2x^2 + 18
    \end{aligned}
    $$

    $$
    \begin{aligned}
    O(x) &= f(x) - f(-x) \\
    &=2^x + (x - 3)^2 - 2^{-x} - (-x - 3)^2 \\
    &=2^x - 2^{-x} - 12x
    \end{aligned}
    $$

    Therefore, $f(x) = 2^x + (x - 3)^2$ can be expressed as 
    $$\frac{1}{2}E(x) = \frac{1}{2} (2^x + 2^{-x} + 2x^2 + 18) = 2^{x-1}+2^{-x-1}+x^2+9$$
    add
    $$\frac{1}{2}O(x) = \frac{1}{2} (2^x - 2^{-x} - 12x) = 2^{x-1}-2^{-x-1}-6x$$

</div>

