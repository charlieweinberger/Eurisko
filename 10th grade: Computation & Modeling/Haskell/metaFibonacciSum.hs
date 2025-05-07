fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

firstKEntriesOfSequence k = [ fib a | a <- [0..k] ] -- [0,1,1,2,3,5,8]
kthPartialSum k = sum (firstKEntriesOfSequence k) -- 20
termsToAddInMetaSum n = [ kthPartialSum (fib k) | k <- [0..n] ] -- [0,1,1,2,4,12,54]
metaSum n = sum (termsToAddInMetaSum n) -- 74

main = print (metaSum 6)