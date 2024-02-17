public class Counter {
  public int countSheeps(Boolean[] arrayOfSheeps) {
    int count = 0;
    
    for (boolean sheep: arrayOfSheeps){
      if (sheep){
        count++;
      }
    }
    
    return count;
  }
}
