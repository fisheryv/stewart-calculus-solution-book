<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 30</h4>

In a normal respiratory cycle the volume of air that moves into and out of the lungs is about $500$ mL. The reserve and residue volumes of air that remain in the lungs occupy about $2000$ mL and a single respiratory cycle for an average human takes about $4$ seconds. Find a model for the total volume of air $V(t)$ in the lungs as a function of time.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

$V(t)$ is a periodic function with a period of $4$ seconds. We can find $V(t)$ by applying appropriate transformations to the function $\sin x$.

First, we scale the function period from $2\pi$ to $4$

$$
V(t) = \sin\Big(\frac{2\pi}{4}t\Big) = \sin\Big(\frac{\pi t}{2}\Big)
$$

Then, since volume of air that moves into and out of the lungs is about $500$ mL, we know the amplitude is $\frac{500}{2} = 250$. Increasing amplitude from $1$ to $250$, we get

$$
V(t) = 250\sin\Big(\frac{\pi t}{2}\Big)
$$

Finally, since the reserve and residue volumes of air that remain in the lungs occupy about $2000$ mL, which can be understood as the minimum volume of air in lung, so the average volume of air is $2000+\frac{500}{2} = 2250$. We can shift $2250$ units upward

$$
V(t) = 250\sin\Big(\frac{\pi t}{2}\Big)+2250
$$

</div>

