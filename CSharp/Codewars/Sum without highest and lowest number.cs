using System;
using System.Linq;

public static class Kata
{
    public static int Sum(int[] numbers)
    {
        if (numbers == null || numbers.Length <= 1)
        {
            return 0;
        }

        int minimum = numbers.Min();
        int maximum = numbers.Max();

        var numberList = numbers.ToList();
        numberList.Remove(minimum);
        numberList.Remove(maximum);

        return numberList.Sum();
    }
}