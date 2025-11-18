<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">📈 Problem 25</h4>

Compare the functions $f(x) = x^{10}$ and $g(x) = e^x$ by graphing both functions in several viewing rectangles. When does the graph of $g$ finally surpass the graph of $f$ ?

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

In the normal graphing window, as the figure below, we can see that the two functions have two points of intersection. 

![](_media/screenshots/11-17-2025%20Image004.jpg ':class=img-center')

However, we know that the exponential function grows faster than the power function, so there must be another point of intersection on the positive $x$-axis. Unfortunately, because the $y$-values are too large and exceed the range of the graphing calculator, it cannot be plotted. Therefore, we take the natural logarithm of both functions (the natural logarithm is monotonically increasing) and compare the the two functions by using the results after taking the natural logarithm.

$$
\begin{align*}
\ln(f(x)) &= \ln x^{10}  = 10 \ln x \\
\ln(g(x)) &= \ln e^x = x
\end{align*}
$$

![](_media/screenshots/11-17-2025%20Image003.jpg ':class=img-center')

The figure above shows that when $x > 35.77$, the graph of $g$ finally surpass the graph of $f$.

</div>
