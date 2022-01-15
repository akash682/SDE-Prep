"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104

"""

def maxprofit(prices):
    """
    # Brute Force Approach O(n^2)
    maximum_revenue = -10^4
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            cur_revenue = prices[j] - prices[i]
            maximum_revenue = max(maximum_revenue, cur_revenue)
    return maximum_revenue
    """

    # Store the minimum value so far you calculate the revenue and compare with the maximum
    maximum_revenue = 0
    minimum_price = prices[0]
    for i in range(len(prices)):
        revenue = prices[i] - minimum_price
        maximum_revenue = max(maximum_revenue, revenue)
        minimum_price = min(minimum_price, prices[i])
    return maximum_revenue


