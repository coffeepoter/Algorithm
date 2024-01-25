import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int[] tri = new int[3];
            tri[0] = Integer.parseInt(st.nextToken());
            tri[1] = Integer.parseInt(st.nextToken());
            tri[2] = Integer.parseInt(st.nextToken());

            Arrays.sort(tri);

            if (tri[0] == tri[1] && tri[1] == tri[2] && tri[2] == 0) {
                break;
            }
            if (tri[2] * tri[2] == tri[0] * tri[0] + tri[1] * tri[1]) {
                sb.append("right\n");
            } else {
                sb.append("wrong\n");
            }
        }

        System.out.println(sb);

    }
}