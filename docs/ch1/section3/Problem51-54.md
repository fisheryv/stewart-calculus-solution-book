<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 51-54</h4>

Express the function in the form $f \circ g \circ h$.

51. $\displaystyle R(x)=\sqrt{\sqrt{x}-1}$

52. $\displaystyle H(x)=\sqrt[8]{2+|x|}$

53. $\displaystyle S(t)=\sin^2(\cos t)$

54. $\displaystyle H(t)=\cos(\sqrt{\tan x}+1)$

</div>


<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

**Problem 51**

$$
R(x)=\sqrt{\underbrace{\overbrace{\sqrt{x}}^{h(x)}-1}_{g(x)}} \Bigg \rbrace f(x)
$$

Therefore, $f(x) = \sqrt{x}$, $g(x)=x-1$ and $h(x)=\sqrt{x}$.

----

**Problem 52**

$$
H(x)=\sqrt[8]{\underbrace{2+\overbrace{|x|}^{h(x)}}_{g(x)}} \Bigg \rbrace f(x)
$$

Therefore, $f(x) = \sqrt[8]{x}$, $g(x)=2+x$ and $h(x)=|x|$.

----

**Problem 53**

$$
S(t)=\sin^2(\cos t)= \underbrace{\big(\overbrace{\sin(\underbrace{\cos t}_{h(x)})}^{g(x)}\big)^2}_{f(x)}
$$

Therefore, $f(t) = t^2$, $g(t)=\sin t$ and $h(t)=\cos t$.

----

**Problem 54**

$$
H(t)=\underbrace{\cos(\overbrace{\sqrt{\underbrace{\tan x}_{h(x)}}+1}^{g(x)})}_{f(x)}
$$

Therefore, $f(t) = \cos t$, $g(t)=\sqrt{t}+1$ and $h(t)=\tan t$.

</div>

