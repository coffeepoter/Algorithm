import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        ArrayList<Pair> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            int order = i;
            list.add(new Pair(age, order, name));
        }

        list.sort(new Comparator<Pair>() {
            @Override
            public int compare(Pair x, Pair y) {
                return x.age - y.age;
            }
        });
        for (int i = 0; i < n; i++) {
            System.out.println(list.get(i).age + " " + list.get(i).name);
        }

    }
}

class Pair {
    int age, order;
    String name;

    public Pair(int age, int order, String name) {
        this.age = age;
        this.order = order;
        this.name = name;
    }
}