int twice_as_old(int dad, int son) {
  int cal = dad - (son*2);
  if (cal < 0){
    cal = -cal;
  }

  return cal;
}