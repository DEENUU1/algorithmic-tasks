using System;

public static class AgeDiff 
{
  public static string CalculateAge(int birth, int yearTo) 
  {
    int old = Math.Abs(yearTo - birth);
    if (birth > yearTo){
      if (old == 1)
        {
          return $"You will be born in 1 year.";
        }
      return $"You will be born in {old} years.";
    }
    if (birth == yearTo)
      {
      return "You were born this very year!";
      }
    if (birth < yearTo)
      {
      if (old == 1)
        {
          return "You are 1 year old.";    
        }
      return $"You are {old} years old.";
      }
    return "None";
  }
}