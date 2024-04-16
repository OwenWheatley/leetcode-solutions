/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const set1 = new Set(nums);
    if (set1.size !== nums.length) {
        return true;
    } else {
        return false;
    }
};