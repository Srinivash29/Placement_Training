import java.util.Scanner;
class Odd_Index {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter Array Size:");
        int n = scan.nextInt();
        int[] arr = new int[n];
        System.out.print("Enter Array Values:");
        for(int i=0;i<n;i++){
            arr[i] = scan.nextInt();
        }
        for(int i=0;i<n;i+=2){
            System.out.print(arr[i]+" ");
        }
        scan.close();

    }
}