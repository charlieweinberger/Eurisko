calcList n = [[x, y] | x <- [-n..n], y <- [-n..n], x - y <= (x * y) / 2, x + y >= (x * y) / 2, not (x `elem` [-2..2]), not (y `elem` [-2..2]) ]

main = print (length(calcList 50))