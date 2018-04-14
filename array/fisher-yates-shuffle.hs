import           Control.Monad.Primitive (PrimMonad, PrimState)
import qualified Data.Vector.Unboxed as V
import qualified Data.Vector.Unboxed.Mutable as M
import           System.Random (StdGen, randomR, getStdGen)

----------------------------------------------------------------------

shuffleM :: (M.Unbox a, PrimMonad m) =>
            StdGen -> Int -> M.MVector (PrimState m) a -> m ()
shuffleM _ n _ | n <= 1 = return ()
shuffleM g n v = do
  let
      n'       = n - 1
      (i, g')  = randomR (0, n') g
  M.swap v n' i
  shuffleM g' n' v

shuffle :: M.Unbox a => StdGen -> V.Vector a -> V.Vector a
shuffle g v =
  V.modify (shuffleM g $ V.length v) v

----------------------------------------------------------------------  

mkVector :: V.Vector Int
mkVector = V.enumFromN 1 20

main :: IO ()
main = getStdGen >>= print . flip shuffle mkVector
