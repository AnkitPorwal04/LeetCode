1496. Path Crossing

Easy Topics Companies

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:

<img width="366" alt="screen-shot-2020-06-10-at-123929-pm" src="https://github.com/AnkitPorwal04/LeetCode/assets/96345105/3e5a267a-98ee-4f63-bbe9-6ceeba0fdeee">

Input: path = "NES"

Output: false 

Explanation: Notice that the path doesn't cross any point more than once.

Example 2:

<img width="425" alt="screen-shot-2020-06-10-at-123843-pm" src="https://github.com/AnkitPorwal04/LeetCode/assets/96345105/4b778a88-dfc8-4911-8cb4-1360acca90d7">

Input: path = "NESWW"

Output: true

Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104

path[i] is either 'N', 'S', 'E', or 'W'.
