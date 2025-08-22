<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 59-64</h4>

Find a formula for the function whose graph is the given curve.

59. The line segment joining the points $(1, -3)$ and $(5, 7)$

60. The line segment joining the points $(-5, 10)$ and $(7, -10)$

61. The bottom half of the parabola $x+(y-1)^2=0$

62. The top half of the circle $x^2+(y-2)^2=4$

![](_media/fig9.png ':size=100%')

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

**Problem 59**

Linear equations are typically expressed in two forms:

- **Point-slope form:** $y - y_0 = k(x - x_0)$, where $k$ is the slope, and $(x_0, y_0)$ is a point on the line.

- **Slope-intercept form:** $y = kx + b$, where $k$ is the slope, and $b$ is the y-intercept.

There are three ways to solve the problem: 

<!-- tabs:start -->

#### **Solution 1**

The slope $k = \frac{y_1 - y_2}{x_1 - x_2} = \frac{-3-7}{1-5} = \frac{5}{2}$. Select any point, for example $(1,-3)$, and substitute it into the point-slope form, we get:

$$ 
\begin{align*}
y-(-3) &= \frac{5}{2}(x-1) \\
y &= \frac{5}{2}x - \frac{5}{2} - 3 \\ 
y &= \frac{5}{2}x - \frac{11}{2}
\end{align*}
$$

Cutting off the line segment from the straight line yields

$$ y = \frac{5}{2}x - \frac{11}{2} \quad (1 \le x \le 5) $$

#### **Solution 2**

The slope $k = \frac{y_1 - y_2}{x_1 - x_2} = \frac{-3-7}{1-5} = \frac{5}{2}$. Hence the slope-intercept form can be written as $y = \frac{5}{2}x + b$. Substitute any point to solve for $b$. 

$$
\begin{align*}
-3 &= \frac{5}{2} \cdot 1 + b \\
b &= -3 - \frac{5}{2} = -\frac{11}{2}
\end{align*}
$$

Therefore, the formular of the line segment is

$$ y = \frac{5}{2}x - \frac{11}{2} \quad (1 \le x \le 5) $$

#### **Solution 3**

Directly use the slope-intercept form, substitute the two points to construct a system of linear equations, and solve for $k$ and $b$.

$$
\begin{cases}
-3 = \enspace k+b \\
\;\;\:7 = 5k+b
\end{cases} \implies
\begin{cases}
k = \frac{5}{2} \\
b = - \frac{11}{2}
\end{cases}
$$

Therefore, the formular of the line segment is

$$ y = \frac{5}{2}x - \frac{11}{2} \quad (1 \le x \le 5) $$

<!-- tabs:end -->

--------

**Problem 60**

Same as the previous problem, $$ y = -\frac{5}{3}x+\frac{5}{3} \quad (-5 \le x \le 7)$$

--------

**Problem 61**

The bottom half means $y-1 \le 0$. Therefore, the original equation can be rearranged as: 

$$
\begin{align*}
x+(y-1)^2 & = 0 \\
(y-1)^2 &= -x \\ 
y-1 &= -\sqrt{-x} &\quad (x \le 0)\\
y &= 1 -\sqrt{-x} &\quad (x \le 0)
\end{align*}
$$

--------

**Problem 62**

The top half means $y-2 \ge 0$. Therefore, the original equation can be rearranged as:

$$
\begin{align*}
x^2+(y-2)^2 &= 4 \\
(y-2)^2 &= 4 - x^2 \\ 
y-2 &= \sqrt{4-x^2} &\quad (-2 \le x \le 2)\\
y &= 2 +\sqrt{4-x^2} &\quad (-2 \le x \le 2)
\end{align*}
$$

--------

**Problem 63**

This is a piecewise function with a break point at $(3, 0)$. 

- For $x < 3$, take a point on the line $(0, 3)$. Using the method introduced in Problem 59, the equation of the line is:
    $$ y=-x+3 $$
- For $x \ge 3$, take a point on the line $(5, 4)$. Similarly, the equation of the line is:
    $$ y=2x-6 $$

Thus, the function expression is:

$$
y = \begin{cases}
-x+3 &\quad \text{if \ } 0 \le x < 3 \\
2x-6 &\quad \text{if \ } 3 \le x \le 5
\end{cases}
$$

--------

**Problem 64**

This is a piecewise function with two break points at $(-2, 0)$ and $(2,0)$. 

- For $x < -2$, take a point on the line $(-4, 3)$. Using the method introduced in Problem 59, the equation of the line is:
    $$ y=-\frac{3}{2}x-3 $$
- For $x > 2$, take a point on the line $(4, 3)$. Similarly, the equation of the line is:
    $$ y=\frac{3}{2}x-3 $$
- For $-2 \le x \le 2$, the graph shows the upper half of a circle centered at the origin $(0,0)$ with a radius of $2$. The equation of the entire circle is $x^2 + y^2 = 4$, and we take its upper half where $y > 0$,

    $$
    \begin{align*}
    x^2 + y^2 &= 4 \\
    y^2 &= 4 - x^2 \\
    y &= \sqrt{4-x^2} \quad (-2 \le x \le 2)
    \end{align*}
    $$

Thus, the function expression is:

$$
y = \begin{cases}
-\frac{3}{2}x-3 &\quad \text{if \ } -4 \le x < -2 \\
\sqrt{4-x^2} &\quad \text{if \ } -2 \le x \le 2 \\
\frac{3}{2}x-3 &\quad \text{if \ } \quad \: 2 < x \le 4
\end{cases}
$$

</div>

