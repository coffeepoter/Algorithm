#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    int N;
    cin >> N;
    stack<int> s;
    vector<char> res;
    int cnt = 1;

    for (int i = 0; i < N; i++)
    {
        int x;
        cin >> x;

        while (cnt <= x)
        {
            s.push(cnt);
            cnt += 1;
            res.push_back('+');
        }

        if (s.top() == x)
        {
            s.pop();
            res.push_back('-');
        }
        else
        {
            cout << "NO";
            return 0;
        }
    }
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << "\n";
    }
}