/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */

bool judge(vector<Interval>& intervals, vector<Interval>::iterator i) {
	bool res = false;
	for(vector<Interval>::iterator j = i + 1; j != intervals.end(); ) {
		//if(i == j) continue;
		if(i->start <= j->end && i->start >= j->start) {
			i->start = j->start;
			i->end = i->end > j->end ? i->end : j->end;
			j = intervals.erase(j);
			res = true;
		}else if(j->start <= i->end && j->start >= i->start) {
			//i->start = j->start;
			i->end = i->end > j->end ? i->end : j->end;
			j = intervals.erase(j);
			res = true;
		}else {
			++j;
		}
	}
	return res;
}

class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
  		vector<Interval> res;
  		//for(int i = 0; i < intervals.size(); ++i) {
  		for(auto i = intervals.begin(); i != intervals.end(); ++i) {
  			while(judge(intervals, i));
  		}	
      	return intervals;
    }
};