<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 61</h4>

A ship is moving at a speed of $30$ km/h parallel to a straight shoreline. The ship is $6$ km from shore and it passes a lighthouse at noon.

1. Express the distance $s$ between the lighthouse and the ship as a function of $d$, the distance the ship has traveled since noon; that is, find $f$ so that $s = f(d)$.

2. Express $d$ as a function of $t$, the time elapsed since noon; that is, find $g$ so that $d = g(t)$.

3. Find $f \circ g$. What does this function represent?

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

1. The distance from the ship to the lighthouse $d$, the sailing distance $d$ and the distance from the ship to the shore (which is $6$ km) meet the Pythagorean theorem.
    $$s^2 = d^2 + 6^2$$
    Therefore, $s = f(d) = \sqrt{d^2 + 36}$

2. Since the speed of the ship is $30$ km/h, the sailing distance of the ship $d = g(t) = 30t$.

3. $(f \circ g)(t) = f(g(t)) = \sqrt{(30t)^2 + 36} = \sqrt{900t^2 + 36}$

    This function represents the distance from the ship to the lighthouse as a function of the time elapsed since noon.

</div>

