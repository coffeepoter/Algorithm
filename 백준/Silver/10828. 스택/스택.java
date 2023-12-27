import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    int[] stack;
    int top = -1;

    public Main(int size) {
        stack = new int[size];
    }

    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Main main = new Main(n);

        for (int i = 0; i < n; i++) {
            String command = br.readLine();
            StringTokenizer st = new StringTokenizer(command);
            int result;

            switch (st.nextToken()) {
                case "push":
                    int x = Integer.parseInt(st.nextToken());
                    main.push(x);
                    break;
                case "pop":
                    result = main.pop();
                    bw.write(result + "\n");
                    break;
                case "size":
                    result = main.size();
                    bw.write(result + "\n");
                    break;
                case "empty":
                    boolean empty = main.empty();
                    bw.write(empty ? 1 + "\n" : 0 + "\n");
                    break;
                case "top":
                    result = main.top();
                    bw.write(result + "\n");
                    break;
            }
        }

        br.close();
        bw.flush();
        bw.close();
    }

    public void push(int x) {
        stack[++top] = x;
    }

    public int pop() {
        if (empty()) {
            return -1;
        }
        return stack[top--];
    }

    public int size() {
        return top + 1;
    }

    public boolean empty() {
        return top == -1;
    }

    public int top() {
        if (empty()) {
            return -1;
        }
        return stack[top];
    }
}
