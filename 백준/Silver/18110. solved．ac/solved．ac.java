import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {

    public Main() {
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] level = new int[n];
        int cutLine = (int) Math.round(n * 0.15);

        for(int i=0;i<n;i++){
            level[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(level);

        int ans = main.cal(cutLine, level, n);

        bw.write(String.valueOf(ans));

        br.close();
        bw.flush();
        bw.close();
    }

    public int cal(int cut, int[] arr, int n){
        double sum = 0;
        int avg;
        for(int i = cut; i<n-cut; i++){
            sum += arr[i];
        }
        double num = n - cut * 2;
        avg = (int)Math.round(sum / num);
        return avg;
    }
}

