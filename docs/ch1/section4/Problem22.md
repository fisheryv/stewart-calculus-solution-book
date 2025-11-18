<div class="alert alert-warning" role="alert">
<h4 class="alert-heading">Problem 22</h4>

Suppose you are offered a job that lasts one month. Which of the following methods of payment do you prefer?

I. One million dollars at the end of the month.

II. One cent on the first day of the month, two cents on the second day, four cents on the third day, and, in general, $2^{n-1}$ cents on the $n$th day.

</div>

<div class="alert alert-success" role="alert">
<h4 class="alert-heading">Solution</h4>

The essence of this problem is to determine which of the two payment methods results in a higher total amount received. 

- For the first option, the total amount is $1,000,000$ in total. 

- For the second option, the total amount is (assume a month has $30$ days)

    $$
    \sum_{n=1}^{30} 2^{n-1} = 2^n-1 = 2^{30} - 1 = 1073741823 \text{\ (cents)} \approx 10,737,418 \text{\ (dollars)}
    $$

    Even though February has only $28$ days, the total amount of the second option is 

    $$
    \sum_{n=1}^{28} 2^{n-1} = 2^n-1 = 2^{28} - 1 = 268435454 \text{\ (cents)} \approx 2,684,355 \text{\ (dollars)}
    $$

Clearly, the total amount of the second option is much more than that of the first option, so the second option should be chosen.

</div>
