
import java.util.*;

public class Solution {
    public int solution(String s, String t) {
        int result = -1;
        Deque<Character> target = new ArrayDeque<>();
        Deque<Character> seq = new ArrayDeque<>();
        Deque<Character> stackLeft = new ArrayDeque<>();
        Deque<Character> stackRight = new ArrayDeque<>();
        
        for (int i=0;i<s.length();i++) {
            seq.add(s.charAt(i));
        }
        for (int i=0;i<t.length();i++) {
            target.add(t.charAt(i));
        }
        while (true) {
            if (left(s,t,seq,target,stackLeft)) {
                for (int i=0;i<target.size()-1;i++) {
                    if (!stackLeft.isEmpty()) {
                        seq.addFirst(stackLeft.pollLast());
                    }
                    if (!stackRight.isEmpty()) {
                        seq.add(stackRight.pollFirst());
                    }
                }
                if (right(s,t,seq,target,stackRight)) {
                    for (int i=0;i<target.size()-1;i++) {
                        if (!stackRight.isEmpty()) {
                            seq.add(stackRight.pollFirst());
                        }
                        if (!stackLeft.isEmpty()) {
                            seq.addFirst(stackLeft.pollLast());
                        }
                    }
                    continue;
                } else break;
                
            } else break;
        }
        
        System.out.println(stackLeft);
        System.out.println(stackRight);
        return result;
    }
    
    public boolean left(String s,String t,Deque<Character> seq,Deque<Character> target, Deque<Character> stackLeft) {
        while (!seq.isEmpty()) {
            int cnt = 0;
            for (int k=0;k<target.size();k++) {
                if (seq.size() > cnt && s.charAt(cnt) == t.charAt(k)) {
                    cnt++;
                } else break;
            }
            if (cnt == target.size()) {
                for (int i=0;i<target.size();i++) {
                    seq.pollFirst();
                }
                return true;
            } else stackLeft.add(seq.pollFirst());
        }
        return false;
    }
    public boolean right(String s,String t,Deque<Character> seq,Deque<Character> target, Deque<Character> stackRight) {
        while (!seq.isEmpty()) {
            int cnt = -1;
            for (int k=target.size()-1;k>-1;k--) {
                if (seq.size() >= Math.abs(cnt) && s.charAt(cnt) == t.charAt(k)) {
                    cnt--;
                } else break;
            }
            if (cnt == -target.size()-1) {
                for (int i=0;i<target.size();i++) {
                    seq.pollLast();
                }
                return true;
            } else stackRight.addFirst(seq.pollLast());
        }
        return false;
    }
}