<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">💻 Problem 29</h4>

The table shows (lifetime) peptic ulcer rates (per $100$ population) for various family incomes as reported by the National Health Interview Survey.

1. Make a scatter plot of these data and decide whether a linear model is appropriate.

2. Find and graph a linear model using the first and last data points.

3. Find and graph the regression line.

4. Use the linear model in part (3) to estimate the ulcer rate for people with an income of $\$25,000$.

5. According to the model, how likely is someone with an income of $\$80,000$ to suffer from peptic ulcers?

6. Do you think it would be reasonable to apply the model to someone with an income of $\$200,000$?

</div>

|  Income | Ulcer rate <br> (per 100 population) |
| ------: | -----------------------------------: |
| $4,000  | 14.1                                 |
| $6,000  | 13.0                                 |
| $8,000  | 13.4                                 |
| $12,000 | 12.5                                 |
| $16,000 | 12.0                                 |
| $20,000 | 12.4                                 |
| $30,000 | 10.5                                 |
| $45,000 | 9.4                                  |
| $60,000 | 8.2                                  |

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

1. ![](_media/screenshots/26-08-2025%20Image011.jpg)

2. ![](_media/screenshots/26-08-2025%20Image012.jpg)

    The linear model is $$ f(x)=-0.000105x+14.5214 $$

3. ![](_media/screenshots/26-08-2025%20Image013.jpg)

    The linear regression model is $$ f(x)=-0.0001x+13.9508 $$

4. Substituting $25000$ to  $f(x)=-0.0001x+13.9508$ yields:

    $$
    f(25000)=-0.0001 \cdot 25000 + 13.9508 = 11.4508
    $$

    The ulcer rate for people with an income of $\$25,000$ is about $11.4508$.

5. Substituting $80000$ to  $f(x)=-0.0001x+13.9508$ yields:

    $$
    f(80000)=-0.0001 \cdot 80000 + 13.9508 = 5.9508
    $$

    The ulcer rate for people with an income of $\$80,000$ is about $5.9508$.

6. Substituting $200000$ to $f(x)=-0.0001x+13.9508$ yields:

    $$
    f(200000)=-0.0001 \cdot 200000 + 13.9508 = -6.0492 < 0
    $$

    This is obviously unreasonable. The detection rate of peptic ulcers per hundred people cannot be less than 0. Using an inverse proportional function for regression here would be better, as it ensures that the function value is always greater than 0.

    ![](_media/screenshots/26-08-2025%20Image014.jpg)

</div>

