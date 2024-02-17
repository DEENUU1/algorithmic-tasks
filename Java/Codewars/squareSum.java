public class Kata
 {
  public static int squareSum(int[] n)
  { 
    int total = 0;
    
    for (int num: n){
      total += num*num;
      
    }
    
    return total;
  }
 }
