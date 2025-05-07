crossProduct :: (Num a) => (a, a, a) -> (a, a, a) -> (a, a, a) 
crossProduct (x1,x2,x3) (y1,y2,y3) = (x2 * y3 - x3 * y2, x3 * y1 - x1 * y3, x1 * y2 - x2 * y1)
main = print (crossProduct (1,2,3) (3,2,1))