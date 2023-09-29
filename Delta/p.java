import java.util.ArrayList;
import java.util.List;

public class DictionarySearch {

    public static List<String> findSimilarWords(String w, String[] d) {
        List<String> s = new ArrayList<>();

        for (String word : d) {
            if (isOneEditAway(w, word)) {
                s.add(word);
            }
        }

        return s;
    }

    public static boolean isOneEditAway(String w1, String w2) {
        if (Math.abs(w1.length() - w2.length()) > 1) {
            return false;
        }

        int d = 0;
        int i = 0, j = 0;

        while (i < w1.length() && j < w2.length()) {
            if (w1.charAt(i) != w2.charAt(j)) {
                d++;
                if (d > 1) {
                    return false;
                }

                if (w1.length() < w2.length()) {
                    j++;
                } else if (w1.length() > w2.length()) {
                    i++;
                } else {
                    i++;
                    j++;
                }
            } else {
                i++;
                j++;
            }
        }

        return d == 1 || (i == w1.length() && j == w2.length() && d == 0);
    }

    public static void main(String[] args) {
        String[] dictionary = {"cat", "bat", "rat", "hat", "cot", "cut", "cup", "cart"};
        String searchWord = "cat";

        List<String> similarWords = findSimilarWords(searchWord, dictionary);

        System.out.println("Similar words to \"" + searchWord + "\": " + similarWords);
    }
}
