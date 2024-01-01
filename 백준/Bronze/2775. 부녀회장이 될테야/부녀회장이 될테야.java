import java.io.*;

public class Main {

    public Main() {
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int test = Integer.parseInt(br.readLine());

        //k층 n호에는 몇 명이 살고 있는지 출력
        for(int i=0;i<test;i++){
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());

            int result = main.numPeople(k,n);
            System.out.println(result);
        }
        
        br.close();
    }

    public int numPeople(int k, int n){
        int[][] people = new int[k+1][n+1];
        //0층 1호부터 필요한 번호까지 값 지정
        for(int i=1;i<=n;i++){
            people[0][i] = i;
        }

        //필요한 층까지 계산
        for(int stage=1;stage<=k;stage++){
            for(int num=1;num<=n;num++){
                for(int i=0;i<num;i++){
                    people[stage][num] += people[stage-1][num-i];
                }
            }
        }

        return people[k][n];
    }
}

