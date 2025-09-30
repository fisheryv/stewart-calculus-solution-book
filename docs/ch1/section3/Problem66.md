<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 66</h4>

If you invest $x$ dollars at $4\%$ interest compounded annually, then the amount $A(x)$ of the investment after one year is $A(x) = 1.04x$. Find $A \circ A$, $A \circ A \circ A$, and $A \circ A \circ A \circ A$. What do these compositions represent? Find a formula for the composition of $n$ copies of $A$.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

This is a typical compound interest calculation.

$A \circ A = A(A(x)) = 1.04(1.04x) = 1.04^2x$

$A \circ A \circ A = A(A(A(x))) = 1.04(1.04(1.04x)) = 1.04^3x$

$A \circ A \circ A \circ A = A(A(A(x))) = 1.04(1.04(1.04(1.04x))) = 1.04^4x$

It is not difficult to find out $\underbrace{A \circ A \circ \dots \circ A}_{n}(x)=1.04^nx$ by induction. 

> ✏️Remark
> 
> We can further get the formula of compound interest:
>
> $$ T(n, x)=(1+r)^n(x) $$
>
> where $r$ is then annual interest, $n$ is the term (year), $x$ is the principal and $T$ is the amount with interest after $n$ years. 

</div>

