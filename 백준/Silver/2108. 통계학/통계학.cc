#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

vector<int> arr;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, tmp;
    int count[8001] = {
        0,
    };
    int max = -9999;
    bool isFirst = true;

    int sum =0, avg, mid, fre, range;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        arr.push_back(tmp);
        sum += tmp;
        count[tmp + 4000]++;
    }

    sort(arr.begin(), arr.end());

    for (int i = 0; i < 8001; i++)
    {
        if (count[i] == 0)
            continue;
        if (count[i] == max && !isFirst)
        {
            fre = i - 4000;
            isFirst = true;
        }
        if (count[i] > max)
        {
            max = count[i];
            fre = i - 4000;
            isFirst = false;
        }
    }

    avg = round((float)sum / N);
    mid = arr[arr.size() / 2];
    range = arr.back() - arr.front();

    cout << avg << '\n'
         << mid << '\n'
         << fre << '\n'
         << range;
}