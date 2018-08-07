
primes :: [Integer]
primes = filterPrime [2..]
  where
    filterPrime (x:xs) = x : filterPrime [n | n <- xs, n `mod` x /= 0]

firstPrimes :: [Integer]
firstPrimes = take 1000 primes
