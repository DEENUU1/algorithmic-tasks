#include<string>

int points(const std::array<std::string, 10>& games) {

  int sum = 0;

  for (int i = 0; i < 10; i++) {
    std::string el = games[i];

    int num1 = std::stoi(el.substr(0, 1));
    int num2 = std::stoi(el.substr(2, 1));

    if (num1 > num2) {
      sum += 3;
    }
    else if (num1 < num2) {
      sum += 0;
    }
    else {
      sum += 1;
    }

  }
  return sum;
}