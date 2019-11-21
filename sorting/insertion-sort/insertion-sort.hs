import Control.Monad as Mon
import Control.Monad.State as S
import Data.Bool (bool)
import Data.List as L
import Data.Vector.Unboxed as V
import Data.Vector.Unboxed.Mutable as M
import Debug.Trace (trace)
import System.Random (StdGen, randomR, getStdGen)


-- | Generates immutable vector of random integers
-- using state monad.
mkRndVector :: StdGen -> Int -> V.Vector Int
mkRndVector g size =
  let
      mkInt :: S.State StdGen Int
      mkInt = state $ randomR (0, 50000)

      mkLst = S.replicateM size mkInt

  in V.fromList $ evalState mkLst g


-- | Insertion sort for immutable vector.
insSort :: V.Vector Int -> V.Vector Int
insSort = V.modify $ \v ->
  Mon.forM_ [0 .. M.length v - 1] $ \i ->
    Mon.forM_ (L.reverse [0 .. i-1]) $ \j -> do
      iv <- M.read v (j + 1)
      jv <- M.read v j
      bool (return ()) (M.swap v (j+1) j) (iv < jv)


main :: IO ()
main = do
  g <- getStdGen

  let
      vec    = mkRndVector g 10
      sorted = insSort vec

  print vec
  print sorted
