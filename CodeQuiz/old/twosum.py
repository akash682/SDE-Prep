"""
        Step1: Check the constraints
        Are all the numbers positive or can there be negatives?
        Are there duplicate numbers in the array? --> No duplicate
        Will there always be a solution available? --> No
        What do we return if there's no solution --> None
        Can there be multiple pairs that add up to the target?  --> No
        
        Step2: Write out some test cases
        T1: nums = [1,3,7,9,2] , target = 11  [3,4]
        T2: nums = [1,3,7,9,2] , target = 25  null
        T3: nums = [] ,target=1  null
        T4: nums = [5], target=5 null
        T5: nums = [1,6], target=7 [0,1]
        
        Step3: Figure out a solution without code
        Solution1: Brute Force approach O(n^2), two pointer technique
        Step4: Code 
        Step5: Double check for errors
        Step6: Test with the testcases
        Step7: Space&Time Complexity
        
        Polynomial
            O(logN) - Logarithmic
            O(n) - Linear
            O(nlogn) - Linearithmic
            O(n^2) - Quadratic
            O(N^3) - Cubic
        Exponential
            O(2^n) - Exponential
            O(n!) - Factorial
            O(n^n) - Exponential

"""