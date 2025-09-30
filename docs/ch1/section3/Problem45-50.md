<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 45-50</h4>

Express the function in the form $f \circ g$.

45. $\displaystyle F(x) = (2x + x^2)^4$

46. $\displaystyle F(x) = \cos^2x$

47. $\displaystyle F(x) = \frac{\sqrt[3]{x}}{1+\sqrt[3]{x}}$

48. $\displaystyle G(x) = \sqrt[3]{\frac{x}{1+x}}$

49. $\displaystyle v(t) = \sec(t^2)\tan(t^2)$

50. $\displaystyle H(x) = \sqrt{1+\sqrt{x}}$

</div>


<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

**Problem 45**

$$
F(x) = \underbrace{(\overbrace{2x + x^2}^{g(x)})^4}_{f(x)}
$$

Therefore, $f(x) = x^4$ and $g(x)=2x + x^2$.

----

**Problem 46**

$$
F(x) = \cos^2x = \underbrace{(\overbrace{\cos x}^{g(x)})^2}_{f(x)}
$$

Therefore, $f(x) = x^2$ and $g(x)=\cos x$.

----

**Problem 47**

$$
F(x) = \underbrace{\frac{\overbrace{\sqrt[3]{x}}^{g(x)}}{1+\underbrace{\sqrt[3]{x}}_{g(x)}}}_{f(x)}
$$

Therefore, $f(x) = \frac{x}{1+x}$ and $g(x)=\sqrt[3]{x}$.

----

**Problem 48**

$$
G(x) = \underbrace{\sqrt[3]{\frac{x}{1+x}}}_{f(x)} \Big\rbrace \small{g(x)}
$$

Therefore, $f(x) = \sqrt[3]{x}$ and $g(x)=\frac{x}{1+x}$.

----

**Problem 49**

$$
v(t) = \underbrace{\sec(\overbrace{t^2}^{g(x)})\tan(\overbrace{t^2}^{g(x)})}_{f(x)}
$$

Therefore, $f(t) = \sec t \tan t$ and $g(t)=t^2$.

----

**Problem 50**

$$
H(x) = \underbrace{\sqrt{1+\sqrt{x}}}_{f(x)} \big\rbrace \small{g(x)}
$$

Therefore, $f(x) = \sqrt{1+x}$ and $g(x)=\sqrt{x}$.

!> Be careful! We cannot define $f(x) = \textcolor{red}{\sqrt{x}}$ and $g(x)=1+\textcolor{red}{\sqrt{x}}$, because this will lead to **circular references**.


</div>

