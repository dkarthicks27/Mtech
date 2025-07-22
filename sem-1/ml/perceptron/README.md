## What's a Perceptron Really?

The simplest definition of a Perceptron is that, Its an algorithm for learning a binary classifier called a threshold function. 

### Definition

![{\displaystyle f(\mathbf {x} )=h(\mathbf {w} \cdot \mathbf {x} +b)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/109cd4ab4495d18c8231b64ae33042e888b526bb)

where $H(x) = \begin{cases} 1, & x \geq 0 \\ 0, & x < 0 \end{cases}$

The H(x) here is the unit step function or the heaviside function. We need to get a binary value as the value of f(x)

### Deep Dive

x - is a real valued vector

f(x) - a single binary value (either 0 or 1)
