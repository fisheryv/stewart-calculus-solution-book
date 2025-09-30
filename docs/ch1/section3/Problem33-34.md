<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 33-34</h4>

Find (a) $f + g$, (b) $f - g$, (c) $fg$, and (d) $f/g$ and state their domains.

33. $\displaystyle f(x) = \sqrt{25 - x^2}, \quad g(x) = \sqrt{x + 1}$

34. $\displaystyle f(x) = \frac{1}{x-1}, \quad g(x) = \frac{1}{x}-2$

</div>


<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

**Problem 33**

a. $$
    f+g = \sqrt{25 - x^2} + \sqrt{x + 1}
   $$

   The domain of $f$ is $25 - x^2 \ge 0 \implies -5 \le x \le 5$.

   The domain of $g$ is $x+1 \ge 0 \implies x \ge -1$.

   Therefore, the domain of $f+g$ is $-1 \le x \le 5$.

b. $$
    f-g = \sqrt{25 - x^2} - \sqrt{x + 1}
   $$

   The domain of $f-g$ is the same as $f+g$, that is $-1 \le x \le 5$.

c. $$
    \begin{aligned}
    fg &= \sqrt{25 - x^2} \cdot \sqrt{x + 1}\\
    &=\sqrt{(25 - x^2)(x+1)}\\
    &=\sqrt{−x^3 − x^2 + 25x + 25}
    \end{aligned}
   $$

   The domain of $fg$ is the same as $f+g$, that is $-1 \le x \le 5$.

d. $$
    f/g = \frac{\sqrt{25 - x^2}}{\sqrt{x + 1}} = \sqrt{\frac{25 - x^2}{x + 1}}
   $$

   where $x + 1 \ne 0 \implies x \ne -1$.

   The domain of $f/g$ satisfies
   $$ 
   \begin{cases}
        25 - x^2 \ge 0 \\
        x + 1 > 0
    \end{cases}
    $$
    Therefore, the domain of $f/g$ is $-1 < x \le 5$.

----

**Problem 34**

a. $$
    \begin{aligned}
    f+g &= \frac{1}{x-1} + \frac{1}{x}-2 \\
    &= \frac{1}{x-1} + \frac{1-2x}{x} \\
    &= \frac{x+(x-1)(1-2x)}{x(x-1)} \\
    &= \frac{-2x^2+4x-1}{x^2-x}
    \end{aligned}
   $$

   The domain of $f$ is $x \in \mathbb{R}$ and $x-1 \ne 0$, that is $x \ne 1$.

   The domain of $g$ is $x \in \mathbb{R}$ and $x \ne 0$.

   Therefore, the domain of $f+g$ is $\{x \mid x \in \mathbb{R} \land x \ne 0 \land x \ne 1\}$.

b. $$
    \begin{aligned}
    f+g &= \frac{1}{x-1} - (\frac{1}{x}-2) \\
    &= \frac{1}{x-1} - \frac{1-2x}{x} \\
    &= \frac{x-(x-1)(1-2x)}{x(x-1)} \\
    &= \frac{2x^2-2x+1}{x^2-x}
    \end{aligned}
   $$

   The domain of $f-g$ is the same as $f+g$, that is $\{x \mid x \in \mathbb{R} \land x \ne 0 \land x \ne 1\}$.

c. $$
    \begin{aligned}
    fg &= \frac{1}{x-1} \cdot (\frac{1}{x}-2) \\
    &= \frac{1}{x-1} \cdot \frac{1-2x}{x} \\
    &= \frac{1-2x}{x(x-1)} \\
    &= \frac{1-2x}{x^2-x}
    \end{aligned}
   $$

   The domain of $fg$ is the same as $f+g$, that is $\{x \mid x \in \mathbb{R} \land x \ne 0 \land x \ne 1\}$.

d. $$
    \begin{aligned}
    f/g &= \frac{1}{x-1} / (\frac{1}{x}-2) \\
    &= \frac{1}{x-1} / \frac{1-2x}{x} \\
    &= \frac{1}{x-1} \cdot \frac{x}{1-2x} \\
    &= \frac{x}{(x-1)(1-2x)} \\
    &= \frac{x}{-2x^2+3x-1}
    \end{aligned}
   $$

   where $\frac{1}{x}-2 \ne 0 \implies x \ne \frac{1}{2}$.

   Therefore, the domain of $f/g$ is $\{x \mid x \in \mathbb{R} \land x \ne 0 \land x \ne 1 \land x \ne \frac{1}{2}\}$.

</div>

