import java.io.*;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        BigInteger factorial = BigInteger.ONE;

        for (int i = 1; i <= n; i++) {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }

        BigInteger div = BigInteger.TEN;
        int count = 0;

        while (factorial.compareTo(BigInteger.ZERO) > 0 && factorial.mod(div).equals(BigInteger.ZERO)){
            count++;
            div = div.multiply(BigInteger.TEN);
        }

        System.out.println(count);
        br.close();
    }
}
