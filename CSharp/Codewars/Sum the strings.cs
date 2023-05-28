using System;
namespace Solution
{
  public static class Program
  {
    public static string StringsSum(string s1, string s2)
    {
      int s1_int = string.IsNullOrEmpty(s1) ? 0 : int.Parse(s1);
      int s2_int = string.IsNullOrEmpty(s2) ? 0 : int.Parse(s2);
      int sum = s1_int + s2_int;
      return sum.ToString();
    }
  }
}