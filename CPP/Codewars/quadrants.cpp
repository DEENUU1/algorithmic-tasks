int quadrant(int x, int y) {
  if (x > 0) {
    if (y > 0) {
      return 1;
    }
    else {
      return 4;
    }
  }

  else {
    if (y > 0) {
      return 2;
    }
    else {
      return 3;
    }
  }
}