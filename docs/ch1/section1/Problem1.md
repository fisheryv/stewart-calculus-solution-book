<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 1</h4>

If $f(x) = x+\sqrt{2-x}$ and $g(u)=u+\sqrt{2-u}$, is it true that $f = g$?

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

Yes, $f = g$.

Think of function as a machine. 

```mermaid
flowchart LR
    input([input])
    func[function]
    output([output])
    input --> func
    func --> output
```

For any valid input, functions $f$ and $g$ produce identical outputs; Therefore, by the definition of function, $f = g$. 

</div>

> Remark
> 
> In pure mathematics, function is defined as a **relation**, which is essentially a set of **ordered pairs**. Here is the formal definition:
>
> <div class="alert alert-primary" role="alert">
>
> Let $A, B$ be sets and $f$ is a relation between $A$ and $B$. If $f$ has the property that
> $$
> \forall a \in A \centerdot \exist! b \in B \centerdot (a,b) \in f
> $$
> then $f$ is called a **function** from $A$ to $B$.
>
> We called $A$ the **domain** of the function and $B$ the **codomain** of the function.
> 
> </div>
>
> Defining a function requires specifying three essential elements, which are **domain**, **codomain**, and the **mapping rule**. 
>
> From a purely mathematical perspective, $f$ and $g$ in this problem are not well-defined because the domain and codomain are not specified. If we define $f: \mathbb{R}^{-} \to \mathbb{R}$ and $g: \mathbb{R} \to \mathbb{C}$, then they are not the same function!
>
> In the context of calculus and elementary algebra, if the domain and codomain of a function are not explicitly stated, they are generally assumed to be the largest reasonable sets. Therefore, under this default assumption, the two functions in this problem share the same domain and codomain, and of course they are equal.
