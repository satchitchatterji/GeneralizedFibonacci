# GeneralizedFibonacci

The Fibonacci numbers and their properties are very well known, with the popular definition:

![fib](https://wikimedia.org/api/rest_v1/media/math/render/svg/0fff1a1716fcc169546079870357f92757ade5fa)

With ![startfib](https://wikimedia.org/api/rest_v1/media/math/render/svg/3c667d91153450b3a161371582ee8227af85951f)

Thus, the [first few](https://oeis.org/A000045) Fibonacci numbers are:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...

The [Binet formula](https://en.wikipedia.org/wiki/Fibonacci_number#Binet's_formula) is also known to produce Fibonacci numbers. Its definition for the <i>nth</i> Fibonacci number is:

![Binet Formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/ccab7a6cd419ca36abdddee5f576e9e63220f88f)

Usually, the Fibonacci numbers are regarded as a subset of the natural numbers. However, we can input non-natural numbers in this formula as well. With rational numbers, we need to take into account that we will inevitably need to take roots of negative numbers, so we extend our domain into the complex. The traditional Fibonacci numbers are still seen where the graph hits the real axis (no imaginary part).

If we input positive rational numbers, we get:

![fibpos](https://github.com/satchitchatterji/GeneralizedFibonacci/blob/master/fibpos.png)

The graph loops around so that it hits 1 twice. 

If we input negative rational numbers, we get an interesting spiral pattern, which, unfortunately, is not representative of the <i>other</i> Fibonacci spiral.

![fibneg](https://github.com/satchitchatterji/GeneralizedFibonacci/blob/master/fibneg.png)

We can combine these graphs to create the generalised Fibonacci graph, based on the Binet formula.

![fibnegpos](https://github.com/satchitchatterji/GeneralizedFibonacci/blob/master/fibnegpos.png)
