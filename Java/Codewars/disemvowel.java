public class Troll {
    public static String disemvowel(String str) {
        char[] vowels = {'a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O'};
        String newStr = "";
        for (char s : str.toCharArray()) {
            boolean isVowel = false;
            for (char vowel : vowels) {
                if (s == vowel) {
                    isVowel = true;
                    break;
                }
            }
            if (!isVowel) {
                newStr = newStr.concat(String.valueOf(s));
            }
        }
        return newStr;
    }
}
