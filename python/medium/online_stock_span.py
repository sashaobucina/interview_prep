class StockSpanner:
    """
    # 901: Write a class StockSpanner which collects daily price quotes for some stock, and returns 
    the span of that stock's price for the current day.

    The span of the stock's price today is defined as the maximum number of consecutive days 
    (starting from today and going backwards) for which the price of the stock was less than or equal 
    to today's price.

    For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], 
    then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
    """

    def __init__(self):
        # keeps track of how many days has gone by
        self.days = 0

        # monotonically decreasing stack to get previous greater element
        self.in_stk = []

    def next(self, price: int) -> int:
        # go through all days where stock was smaller than current price
        while self.in_stk and price >= self.in_stk[-1][0]:
            self.in_stk.pop()

        # get distance from previous greater element (PGE)
        PGE = (self.in_stk[-1][1] + 1) if self.in_stk else 0

        # do updates, push to stack
        self.in_stk.append((price, self.days))
        self.days += 1

        # return days since last day stock was at a greater price
        return self.days - PGE

if __name__ == "__main__":
    spanner = StockSpanner()
    assert spanner.next(100) == 1
    assert spanner.next(80) == 1
    assert spanner.next(60) == 1
    assert spanner.next(70) == 2
    assert spanner.next(60) == 1
    assert spanner.next(75) == 4
    assert spanner.next(85) == 6
    assert spanner.next(100) == 8

    print("Passed all tests!")