using System;

public class GrassHopper 
    {
        public static int FindAverage(int[] nums)
        {
          int sum = 0;
          foreach(int num in nums)
            {
              sum += num;
            }
          
          return sum / nums.Length;
        }
    }