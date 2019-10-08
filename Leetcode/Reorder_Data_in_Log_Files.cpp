// Problem : letter log를 digit log 보다 앞에오게하고, letter log들은 뒷부분 문자열로 정렬하고, 문자가 똑같으면 id로 정렬.
// Time : O(NlogN), Space : O(N)

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        stable_sort(logs.begin(), logs.end(), [](string l, string r) {
            int i = l.find(" ");
            int j = r.find(" ");
            if (!isdigit(l[i+1]) && !isdigit(r[j+1])) {
                string l_sub = l.substr(i+1);
                string r_sub = r.substr(j+1);
                return (l_sub != r_sub) ? (l_sub < r_sub) : (l.substr(0, i) < r.substr(0, j));
            }
            else {
                if(isdigit(l[i+1]))
                    return false;
                return true;
            }
        });
        return logs;
    }
};
