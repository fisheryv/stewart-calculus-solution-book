<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 27</h4>

The city of New Orleans is located at latitude $30 \degree N$. Use Figure 9 to find a function that models the number of hours of daylight at New Orleans as a function of the time of year. To check the accuracy of your model, use the fact that on March 31 the sun rises at 5:51 am and sets at 6:18 pm in New Orleans.

</div>

![](_media/fig10.png ':size=80% :class=img-center')

<p align="center">
FIGURE 9. Graph of the length of daylight from March 21 through December 21 at various latitudes
<small>Source: Adapted from L. Harrison, Daylight, Twilight, Darkness and Time (New York: Silver, Burdett, 1935), 40.</small>
</p>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

$30 \degree N$ corresponds to the red curve in the Figure 9. Its amplitude is $\frac{14-10}{2} = 2$, so the function will be

$$
L(t) = 12 + 2\sin\Bigg[\frac{2\pi}{365}(t-80)\Bigg]
$$

where $t$ represents the day of the year. 

March 31 is the $90$th day of the year, so the model gives

$$
L(90) = 12+2\sin\Bigg[\frac{2\pi}{365}(90-80)\Bigg] \approx 12+2 \cdot 0.1713 = 12.3426
$$

We know that the sun rises at 5:51 am and sets at 6:18 pm in New Orleans on March 31, that is the daylight in New Orleans on March 31 is $12.45$ hours. Then the error rate between the model output and the actual is

$$
\epsilon = \frac{|X-X_0|}{X_0}=\frac{|12.3426 - 12.45|}{12.45} \approx 0.0086
$$

The accuracy of the model is very high.

</div>

