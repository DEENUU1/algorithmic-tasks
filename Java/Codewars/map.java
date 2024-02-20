import java.util.List;
import java.util.ArrayList;

public class Maps {
  public static int[] map(int[] arr) {
    List<Integer> nums = new ArrayList<>();
    
    for (int num : arr){
      nums.add(num*2);
    }
    
    int[] result = new int[nums.size()];
    for (int i = 0; i < nums.size(); i++) {
      result[i] = nums.get(i);
    }
    
    return result;
  }
}
