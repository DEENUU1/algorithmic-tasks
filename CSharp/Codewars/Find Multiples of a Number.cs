using System.Collections.Generic;

public class Kata
{
  public static List<int> FindMultiples(int integer, int limit)
  {
    List <int> result = new List<int>();
    for(int i = integer; i <= limit; i+= integer)
      {
        result.Add(i);
      }
    return result;
  }
}