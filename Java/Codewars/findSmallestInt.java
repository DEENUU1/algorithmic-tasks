public class SmallestIntegerFinder {
    public static int findSmallestInt(int[] args) {
      int smallest = args[0];
      
      for (int num: args){
        if (smallest > num){
          smallest = num;
        }
      }
      
      return smallest;
    }
}
