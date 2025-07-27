import heapq

class FlashSaleTracker:
    def __init__(self):
        self.request_counts = {}
        self.stock_levels = {}

    def add_stock(self, item_id, quantity):
        """Add or update stock for an item."""
        self.stock_levels[item_id] = self.stock_levels.get(item_id, 0) + quantity

    def request_item(self, item_id):
        """Record a request for an item."""
        self.request_counts[item_id] = self.request_counts.get(item_id, 0) + 1

    def update_stock(self, item_id, quantity):
        """Decrease stock when an item is sold."""
        if item_id in self.stock_levels:
            self.stock_levels[item_id] = max(0, self.stock_levels[item_id] - quantity)

    def top_k_popular_in_stock(self, k):
        """Return K most requested items that are still in stock."""
        min_heap = []  

        for item_id, count in self.request_counts.items():
            if self.stock_levels.get(item_id, 0) > 0: 
                heapq.heappush(min_heap, (count, item_id))
                if len(min_heap) > k:
                    heapq.heappop(min_heap)  

        top_items = sorted(min_heap, key=lambda x: (-x[0], x[1]))
        return [item_id for count, item_id in top_items]

tracker = FlashSaleTracker()
tracker.add_stock("item1", 10)
tracker.add_stock("item2", 5)
tracker.add_stock("item3", 0)  

tracker.request_item("item1")
tracker.request_item("item1")
tracker.request_item("item2")
tracker.request_item("item3")  

print(tracker.top_k_popular_in_stock(2))  