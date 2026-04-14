from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # map1: counts of characters in the current window of s
        # map2: required counts of characters from t
        map1, map2 = defaultdict(int), Counter(t)

        # mct: number of characters from t currently satisfied in the window
        # dmct: total number of characters we need to satisfy (length of t)
        mct, dmct = 0, len(t)

        # i and j are the right and left ends of the current window
        # Start with an empty window: i and j both -1
        i = j = -1

        # best answer so far
        ans = ""

        while True:
            flag1 = flag2 = False  # Track progress in this iteration

            # Acquire: Try to expand the window to satisfy all characters of t
            # Move 'i' to the right while we haven't satisfied t yet
            while i < len(s) - 1 and mct < dmct:
                i += 1
                char = s[i]

                # Include s[i] into the window
                map1[char] += 1

                # If including this char doesn't exceed the needed count for this char,
                # we have one more character from t satisfied
                if map1[char] <= map2[char]:
                    mct += 1

                flag1 = True  # We progressed by acquiring

            # Release: Try to shrink the window from the left while it's still valid
            while j < i and mct == dmct:
                # Current valid window is (j+1) to i, inclusive
                pans = s[j+1:i+1]

                # Update best answer if this window is smaller
                if ans == "" or len(ans) > len(pans):
                    ans = pans

                # Move left edge to the right to shrink
                j += 1
                char = s[j]

                # Remove s[j] from the window
                map1[char] -= 1

                # If removing this char causes the window to no longer satisfy
                # the required count for this char, we lose one matched character
                if map1[char] < map2[char]:
                    mct -= 1

                flag2 = True  # We progressed by releasing/shrinking

            # If no progress was made in both directions, we've explored all substrings
            if not (flag1 and flag2):
                break

        return ans