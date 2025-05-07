nthFibonacciNumber :: (Integral a) => a -> a  
nthFibonacciNumber 0 = 0
nthFibonacciNumber 1 = 1
nthFibonacciNumber n = nthFibonacciNumber(n - 2) + nthFibonacciNumber(n - 1)
main = print (nthFibonacciNumber 20)