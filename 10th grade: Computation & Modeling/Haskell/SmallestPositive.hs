findSmallestPositive :: (Num a, Ord a) => [a] -> a
findSmallestPositive [] = error "findSmallestPositive of empty list"  
findSmallestPositive [x] = x  
findSmallestPositive (x:xs)   
    | 0 < x && x <= smallestPositiveTail = x  
    | otherwise = smallestPositiveTail  
    where smallestPositiveTail = findSmallestPositive xs

main = print (findSmallestPositive [8, 3, -1, 2, -5, 7])