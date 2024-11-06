#include <iostream>
using namespace std;

int main() {
    int blocks, processes;

    // Input number of blocks and processes
    cout << "Enter the number of blocks: ";
    cin >> blocks;
    cout << "Enter the number of processes: ";
    cin >> processes;

    int blockSize[blocks], processSize[processes], allocation[processes], fragment[processes];

    // Input block sizes
    cout << "\nEnter the size of the blocks:\n";
    for (int i = 0; i < blocks; i++) {
        cout << "Block " << i + 1 << ": ";
        cin >> blockSize[i];
    }

    // Input process sizes
    cout << "\nEnter the size of the processes:\n";
    for (int i = 0; i < processes; i++) {
        cout << "Process " << i + 1 << ": ";
        cin >> processSize[i];
        allocation[i] = -1; // initially no block allocated
    }

    int lastAllocatedBlock = 0; // Start from the first block for next-fit

    // Memory allocation using Next-Fit
    for (int i = 0; i < processes; i++) {
        int allocated = 0;
        
        for (int j = 0; j < blocks; j++) {
            int currentBlock = (lastAllocatedBlock + j) % blocks; // Wrap around using modulo

            if (blockSize[currentBlock] >= processSize[i]) {
                allocation[i] = currentBlock;               // Allocate block to process
                fragment[i] = blockSize[currentBlock] - processSize[i]; // Calculate fragment
                blockSize[currentBlock] -= processSize[i];  // Reduce available block size
                lastAllocatedBlock = (currentBlock + 1) % blocks; // Update last allocated block
                allocated = 1;
                break;
            }
        }

        if (!allocated) {
            fragment[i] = -1; // Indicate no allocation was possible for this process
        }
    }

    // Display allocation and fragmentation details
    cout << "\nProcess_no\tProcess_size\tBlock_no\tBlock_size\tFragment\n";
    for (int i = 0; i < processes; i++) {
        cout << i + 1 << "\t\t" << processSize[i] << "\t\t";
        if (allocation[i] != -1) {
            cout << allocation[i] + 1 << "\t\t" << processSize[i] + fragment[i] << "\t\t" << fragment[i] << endl;
        } else {
            cout << "Not Allocated\t\t--\t\t--\n";
        }
    }

    return 0;
}