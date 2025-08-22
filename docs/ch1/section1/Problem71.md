<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 71</h4>

A box with an open top is to be constructed from a rectangular piece of cardboard with dimensions $30$ cm by $50$ cm by cutting out equal squares of side $x$ at each corner and then folding up the sides as in the figure. Express the volume $V$ of the box as a function of $x$.

</div>

![](_media/fig10.png ':size=60% :class=img-center')

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

The volume of a cube is equal to the base area multiplied by the height. In this problem, the height of the box is $x$, and the two sides of the base are obtained by subtracting $2x$ from the two sides of the rectangular cardboard.

Be careful, $2x$ must be less than the shorter side, that is $2x < 30 \implies x < 15$. 

Therefore, the volume of the box is:

$$
\begin{align*}
V &= (50-2x)(30-2x)x\\
&= (1500 - 100x - 60x + 4x^2)x \\
&= 4x^3 - 160x^2 + 1500x \quad \text{where\ } 0<x<15
\end{align*}
$$

</div>
