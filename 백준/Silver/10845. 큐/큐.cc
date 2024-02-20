#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    queue<string> q;
    for (int i = 0; i < N; i++)
    {
        string str;
        getline(cin >> ws, str);

        size_t pos = str.find(' ');
        string cmd = str.substr(0, pos);
        string data = str.substr(pos + 1);

        if (cmd == "push")
            q.push(data);
        else if (cmd == "pop")
        {
            if (q.empty())
                cout << "-1\n";
            else
            {
                cout << q.front() << "\n";
                q.pop();
            }
        }
        else if (cmd == "size")
            cout << q.size() << "\n";
        else if (cmd == "empty")
        {
            if (q.empty())
                cout << "1\n";
            else
                cout << "0\n";
        }
        else if (cmd == "front")
        {
            if (q.empty())
                cout << "-1\n";
            else
                cout << q.front() << "\n";
        }
        else if (cmd == "back")
        {
            if (q.empty())
                cout << "-1\n";
            else
                cout << q.back() << "\n";
        }
    }
}