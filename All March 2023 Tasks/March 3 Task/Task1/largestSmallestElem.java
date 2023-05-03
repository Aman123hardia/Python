//Write a program that finds the largest and smallest numbers in an array of integers
public class Main
{
  public static void main(String args[]){
        int arr[]={3,2,5,6,8,3,0};
        int max=arr[0];
        int min=arr[0];
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(min>arr[j])
                min=arr[j];
                if(max<arr[j])
                max=arr[j];
                                       
            }
        }
        System.out.print(min+" "+max);
    }

}
          