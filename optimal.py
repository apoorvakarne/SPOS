class OptimalPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of frames in memory
        self.memory = []  # Memory (list)
        self.page_faults = 0  # Counter for page faults

    def access_page(self, pages, current_index):
        """Access a page, either adding it to memory or causing a page fault."""
        page = pages[current_index]
        if page not in self.memory:
            # Page fault occurs
            if len(self.memory) < self.capacity:
                # If memory is not full, add the page
                self.memory.append(page)
                print(f"Page {page} caused a page fault. Memory: {list(self.memory)}")
            else:
                # Memory is full, find the optimal page to replace
                farthest_index = -1
                page_to_replace = None
                for mem_page in self.memory:
                    try:
                        next_index = pages.index(mem_page, current_index)
                    except ValueError:
                        next_index = float('inf')  # Page not found in future
                        
                    if next_index > farthest_index:
                        farthest_index = next_index
                        page_to_replace = mem_page
                
                # Replace the optimal page
                self.memory.remove(page_to_replace)
                self.memory.append(page)
                print(f"Page {page} caused a page fault. Replaced page {page_to_replace}. Memory: {list(self.memory)}")
                
            self.page_faults += 1
        else:
            print(f"Page {page} found in memory. Memory: {list(self.memory)}")

    def get_page_faults(self):
        """Returns the number of page faults."""
        return self.page_faults

def main():
    # Test the Optimal Page Replacement algorithm
    capacity = int(input("Enter the number of frames: "))
    pages = list(map(int, input("Enter the reference string (space-separated page numbers): ").split()))

    optimal = OptimalPageReplacement(capacity)
    
    for index in range(len(pages)):
        optimal.access_page(pages, index)
    
    print(f"\nTotal page faults: {optimal.get_page_faults()}")

if __name__ == "__main__":
    main()

