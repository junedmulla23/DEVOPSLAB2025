public class LinearSearch {
    public static void main(String[] args) {
        int[] arr = {4, 2, 7, 1, 9};
        int key = 7;
        boolean found = false;
        for (int num : arr) {
            if (num == key) {
                found = true;
                break;
            }
        }
        if (found)
            System.out.println(key + " is found in the array.");
        else
            System.out.println(key + " is not found in the array.");
    }
}
