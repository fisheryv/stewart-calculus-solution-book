<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 63</h4>

**The Heaviside Function**

The *Heaviside function $H$* is defined by

$$
\begin{cases}
0 & \text{if\ } t<0\\
1 & \text{if\ } t \ge 0
\end{cases}
$$

It is used in the study of electric circuits to represent the sudden surge of electric current, or voltage, when a switch is instantaneously turned on.

1. Sketch the graph of the Heaviside function.

2. Sketch the graph of the voltage $V(t)$ in a circuit if the switch is turned on at time $t = 0$ and $120$ volts are applied instantaneously to the circuit. Write a formula for $V(t)$ in terms of $H(t)$.

3. Sketch the graph of the voltage $V(t)$ in a circuit if the switch is turned on at time $t = 5$ seconds and $240$ volts are applied instantaneously to the circuit. Write a formula for $V(t)$ in terms of $H(t)$. (Note that starting at $t = 5$ corresponds to a translation.)

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

1. ![](_media/graph31-1.png ':size=70% :class=img-center')

2. Let turned on switch for $1$. Whenever the switch is turned on, there is $120$ V current. We can express function $V(t)$ as $V(t) = 120 H(t)$. Its graph is as follows

    ![](_media/graph31-2.png ':size=70% :class=img-center')

3. The switch is turned on at time $t = 5$, and the voltage is $240$ V, so the function $V(t)$ can be expressed as

    $$
    V(t) = \begin{cases}
    0 & \text{if\ } t<5\\
    240 & \text{if\ } t \ge 5
    \end{cases}
    $$

    It is equivalent to stretching vertically by a factor of $240$ and shifting $5$ unit to the right on graph of $H(t)$. Thus, $V(t)$ can be also express as $V(t)=240H(t-5)$.

    ![](_media/graph31-3.png ':size=70% :class=img-center')

</div>

