public static class Kata
{
 public static string Usdcny(int usd)
   {
      float res = (float)(usd * 6.75);
      return $"{res:F2} Chinese Yuan";
   }
}