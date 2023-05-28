public class Kata
{
  public static string Contamination(string text, string character)
  {
      string new_str = "";
      for(int i = 0; i < text.Length; i++)
        {
          new_str += character;
        }
    
      return new_str;
  }
}