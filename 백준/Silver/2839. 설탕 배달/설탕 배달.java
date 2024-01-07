import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int min = 987654321;
        int x = (n / 5) + 1;
        int y = (n / 3) + 1;
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (n == (i * 5) + (j * 3) && min > (i + j)) {
                    min = i + j;
                }
            }
        }
        if(min == 987654321){
            min = -1;
        }
        System.out.println(min);

        br.close();
    }
}

