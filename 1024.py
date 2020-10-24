from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        start = end = 0
        clips.sort()
        print(clips)
        count = 0
        i = 0
        while end < T:
            if i >= len(clips) or clips[i][0] > end:
                return -1
            new_end = end
            while i < len(clips) and clips[i][0] <= end:
                new_end = max(new_end, clips[i][1])
                i += 1
            end = new_end
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    clips = [[0, 4], [2, 8]]
    print(s.videoStitching(clips, 5))
