package persistent.bugger;

public class PersistentBugger {

   public int persistence(int num){
       int temp,x,count=0;
       while(num>=10){
           temp=n;
           count++;
           n=1;
           while(temp>0){
              x=temp%10;
              num=n*x;
              temp=temp/10;}
       
           }
    return count;
   }
    public static void main(String[] args) {
     PersistentBugger obj= new PersistentBugger();
     obj.persistence(39);
    }
    
}
