class Kata {
  public static String getMiddle(String word) {
    String result = "";
    
    if(word.length() % 2 == 0) {
      int idx = word.length() / 2 - 1;
      result = word.substring(idx, idx + 2);
      
    } else {
      int idx = (word.length() - 1) / 2;
      result = word.valueOf(word.charAt(idx));
    }
    
    return result;
    
  }
}
