/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
	bool judge(vector<Interval>& intervals, int i) {
		if(i == intervals.size() - 1) return 0;
		if(intervals[i].end >= intervals[i + 1].start) {
			intervals[i].end = intervals[i].end > intervals[i + 1].end ? intervals[i].end : intervals[i + 1].end;
			cout << intervals[i].start << " " << intervals[i].end << endl;
			intervals.erase(intervals.begin() + i + 1);
			return 1;
		}
		return 0;
	}

    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        if(intervals.empty()) {
            intervals.push_back(newInterval);
            return intervals;
        }
      	for(int i = 0; i < intervals.size(); ++i) {
      		if(intervals[i].end < newInterval.start) continue;
      		else if(intervals[i].start > newInterval.end) {
      			intervals.insert(intervals.begin() + i, newInterval);
      			return intervals;
      		}else {
      			intervals[i].start = intervals[i].start < newInterval.start ? intervals[i].start : newInterval.start;
      			intervals[i].end = intervals[i].end > newInterval.end ? intervals[i].end : newInterval.end;
      			cout << intervals[i].start << " " << intervals[i].end << endl;
      			while(judge(intervals, i));
                return intervals;
      		}
      	}
      	intervals.push_back(newInterval);
      	return intervals;  
    }
};

vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
	intervals.push_back(newInterval);
    sort(intervals.begin(), intervals.end(), [](Interval a, Interval b){
    	return a.start < b.start;
    })
    vector<Interval> res;
    res.push_back(intervals[0]);
    for(auto tem : intervals) {
    	int r = res.size() - 1;
    	if(tem.end <= res[r].end) continue;
    	if(tem.start > res[r].end) res.push_back(tem);
    	else if(tem.start <= res[r].end) res[r].end = tem.end;
    }
    return res;
}