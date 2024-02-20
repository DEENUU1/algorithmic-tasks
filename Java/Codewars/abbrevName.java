public class AbbreviateTwoWords {

  public static String abbrevName(String name) {
    
    String[] nameSplit = name.split(" ");
    char firstName = nameSplit[0].charAt(0);
    char lastName = nameSplit[1].charAt(0);
    return Character.toUpperCase(firstName) + "." + Character.toUpperCase(lastName);
    
  }
}
