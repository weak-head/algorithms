import Control.Monad.Loops (iterateUntilM)

-- | Priority queue that is based on linked-list.
--
--  Insert: O(1)
--  Find/Peek: O(1)
--  Delete: O(n)
--
newtype PQueue a = PQueue { getQueue :: [a] }
  deriving (Show, Eq, Ord)

-- | O(1)
empty :: PQueue a
empty = PQueue []

-- | O(1)
insert :: Ord a => PQueue a -> a -> PQueue a
insert (PQueue []) a = PQueue [a]
insert (PQueue (x:xs)) a
  | x < a     = PQueue (x:a:xs)
  | otherwise = PQueue (a:x:xs)

-- | O(1)
peek :: PQueue a -> Maybe a
peek (PQueue [])    = Nothing
peek (PQueue (x:_)) = Just x

-- | O(n)
deleteMin :: Ord a => PQueue a -> PQueue a
deleteMin (PQueue [])       = PQueue []
deleteMin (PQueue [x])      = PQueue []
deleteMin (PQueue (_:x:xs)) = PQueue $ go x xs []
  where go m [] ys = m:ys
        go m (x:xs) ys
          | x < m     = go x xs (m:ys)
          | otherwise = go m xs (x:ys)


main :: IO ()
main = do
  let queue = foldl insert empty [5, 4, 3, 1, 7, 2]
  print queue

  iterateUntilM (null . getQueue)
                (\q -> do
                  let q' = deleteMin q
                  print q' >> return q')
                queue
  return ()