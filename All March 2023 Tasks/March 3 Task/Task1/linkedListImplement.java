
    import java.util.*;  
    public class Main{  
     public static void main(String args[]){  
      
      LinkedList li=new LinkedList();  
    
      li.add("Amit");  
      li.add("Shubham");  
      li.add(22);  
   
        
      LinkedList li1=new LinkedList();  
      li1.add("Nikhil");  
      li1.add("Shubham");  
     
      
      li.remove("Amit");  // remove element in LinkedList 
      li.remove((Integer.valueOf(22))); //remove Integer in LinkedList
      
      li.addFirst("Nitesh");  //insert element at first position in LinkedList
      li.addLast(44);     //insert element at last position in LinkedList
      
      li.addAll(1,li1);          //add Collection in 1st LinkedList
      Iterator itr=li.iterator();  

      while(itr.hasNext()){  
      System.out.println(itr.next());  
      }  
         
      li.clear();   // Remove all data from LinkedList l1
    
     for( ;itr.hasNext();){
        System.out.print(itr.next());  // itr used in for loop 
      }
      
     
     }  
    }  
    
