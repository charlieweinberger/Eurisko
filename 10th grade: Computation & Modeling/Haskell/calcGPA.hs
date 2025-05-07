gradeToNum :: (Num a) => String -> a  
gradeToNum grade
    | grade=="A" = 4
    | grade=="B" = 3
    | grade=="C" = 2
    | grade=="D" = 1
    | otherwise = 0

calcGPA gradeList = (sum ([ gradeToNum x | x <- gradeList ]) `div` length(gradeList))

main = print (calcGPA ["A", "B", "B", "C", "C", "C", "D", "F"])