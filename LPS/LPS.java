public class LPS {
    public static void main(String[] args) {
        runLPS("character");
    }

    public static void runLPS(String str) {
        System.out.println(str);
        System.out.println(LPS(str));
    }

    public static String LPS(String str) {
        int n = str.length();
        Integer [][] size = new Integer [n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if (i == j) {
                    size[i][j] = 1;
                }
                else {
                    size[i][j] = 0;
                }
            }
        }

        for(int k = 2; k <= n; k++) {
            for(int i = 0; i < n-k+1; i++) {
                int j = i + k - 1;

                if(str.charAt(i) == str.charAt(j)) {
                    if (k == 2){
                        size[i][j] = 2;
                    }
                    else {
                        size[i][j] = 2 + size[i+1][j-1];
                    }
                }
                else {
                    size[i][j] = Math.max(size[i+1][j], size[i][j-1]);
                }
            }
        }

        int answerLength = size[0][n-1];
        char [] result = new char[answerLength];
        int rIndex = n-1;
        int i = 0;
        char cur = str.charAt(rIndex);
        while(rIndex > 0 && size[0][rIndex] != 1) {
            if (size[0][rIndex] != size[0][rIndex-1]) {
                result[i] = cur;
                result[answerLength - i - 1] = cur;
                i++;
            }
            rIndex--;
            cur = str.charAt(rIndex);
        }
        result[i] = cur;

        return new String(result);
    }

    public static <E> void multiToString(E[][] inputArray) {
        for(E[] i : inputArray) {
            for(E j : i) {
                System.out.print(j + " ");
            }
            System.out.println("");
        }
    }
}
