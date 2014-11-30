import java.util.Set;
import java.util.HashSet;

class ActivitySelection {
    public static void main(String [] args) {
        Set <Activity> s = new HashSet<Activity>();
        s.add(new Activity(1,2));
        s.add(new Activity(2,3));
        s.add(new Activity(1,5));
        ActivitySelection(s);
    }

    public static void ActivitySelection(Set <Activity> s) {
        for(Activity a : s) {
            System.out.println(s);
        }
    }
}
