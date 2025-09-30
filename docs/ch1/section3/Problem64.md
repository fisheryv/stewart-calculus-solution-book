<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 64</h4>

**The Ramp Function**

The Heaviside function defined in [Exercise 63](/docs/ch1/section3/Problem63.md) can also be used to define the *ramp function* $y = ctH(t)$, which represents a gradual increase in voltage or current in a circuit.

1. Sketch the graph of the ramp function $y = tH(t)$.

2. Sketch the graph of the voltage $V(t)$ in a circuit if the switch is turned on at time $t = 0$ and the voltage is gradually increased to $120$ volts over a 60-second time interval. Write a formula for $V(t)$ in terms of $H(t)$ for $t < 60$.

3. Sketch the graph of the voltage $V(t)$ in a circuit if the switch is turned on at time $t = 7$ seconds and the voltage is gradually increased to $100$ volts over a period of $25$ seconds. Write a formula for $V(t)$ in terms of $H(t)$ for $t < 32$.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

1.  $$
    y = tH(t)= \begin{cases}
    0 & \text{if\ } t<0\\
    t & \text{if\ } t \ge 0
    \end{cases}
    $$

    ![](_media/graph32-1.png ':size=70% :class=img-center')

2.  $$
    V(t) = \begin{cases}
    0 & \text{if\ } t<0\\
    2t & \text{if\ } 0 \le t \le 60
    \end{cases} = 2tH(t)
    $$

    ![](_media/graph32-2.png ':size=70% :class=img-center')

3.  $$
    V(t) = \begin{cases}
    0 & \text{if\ } t<7\\
    4t & \text{if\ } 7 \le t \le 32
    \end{cases} = 4(t-7)H(t-7)
    $$

    ![](_media/graph32-3.png ':size=70% :class=img-center')

</div>

