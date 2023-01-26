# problem link
# https://leetcode.com/problems/stock-price-fluctuation/description/

class StockPrice:

    def __init__(self):
        self.timestamps = defaultdict(int)
        self.latest = 0
        self.mint = []
        self.maxt = []

    def update(self, timestamp: int, price: int) -> None:
        old = self.timestamps[timestamp]
        self.timestamps[timestamp] = price
        self.latest = max(self.latest,timestamp)
        heappush(self.mint, (price, timestamp))
        heappush(self.maxt, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.latest]
        

    def maximum(self) -> int:
        currPrice, timestamp = heappop(self.maxt)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while -currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.maxt)
            
        heappush(self.maxt, (currPrice, timestamp))
        return -currPrice

    def minimum(self) -> int:
        currPrice, timestamp = heappop(self.mint)
		
		#If the price from the heap doesn't match the price the timestamp indicates, keep popping from the heap
        while currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.mint)
            
        heappush(self.mint, (currPrice, timestamp))
        return currPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()