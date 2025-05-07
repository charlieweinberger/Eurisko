-- Check the first elements of each list, and make the lesser one the next element, then merge the lists that remain.

merge (x:xs) (y:ys) = if x < y
                        then x:(merge xs (y:ys))
                        else y:(merge ys (x:xs))

merge [] xs = xs
merge xs [] = xs

main = print(merge [1,2,5,8] [3,4,6,7,10])
-- should return [1,2,3,4,5,6,7,8,9,10]