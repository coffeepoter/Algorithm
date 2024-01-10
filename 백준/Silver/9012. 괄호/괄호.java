import java.io.*;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int k = 0; k < n; k++) {
            Stack<String> stack = new Stack<>();
            boolean vps;

            String[] str = br.readLine().split("");

            for (int i = 0; i < str.length; i++) {
                if (str[i].equals("(")) {
                    stack.push(str[i]);
                } else  {
                    if (stack.empty() || stack.peek().equals(")")) {
                        stack.push(str[i]);
                    } else {
                        stack.pop();
                    }
                }
            }

            if (stack.empty()) {
                vps = true;
            } else {
                vps = false;
            }
            if (vps) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
