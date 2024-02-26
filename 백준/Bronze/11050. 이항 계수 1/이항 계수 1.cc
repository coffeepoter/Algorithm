#include <iostream>

using namespace std;

int factorial(int n)
{
    int k = 1;

    for (int i = n; i > 0; i--)
    {   
        k *= i;
    }

    return k;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K;
    int ans;
    cin >> N >> K;

    ans = factorial(N)/ (factorial(N-K) * factorial(K));

    cout << ans;
}