/*
Problema 1002 BeeCrowd
2026.11.03
Benicio Cordeiro
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;

    cin >> r;
    area = 3.14159 * r * r;
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}