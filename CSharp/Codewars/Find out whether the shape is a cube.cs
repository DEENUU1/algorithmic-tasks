namespace CubeCheck {
    using System;
    
    public class CubeChecker {
        public bool IsCube(double volume, double side) {
            if (volume <= 0 || side <= 0)
                return false;
            double calculatedVolume = Math.Pow(side, 3);
            return Math.Abs(calculatedVolume - volume) < 0.000001; 
        }
    }
}
