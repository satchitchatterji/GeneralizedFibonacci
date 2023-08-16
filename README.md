# GeneralizedFibonacci

The Fibonacci numbers and their properties are very well known, with the popular definition:

$$F_n=F_{n-1}+F_{n-2}$$

With $F_0=0$ and $F_1=1$.

Thus, the [first few](https://oeis.org/A000045) Fibonacci numbers are:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...

The [Binet formula](https://en.wikipedia.org/wiki/Fibonacci_number#Binet's_formula) is also known to produce Fibonacci numbers. Its definition for the <i>nth</i> Fibonacci number is:

$$F_n=\frac{\varphi^n-\psi^n}{\varphi-\psi}=\frac{\varphi^n-\psi^n}{\sqrt{5}}$$

With:

$$\varphi=\frac{1+\sqrt{5}}{2}\approx1.6180339887...$$

$$\psi=\frac{1-\sqrt{5}}{2}=1-\varphi\approx -0.6180339887$$

Usually, the Fibonacci numbers are regarded as a subset of the natural numbers. However, we can input non-natural numbers in this formula as well. With rational numbers, we need to take into account that we will inevitably need to take roots of negative numbers, so we extend our domain into the complex. The traditional Fibonacci numbers are still seen where the graph hits the real axis (no imaginary part).

If we input positive rational numbers, we get:

![fibpos](https://github.com/satchitchatterji/GeneralizedFibonacci/blob/master/fibpos.png)

Interestingly, the graph loops around so that it hits 1 twice. Here we see the first four real Fibonacci numbers formed as well. 

If we input negative rational numbers, we get an interesting spiral pattern, which, unfortunately, is not representative of the <i>other</i> Fibonacci spiral.

![fibneg](https://github.com/satchitchatterji/GeneralizedFibonacci/blob/master/fibneg.png)

We can combine these graphs to create the generalised Fibonacci graph, based on the Binet formula.

![fibnegpos](https://github.com/satchitchatterji/GeneralizedFibonacci/blob/master/fibnegpos.png)
