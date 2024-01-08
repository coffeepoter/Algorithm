import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<String> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(br.readLine());
        }

        List<String> newList = list.stream().distinct().collect(Collectors.toList());
        newList.sort(Comparator.naturalOrder());
        newList.sort(new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return a.length() - b.length();
            }
        });

        for(int i=0;i< newList.size();i++){
            System.out.println(newList.get(i));
        }
    }
}

