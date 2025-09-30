<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 29</h4>

Some of the highest tides in the world occur in the Bay of Fundy on the Atlantic Coast of Canada. At Hopewell Cape the water depth at low tide is about $2.0$ m and at high tide it is about $12.0$ m. The natural period of oscillation is about $12$ hours and on a particular day, high tide occurred at 6:45 am. Find a function involving the cosine function that models the water depth $D(t)$ (in meters) as a function of time $t$ (in hours after midnight) on that day.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

We find the function $D(t)$ by applying appropriate transformations to the function $\cos x$.

First, since the natural period of oscillation is about $12$ hours, we scale the function period from $2\pi$ to $12$

$$D(t) = \cos \Big(\frac{2\pi}{12} t\Big) = \cos \Big(\frac{\pi}{6}t\Big) $$

Then, since the low tide is about $2.0$ m and the high tide is about $12.0$ m, we know the amplitude is $\frac{12-2}{2} = 5$ and the average depth is $\frac{12+2}{2} = 7$. Stretching vertically by a factor of $5$ and shifting $7$ units upward yields

$$D(t) = 5\cos \Big(\frac{\pi}{6}t\Big)+7$$

Finally, since high tide occurred at 6:45 am ($6.75$ hours after midnight), we can shift $6.75$ units to the right

$$D(t) = 5\cos \Big(\frac{\pi}{6}(t-6.75)\Big)+7$$

</div>

