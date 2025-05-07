recommendClothing :: (RealFloat a) => a -> a -> String  
recommendClothing degreesCelsius
    | degreesFahrenheit >= temp1 = "You should wear a shortsleeve shirt."
    | degreesFahrenheit > temp2 = "You should wear a longsleeve shirt."
    | degreesFahrenheit > temp3 = "You should wear a sweater."   
    | otherwise = "You should wear a jacket."  
    where degreesFahrenheit = (9 * degreesCelsius / 5) + 32  
          temp1 = 80
          temp1 = 65
          temp1 = 50