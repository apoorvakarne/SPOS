from collections import deque

class FIFOPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of frames in memory
        self.memory = deque(maxlen=capacity)  # Memory (FIFO queue)
        self.page_faults = 0  # Counter for page faults

    def access_page(self, page):
        """Access a page, either adding it to memory or causing a page fault."""
        if page not in self.memory:
            # Page fault occurs, so we add the page to memory
            if len(self.memory) == self.capacity:
                # If memory is full, the oldest page is removed (FIFO)
                self.memory.popleft()
            self.memory.append(page)
            self.page_faults += 1  # Increment page fault count
            print(f"Page {page} caused a page fault. Memory: {list(self.memory)}")
        else:
            print(f"Page {page} found in memory. Memory: {list(self.memory)}")

    def get_page_faults(self):
        """Returns the number of page faults."""
        return self.page_faults

def main():
    # Test the FIFO Page Replacement algorithm
    capacity = int(input("Enter the number of frames: "))
    pages = list(map(int, input("Enter the reference string (space-separated page numbers): ").split()))

    fifo = FIFOPageReplacement(capacity)
    
    for page in pages:
        fifo.access_page(page)
    
    print(f"\nTotal page faults: {fifo.get_page_faults()}")

if __name__ == "__main__":
    main()

