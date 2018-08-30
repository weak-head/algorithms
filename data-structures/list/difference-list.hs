import Prelude hiding (concat, foldr, map, replicate)
import qualified Data.List as L

-- | Difference list supports O(1) append and snoc time.
--
newtype DList a = DList { unDL :: [a] -> [a] }

-- | O(1)
empty :: DList a
empty = DList id

-- | O(1)
singleton :: a -> DList a
singleton = DList . (:)

-- |
apply :: DList a -> [a] -> [a]
apply = unDL

-- | O(1)
cons :: a -> DList a -> DList a
cons a dl = DList $ (a:) . unDL dl

-- | O(1)
snoc :: DList a -> a -> DList a
snoc dl a = DList $ unDL dl . (a:)

-- | O(1)
append :: DList a -> DList a -> DList a
append a b = DList $ unDL a . unDL b

-- | O(spine)
concat :: [DList a] -> DList a
concat = L.foldr append empty

-- | O(n)
replicate :: Int -> a -> DList a
replicate n a
  | n == 0    = empty
  | otherwise = cons a (replicate (n-1) a)

-- | O(n)
map :: (a -> b) -> DList a -> DList b
map f = foldr (cons . f) empty

-- | O(n)
foldr :: (a -> b -> b) -> b -> DList a -> b
foldr f b = L.foldr f b . ($[]) . unDL

-- |
toList :: DList a -> [a]
toList = ($[]) . unDL

-- |
fromList :: [a] -> DList a
fromList = DList . (++)

----------------------------------------

example :: IO ()
example = do
  let d1 = cons (1::Int) empty  -- 1
      d2 = cons 2 d1            -- 2 1
      d3 = cons 3 d2            -- 3 2 1
      d4 = snoc d3 0            -- 3 2 1 0
      d5 = append d4 d4         -- 3 2 1 0 3 2 1 0
      d6 = map (+1) d5          -- 4 3 2 1 4 3 2 1
      d7 = replicate 3 (replicate 3 (5::Int)) -- [5 5 5] [5 5 5] [5 5 5]
      d8 = concat $ toList d7   -- 5 5 5 5 5 5 5 5 5
      d9 = append d6 d8         -- 4 3 2 1 4 3 2 1 5 5 5 5 5 5 5 5 5
      df = foldr (+) 0 d9       -- 65

  print $ toList d1
  print $ toList d2
  print $ toList d3
  print $ toList d4
  print $ toList d5
  print $ toList d6
  print $ toList $ map toList d7
  print $ toList d8
  print $ toList d9
  print df