public class Kata {
    public static String highAndLow(String numbers) {
        String[] numArray = numbers.split(" ");

        int highest = Integer.MIN_VALUE;
        int lowest = Integer.MAX_VALUE;

        for (String numStr : numArray) {
            int num = Integer.parseInt(numStr);
            highest = Math.max(highest, num);
            lowest = Math.min(lowest, num);
        }

        return highest + " " + lowest;
    }
}
