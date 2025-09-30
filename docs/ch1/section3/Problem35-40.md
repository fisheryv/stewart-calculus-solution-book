<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 35-40</h4>

Find the functions (a) $f \circ g$, (b) $g \circ f$, (c) $f \circ f$, and (d) $g \circ g$ and their domains.

35. $\displaystyle f(x) = x^3+5, \quad g(x) = \sqrt[3]{x}$

36. $\displaystyle f(x) = \frac{1}{x}, \quad g(x) = 2x+1$

37. $\displaystyle f(x) = \frac{1}{\sqrt{x}}, \quad g(x) = x+1$

38. $\displaystyle f(x) = \frac{x}{x+1}, \quad g(x) = 2x-1$

39. $\displaystyle f(x) = \frac{2}{x}, \quad g(x) = \sin x$

40. $\displaystyle f(x) = \sqrt{5-x}, \quad g(x) = \sqrt{x-1}$

</div>


<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

**Problem 35**

The domain of $f(x) = x^3+5$ is $\mathbb{R}$

The domain of $g(x) = \sqrt[3]{x}$ is $\mathbb{R}$

- $\displaystyle f \circ g = f\big(g(x)\big) = (\sqrt[3]{x})^3+5 = x+5 $ 

    The domain of $f \circ g$ is $\mathbb{R}$.

- $\displaystyle g \circ f = g\big(f(x)\big) = \sqrt[3]{x^3+5}$ 

    The domain of $g \circ f$ is $\mathbb{R}$.

- $\displaystyle f \circ f = f\big(f(x)\big) = (x^3+5)^3+5$ 

    The domain of $f \circ f$ is $\mathbb{R}$.

- $\displaystyle g \circ g = g\big(g(x)\big) = \sqrt[3]{\sqrt[3]{x}} = \sqrt[9]{x}$ 

    The domain of $g \circ g$ is $\mathbb{R}$.

----

**Problem 36**

The domain of $f(x) = \frac{1}{x}$ is $\{x \mid x \in \mathbb{R} \land x \ne 0\}$

The domain of $g(x) = 2x+1$ is $\mathbb{R}$

- $\displaystyle f \circ g = f\big(g(x)\big) = \frac{1}{2x+1}$, where $2x+1 \ne 0 \implies x \ne -\frac{1}{2}$

    The domain of $f \circ g$ is $\{x \mid x \in \mathbb{R} \land x \ne -\frac{1}{2}\}$.

- $\displaystyle g \circ f = g\big(f(x)\big) = 2(\frac{1}{x})+1 = \frac{2+x}{x}$, where $x \ne 0$

    The domain of $g \circ f$ is $\{x \mid x \in \mathbb{R} \land x \ne 0\}$.

- $\displaystyle f \circ f = f\big(f(x)\big) = \frac{1}{\frac{1}{x}}=x$, where $x \ne 0$

    The domain of $f \circ f$ is $\{x \mid x \in \mathbb{R} \land x \ne 0\}$.

- $\displaystyle g \circ g = g\big(g(x)\big) = 2(2x+1)+1 = 4x+3$ 

    The domain of $g \circ g$ is $\mathbb{R}$.

----

**Problem 37**

The domain of $f(x) = \frac{1}{\sqrt{x}}$ is $\mathbb{R}^+$

The domain of $g(x) = x+1$ is $\mathbb{R}$

- $\displaystyle f \circ g = f\big(g(x)\big) = \frac{1}{\sqrt{x+1}}$, where $x+1 > 0 \implies x > -1$

    The domain of $f \circ g$ is $\{x \mid x \in \mathbb{R} \land x > -1\}$.

- $\displaystyle g \circ f = g\big(f(x)\big) = \frac{1}{\sqrt{x}}+1$, where $x > 0$

    The domain of $g \circ f$ is $\mathbb{R}^+$.

- $\displaystyle f \circ f = f\big(f(x)\big) = \frac{1}{\sqrt{\frac{1}{\sqrt{x}}}} = \frac{1}{\frac{1}{\sqrt[4]{x}}} = \sqrt[4]{x}$, where $x > 0$

    The domain of $f \circ f$ is $\mathbb{R}^+$.

- $\displaystyle g \circ g = g\big(g(x)\big) = (x+1)+1 = x+2$ 

    The domain of $g \circ g$ is $\mathbb{R}$.

----

**Problem 38**

The domain of $f(x) = \frac{x}{x+1}$ is $\{x \mid x \in \mathbb{R} \land x \ne -1\}$

The domain of $g(x) = 2x-1$ is $\mathbb{R}$

- $\displaystyle f \circ g = f\big(g(x)\big) = \frac{1}{\sqrt{x+1}}$, where $x+1 > 0 \implies x > -1$

    The domain of $f \circ g$ is $\{x \mid x \in \mathbb{R} \land x > -1\}$.

- $\displaystyle g \circ f = g\big(f(x)\big) = \frac{1}{\sqrt{x}}+1$, where $x > 0$

    The domain of $g \circ f$ is $\mathbb{R}^+$.

- $\displaystyle f \circ f = f\big(f(x)\big) = \frac{1}{\sqrt{\frac{1}{\sqrt{x}}}} = \frac{1}{\frac{1}{\sqrt[4]{x}}} = \sqrt[4]{x}$, where $x > 0$

    The domain of $f \circ f$ is $\mathbb{R}^+$.

- $\displaystyle g \circ g = g\big(g(x)\big) = (x+1)+1 = x+2$ 

    The domain of $g \circ g$ is $\mathbb{R}$.

----

**Problem 39**

The domain of $f(x) = \frac{2}{x}$ is $\{x \mid x \in \mathbb{R} \land x \ne 0\}$

The domain of $g(x) = \sin x$ is $\mathbb{R}$

- $\displaystyle f \circ g = f\big(g(x)\big) = \frac{2}{\sin x}$, where $\sin x \ne 0 \implies x \ne k\pi, k \in \mathbb{Z}$

    The domain of $f \circ g$ is $\{x \mid x \in \mathbb{R} \land x \ne k\pi, k \in \mathbb{Z}\}$.

- $\displaystyle g \circ f = g\big(f(x)\big) = \sin(\frac{2}{x})$, where $x \ne 0$

    The domain of $g \circ f$ is $\{x \mid x \in \mathbb{R} \land x \ne 0\}$.

- $\displaystyle f \circ f = f\big(f(x)\big) = \frac{2}{\frac{2}{x}} = x$, where $x \ne 0$

    The domain of $f \circ f$ is $\{x \mid x \in \mathbb{R} \land x \ne 0\}$.

- $\displaystyle g \circ g = g\big(g(x)\big) = \sin(\sin x)$ 

    The domain of $g \circ g$ is $\mathbb{R}$.

----

**Problem 40**

The domain of $f(x) = \sqrt{5-x}$ is $\{x \mid x \in \mathbb{R} \land x \le 5\}$

The domain of $g(x) = \sqrt{x-1}$ is $\{x \mid x \in \mathbb{R} \land x \ge 1\}$

- $\displaystyle f \circ g = f\big(g(x)\big) = \sqrt{5-\sqrt{x-1}}$, where

    $$
    \begin{cases}
        x-1 &\ge 0 \\
        5 - \sqrt{x-1} &\ge 0
    \end{cases} \implies
    \begin{cases}
        x \ge 1 \\
        1 \le x \le 26
    \end{cases} \implies 1 \le x \le 26
    $$

    The domain of $f \circ g$ is $\{x \mid x \in \mathbb{R} \land 1 \le x \le 26\}$.

- $\displaystyle g \circ f = g\big(f(x)\big) = \sqrt{\sqrt{5-x}-1}$, where

    $$
    \begin{cases}
        5-x &\ge 0 \\
        \sqrt{5-x}-1 &\ge 0
    \end{cases} \implies
    \begin{cases}
        x \le 5 \\
        x \le 4
    \end{cases} \implies x \le 4
    $$

    The domain of $g \circ f$ is $\{x \mid x \in \mathbb{R} \land x \le 4\}$.

- $\displaystyle f \circ f = f\big(f(x)\big) = \sqrt{5-\sqrt{5-x}}$, where

    $$
    \begin{cases}
        5-x &\ge 0 \\
        5-\sqrt{5-x} &\ge 0
    \end{cases} \implies
    \begin{cases}
        x \le 5 \\
        -20 \le x \le 5
    \end{cases} \implies -20 \le x \le 5
    $$

    The domain of $f \circ f$ is $\{x \mid x \in \mathbb{R} \land -20 \le x \le 5\}$.

- $\displaystyle g \circ g = g\big(g(x)\big) = \sqrt{\sqrt{x-1}-1}$, where

    $$
    \begin{cases}
        x-1 &\ge 0 \\
        \sqrt{x-1}-1 &\ge 0
    \end{cases} \implies
    \begin{cases}
        x \ge 1 \\
        x \ge 2
    \end{cases} \implies x \ge 2
    $$

    The domain of $g \circ g$ is $\{x \mid x \in \mathbb{R} \land x \ge 2\}$.

</div>

