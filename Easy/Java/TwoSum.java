class Solution {

    public int[] twoSum(int[] nums, int target) {
        int rounds = nums.length;

        for (int i = 0; i < rounds; i = i + 1) {
            for (int j = i + 1; j < rounds; j = j + 1) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        

        // Placeholder return, replace with actual logic
        return new int[]{};
    }

    // public static void main(String[] args) {
    //     Solution solution = new Solution(); // Create an instance of Solution

    //     // Example usage
    //     int[] result = solution.twoSum(new int[]{2, 7, 11, 15}, 13);
    //     // Output the result

    //     for (int num : result) {
    //         System.out.println(num);
    //     }
    // }
}
