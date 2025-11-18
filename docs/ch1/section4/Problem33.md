<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">📈 Problem 33</h4>

If you graph the function

$$
f(x) = \frac{1-e^{1/x}}{1+e^{1/x}}
$$

you'll see that $f$ appears to be an odd function. Prove it.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

![](_media/screenshots/10-01-2025%20Image074.jpg ':class=img-center')

Proof.

$$
\begin{aligned}
f(-x) &= \frac{1-e^{1/-x}}{1+e^{1/-x}} =\frac{1-\frac{1}{\sqrt[x]{e}}}{1+\frac{1}{\sqrt[x]{e}}} \\
&=\frac{\frac{\sqrt[x]{e}-1}{\sqrt[x]{e}}}{\frac{\sqrt[x]{e}+1}{\sqrt[x]{e}}} = \frac{\sqrt[x]{e}-1}{\sqrt[x]{e}+1}\\ 
&=-\frac{1-\sqrt[x]{e}}{1+\sqrt[x]{e}} \\
&=-\frac{1-e^{1/x}}{1+e^{1/x}} \\
&=-f(x)
\end{aligned}
$$

Therefore, $f(x)$ is an odd function, as required. $\blacksquare$

</div>
