function removeDuplicates(nums) {
    if (nums.length === 0) return 0; // Fix: Handle empty array case

    let k = 1;                      // Fix: Start from 1, since first element is always unique

    for (let i = 1; i < nums.length; i++) {   // Fix: Correct loop condition
        if (nums[i] !== nums[i - 1]) {      // Fix: Proper condition to check unique elements
            nums[k] = nums[i];  // Move unique element forward
            k++;
        }
    }

    return k;   // Return number of unique elements
}

// Example usage:
let nums = [1, 1, 2, 2, 3, 4, 4, 5];
let k = removeDuplicates(nums);

console.log(nums.slice(0, k)); // Output: [1, 2, 3, 4, 5]
console.log(k); // Output: 5
