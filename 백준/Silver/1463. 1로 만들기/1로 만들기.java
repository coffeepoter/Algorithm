import java.io.*;

public class Main {

    public Main() {
    }

    public static void main(String[] args) throws IOException{
        Main main = new Main();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        System.out.println(main.cal(n,0));
    }

    public int cal(int n, int count) {
        if (n < 2) {
            return count;
        }
        return Math.min(cal(n / 2, count + 1 + (n % 2)), cal(n / 3, count + 1 + (n % 3)));
    }
}
