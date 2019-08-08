class Solution {
public:    
// Solution1 : DP + Sorting. 뒤쪽부터 각 원소에서 odd jump, even jump 시 end에 도달하는 지 여부를 저장.    
    struct Item {
        Item(int val, int idx) : val_(val), idx_(idx) {}
        int val_; // value of item in A
        int idx_; // index of item in A
    };

    int findNextIdx(bool odd_jump, vector<Item>& arr, int i, int N) {
        sort(arr.begin(), arr.end(), [odd_jump](const Item& l, const Item& r) {
            if(l.val_ < r.val_)
                return true;
            else if(l.val_ > r.val_)
                return false;
            else
                return odd_jump ? (l.idx_ < r.idx_) : (l.idx_ > r.idx_); //odd_jump면 같은 값에 대해 정순, even_jump면 같은 값에 대해 역순으로 sorting
        });
            
        //find location in array 
        auto iter = find_if(arr.begin(), arr.end(), [i](const Item& item) {
           return item.idx_ == i;
        });
        int arr_idx = distance(arr.begin(), iter);
        
        //find next idx
        if(odd_jump)
            return arr_idx != N-1-i ? arr[arr_idx+1].idx_ : -1;
        else
            return arr_idx != 0 ? arr[arr_idx-1].idx_ : -1;
    }
    
    int oddEvenJumps_2(vector<int>& A) {
        int N = A.size();
        vector<bool> odd(N, true);
        vector<bool> even(N, true);
        vector<Item> arr;
        arr.push_back(Item(A[N-1], N-1));
        
        for(int i = N-2; i >= 0; i--) {
            arr.push_back(Item(A[i], i));
            
            // Check if even/odd jumps are 'good'
            int even_j = findNextIdx(false, arr, i, N);
            if(even_j == -1) // Can't do even jump (to same or smaller)
                even[i] = false;
            else  // do even jump
                even[i] = odd[even_j];
            
            int odd_j = findNextIdx(true, arr, i, N);
            if(odd_j == -1) // Can't do odd jump (to same or bigger)
                odd[i] = false;
            else // do odd jump
                odd[i] = even[odd_j]; 
        }
        
        return accumulate(odd.begin(), odd.end(), 0);
    }
    
    
    
// Solution2 : DP + Map. 뒤쪽부터 각 원소에서 odd jump, even jump 시 end에 도달하는 지 여부를 저장.
    int oddEvenJumps(vector<int>& A) {
        int N = A.size();
        vector<bool> odd(N, false);
        vector<bool> even(N, false);    
        map<int, int> acc_map; //Key : value of item , Value : idx of item
        acc_map[A[N-1]] = N-1;

        odd.back() = true;
        even.back() = true;

        for(int i = N-2; i >= 0; i--) {
            auto iter_lo = acc_map.lower_bound(A[i]);
            auto iter_up = acc_map.upper_bound(A[i]);

            if (iter_lo != acc_map.end())
                odd[i] = even[iter_lo->second]; // do even jump

            if (iter_up != acc_map.begin())
                even[i] = odd[(--iter_up)->second]; // do odd jump

            acc_map[A[i]] = i;
        }

        return accumulate(odd.begin(), odd.end(), 0);
    }
//In the case that the map contains an element with a key equivalent to k: In this case, lower_bound returns an iterator pointing to that element, whereas upper_bound returns an iterator pointing to the next element.
//refer : http://www.cplusplus.com/reference/map/map/lower_bound/
    
};
