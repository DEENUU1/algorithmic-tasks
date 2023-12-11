#include <vector>

std::vector<int> humanYearsCatYearsDogYears(int humanYears) {
  std::vector<int> res;

  int cat = 15;
  int dog = 15;

  if (humanYears >= 2) {
    cat += 9;
    dog += 9;
  }

  if (humanYears > 2) {
    cat += (humanYears - 2) * 4;
    dog += (humanYears - 2) * 5;
  }

  res.push_back(humanYears);
  res.push_back(cat);
  res.push_back(dog);

  return res;
}