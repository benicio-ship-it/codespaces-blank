/*
Problema 1174 BeeCrowd
2026.11.05
Benício Cordeiro
*/
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
    vector<double> a;
    double x;
    int i, qtd;

    for (i = 0; i < 100; i++) {
        cin >> x;
        a.push_back(x);
    }

    qtd = a.size();
    cout << fixed << setprecision(1);
    for (i = 0; i < qtd; i++) {
        if (a[i] <= 10) {
            cout << "A[" << i << "] = " << a[i] << endl;
        }
    }

    return 0;
}