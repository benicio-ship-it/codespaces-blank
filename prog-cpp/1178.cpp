/*
Problema (1178) BeeCrowd
2026.11.05
Benício Cordeiro
*/
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

void preencher(vector<double> &n, double x) {
    n.push_back(x);
    for (int i = 1; i < 100; i++) {
        n.push_back(n[i - 1] / 2.0);
    }
}

void mostrar(const vector<double> &n) {
    cout << fixed << setprecision(4);
    for (int i = 0; i < 100; i++) {
        cout << "N[" << i << "] = " << n[i] << endl;
    }
}

int main() {
    vector<double> n;
    double x;

    cin >> x;
    preencher(n, x);
    mostrar(n);

    return 0;
}