import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int test = Integer.parseInt(br.readLine());

        for(int i=0;i<test;i++){
            String[] info = br.readLine().split(" ");
            int height = Integer.parseInt(info[0]);
            int num = Integer.parseInt(info[2]);

            if (num % height == 0) {
                bw.write((height * 100) + num/height + "\n");

            } else {
                bw.write(((num % height) * 100) + (num/height + 1) + "\n");
            }
        }
        br.close();
        bw.flush();
        bw.close();
    }
}

