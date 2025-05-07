-- takes a list returns the squares of the values that are less than 10.
squareSingleDigitNumbers x = map (^2) ( filter (<10) x )

main = print(squareSingleDigitNumbers [2, 7, 15, 11, 5]) -- [4, 49, 25]