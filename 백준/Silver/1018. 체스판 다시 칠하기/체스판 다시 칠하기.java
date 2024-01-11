import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Main {

    public boolean[][] arr;
    public int min;

    public Main(boolean[][] arr, int min) {
        this.arr = arr;
        this.min = min;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Main main = new Main(new boolean[N][M], 64);

        for (int i = 0; i < N; i++) {
            String str = br.readLine();

            for (int j = 0; j < M; j++) {
                if (str.charAt(j) == 'W') {
                    main.arr[i][j] = true;		// W일 때는 true
                } else {
                    main.arr[i][j] = false;		// B일 때는 false
                }

            }
        }


        int N_row = N - 7;
        int M_col = M - 7;

        for (int i = 0; i < N_row; i++) {
            for (int j = 0; j < M_col; j++) {
                main.cal(i, j,main);
            }
        }
        System.out.println(main.min);
    }


    public void cal(int x, int y, Main main) {
        int end_x = x + 8;
        int end_y = y + 8;
        int count = 0;

        boolean TF = main.arr[x][y];

        for (int i = x; i < end_x; i++) {
            for (int j = y; j < end_y; j++) {
                if (main.arr[i][j] != TF) {
                    count++;
                }
                TF = (!TF);
            }
            TF = !TF;
        }
        count = Math.min(count, 64 - count);

        main.min = Math.min(main.min, count);
    }
}