import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        double[] grade = new double[n];
        for (int i = 0; i < n; i++) {
            grade[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(grade);
        double max = grade[n - 1];
        double sum = 0;
        for (int i = 0; i < n; i++) {
            grade[i] = (grade[i]/max) * 100;
            sum += grade[i];
        }
        System.out.println(sum / n);
    }


}
