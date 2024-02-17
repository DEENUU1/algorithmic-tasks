public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        
        String res = "";
        
        for (int i = 0; i < repeat; i++){
          res = res.concat(string);
        }
      
        return res;
      
    }
}
