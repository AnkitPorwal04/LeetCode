1437. Check If All 1's Are at Least Length K Places Away

Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

Example 1:

<img width="428" height="181" alt="sample_1_1791" src="https://github.com/user-attachments/assets/089f563e-81c2-45d2-ac1e-94723a726510" />

- Input: nums = [1,0,0,0,1,0,0,1], k = 2
- Output: true
- Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:

<img width="320" height="173" alt="sample_2_1791" src="https://github.com/user-attachments/assets/3b09c181-8727-4609-b72d-c6730f4acb52" />

- Input: nums = [1,0,0,1,0,1], k = 2
- Output: false
- Explanation: The second 1 and third 1 are only one apart from each other.
 

Constraints:

- 1 <= nums.length <= 105
- 0 <= k <= nums.length
- nums[i] is 0 or 1
