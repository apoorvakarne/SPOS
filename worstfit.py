#include <iostream>
using namespace std;

int main() {
    int blocks, files;

    // Input number of blocks and files
    cout << "Enter the number of blocks: ";
    cin >> blocks;
    cout << "Enter the number of files: ";
    cin >> files;

    int blockSize[blocks], originalBlockSize[blocks], fileSize[files], allocation[files], fragment[files];

    // Input block sizes and store original sizes
    cout << "\nEnter the size of the blocks:\n";
    for (int i = 0; i < blocks; i++) {
        cout << "Block " << i + 1 << ": ";
        cin >> blockSize[i];
        originalBlockSize[i] = blockSize[i];  // Save original block sizes for display purposes
    }

    // Input file sizes
    cout << "\nEnter the size of the files:\n";
    for (int i = 0; i < files; i++) {
        cout << "File " << i + 1 << ": ";
        cin >> fileSize[i];
        allocation[i] = -1; // initially no block allocated
        fragment[i] = 0;    // initially no fragment
    }

    // Memory allocation using Worst-Fit
    for (int i = 0; i < files; i++) {
        int worstIdx = -1;

        // Find the largest block that can accommodate the current file
        for (int j = 0; j < blocks; j++) {
            // Block must be available and large enough to fit the file
            if (blockSize[j] >= fileSize[i]) {
                if (worstIdx == -1 || blockSize[j] > blockSize[worstIdx]) {
                    worstIdx = j;
                }
            }
        }

        // If a suitable block is found, allocate it to the file
        if (worstIdx != -1) {
            allocation[i] = worstIdx + 1;                  // Store 1-based index of block
            fragment[i] = blockSize[worstIdx] - fileSize[i]; // Calculate fragment
            blockSize[worstIdx] = 0;            // Mark this block as used by setting its size to 0
        } else {
            // If no suitable block found, mark as not allocated
            allocation[i] = 0;
            fragment[i] = 0;
        }
    }

    // Display allocation and fragmentation details
    cout << "\nFile_no\tFile_size\tBlock_no\tBlock_size\tFragment\n";
    for (int i = 0; i < files; i++) {
        cout << i + 1 << "\t" << fileSize[i] << "\t\t";
        if (allocation[i] != 0) {
            int blockIndex = allocation[i] - 1; // Convert to 0-based index for block size display
            cout << allocation[i] << "\t\t" << originalBlockSize[blockIndex] << "\t\t" << fragment[i] << endl;
        } else {
            cout << "0\t\t0\t\t0\n";
        }
    }

    return 0;
}