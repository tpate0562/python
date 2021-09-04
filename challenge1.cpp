#include <iostream>
using namespace std;
int var1;
int main() {
  cout << "enter a number:";
  cin >> var1;
  if (var1 == 1) cout << "1\n";
  if (var1 > 100) cout << "why is this number so high?\n";
  for (int i = 1; i <= var1; i++) {
    for (int k = var1 - i; k > 0; k--) {
      cout << " ";
    }
    for (int j = 1; j <= i; j++) {
      cout << "* ";
    }
    cout << endl;
  }
}
