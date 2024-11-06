#include <iostream>
using namespace std;

int main() {
    int blocks, files;
    int blockSize[20], fileSize[20], blockAllocated[20] = {0}, fragment[20];

    cout << "Enter the number of blocks: ";
    cin >> blocks;
    cout << "Enter the number of files: ";
    cin >> files;

    cout << "\nEnter the size of the blocks:\n";
    for (int i = 0; i < blocks; i++) {
        cout << "Block " << i + 1 << ": ";
        cin >> blockSize[i];
    }

    cout << "\nEnter the size of the files:\n";
    for (int i = 0; i < files; i++) {
        cout << "File " << i + 1 << ": ";
        cin >> fileSize[i];
    }

    // First-Fit Allocation
    for (int i = 0; i < files; i++) {
        for (int j = 0; j < blocks; j++) {
            if (blockAllocated[j] == 0 && blockSize[j] >= fileSize[i]) {  // Check if block is free and fits the file
                blockAllocated[j] = i + 1;  // Mark block as allocated to the file (using file index)
                fragment[i] = blockSize[j] - fileSize[i];  // Calculate fragmentation
                break;
            }
        }
    }

    // Display Output
    cout << "\nFile_no\tFile_size\tBlock_no\tBlock_size\tFragment\n";
    for (int i = 0; i < files; i++) {
        int allocatedBlock = -1;
        for (int j = 0; j < blocks; j++) {
            if (blockAllocated[j] == i + 1) {  // Check which block is allocated to this file
                allocatedBlock = j + 1;
                break;
            }
        }

        if (allocatedBlock != -1) {
            cout << i + 1 << "\t" << fileSize[i] << "\t\t" << allocatedBlock
                 << "\t\t" << blockSize[allocatedBlock - 1] << "\t\t" << fragment[i] << endl;
        } else {
            cout << i + 1 << "\t" << fileSize[i] << "\t\tNot Allocated\n";
        }
    }

    return 0;
}