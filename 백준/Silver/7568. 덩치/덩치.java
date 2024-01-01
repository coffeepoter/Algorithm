import java.io.*;

public class Main {

    public Main() {
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] height = new int[n];
        int[] weight = new int[n];
        int[][] level = new int[n][n];

        //초기화
        for(int i=0;i<n;i++){
            String[] str = br.readLine().split(" ");
            height[i] = Integer.parseInt(str[0]);
            weight[i] = Integer.parseInt(str[1]);
            level[i][i] = 1;
        }

        //계산
        main.rateLevel(n, height, weight, level);

        for(int i=0;i<n;i++){
            bw.write(level[i][i] + " ");
        }

        br.close();
        bw.flush();
        bw.close();
    }

    public void rateLevel(int n, int[] height, int[] weight, int[][] level){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(height[i] < height[j] && weight[i] < weight[j]){
                    level[i][i] += 1;
                }
            }
        }

    }

}

