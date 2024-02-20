#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    deque<string> q;
    for (int i = 0; i < N; i++)
    {
        string str;
        getline(cin >> ws, str);

        size_t pos = str.find(' ');
        string cmd = str.substr(0, pos);
        string data = str.substr(pos + 1);

        if(cmd == "push_front")
            q.push_front(data);
        else if(cmd == "push_back")
            q.push_back(data);
        else if(cmd == "pop_front"){
            if(q.empty())
                cout << "-1\n";
            else{
                cout << q.front() <<"\n";
                q.pop_front();
            }   
        }
        else if(cmd == "pop_back"){
            if(q.empty())
                cout << "-1\n";
            else{
                cout << q.back() <<"\n";
                q.pop_back();
            }   
        }
        else if(cmd == "size")
            cout << q.size() << "\n";
        else if(cmd == "empty")
        {
            if(q.empty())
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