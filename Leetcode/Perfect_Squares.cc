// Solution 1 : DP. 
// Time : O(N^2), Space : O(N)
// C++로는 80ms인데, 똑같은 솔루션으로 Python에서는 400ms가 넘어 Time Limit Exceeded 발생함.

class Solution {
public:
    int numSquares(int n) {
        static std::vector<int> min_nums = {0};
        while(min_nums.size() <= n) {
            int min_num = INT_MAX, i = min_nums.size();
            for(int j = 1; j*j <= i; j++)
                min_num = min(1 + min_nums[i-j*j], min_num);
            min_nums.push_back(min_num);
        }
        return min_nums[n];
    }
    
    int numSquares_1(int n) {
        std::vector<int> min_nums = {0};
        for(int i = 1; i < n+1; i++) {
            int min_num = INT_MAX;
            for(int j = 1; j*j <= i; j++)
                min_num = min(1 + min_nums[i-j*j], min_num);
            min_nums.push_back(min_num);
        }
        return min_nums[n];
    }
};
