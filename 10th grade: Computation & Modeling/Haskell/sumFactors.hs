findFactors n = [x | x <- [1..n], (n `mod` x) == 0]

sumFactors n = sum (findFactors n)

main = print(sumFactors 10)
should be 1 + 2 + 5 + 10 = 18