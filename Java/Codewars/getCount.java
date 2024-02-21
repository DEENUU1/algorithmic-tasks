public class Vowels {

  public static int getCount(String str) {
    char[] vowels = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;
    for (char c : str.toCharArray()){
      for (char vowel : vowels) {
        if (c == vowel){
          count++;
          break;
        }
      }
    }
    return count;
  }

}
