class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        } else {
            String number = String.valueOf(x);
            String rev = "";
            char ch;

            for (int i = 0; i < number.length(); i = i + 1)
            {
              ch = number.charAt(i); //extracts each character
              rev = ch + rev; //adds each character in front of the existing string
            }

            return number.equalsIgnoreCase(rev);
        }
    }
}