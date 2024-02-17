public class Positive{

  public static int sum(int[] arr){
    int total = 0;
    for (int num: arr) {
      if (num > 0){
        total += num;
      }
      
    }
    
    return total;
    
  }

}
