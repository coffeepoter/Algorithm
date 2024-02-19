#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int M, N;
    cin >> M >> N;
    int root;

    for (int i = M; i <= N; i++)
    {
        bool isPrime = true;
        root = (int)sqrt(i);

        if (i == 1)
        {
            isPrime = false;
            continue;
        }

        for (int j = 2; j <= root; j++)
        {
            if (i % j == 0)
            {
                isPrime = false;
                break;
            }
        }

        if (isPrime)
            cout << i << "\n";
    }
    return 0;
}