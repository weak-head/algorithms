import Control.Monad as M
import Data.Bool (bool)
import Data.List as L
import Data.Vector.Unboxed as V
import Data.Vector.Unboxed.Mutable as MV
import System.Random (StdGen, randomRs, getStdGen)


-- | Generates immutable vector of random integers
mkRandomVector :: StdGen -> Int -> V.Vector Int
mkRandomVector g size =
  V.fromList $ L.take size $ randomRs (0, 50000) g


-- | Bubble sort for an immutable vector.
bubbleSort :: V.Vector Int -> V.Vector Int
bubbleSort = V.modify $ \v ->
  M.forM_ (L.reverse [0 .. MV.length v - 1]) $ \i ->
    M.forM_ [0 .. i - 1] $ \j -> do
      jv  <- MV.read v j
      jv' <- MV.read v (j + 1)
      bool (return ()) (MV.swap v j (j+1)) (jv > jv')


main :: IO ()
main = do
  g <- getStdGen

  let
      vec    = mkRandomVector g 10
      sorted = bubbleSort vec

  print vec
  print sorted
