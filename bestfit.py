#include <iostream>
using namespace std;

int main() {
    int blocks, files;

    // Input number of blocks and files
    cout << "Enter the number of blocks: ";
    cin >> blocks;
    cout << "Enter the number of files: ";
    cin >> files;

    int blockSize[blocks], fileSize[files], allocation[files], fragment[files];

    // Input block sizes
    cout << "\nEnter the size of the blocks:\n";
    for (int i = 0; i < blocks; i++) {
        cout << "Block " << i + 1 << ": ";
        cin >> blockSize[i];
    }

    // Input file sizes
    cout << "\nEnter the size of the files:\n";
    for (int i = 0; i < files; i++) {
        cout << "File " << i + 1 << ": ";
        cin >> fileSize[i];
        allocation[i] = -1; // initially no block allocated
    }

    // Memory allocation using best-fit
    for (int i = 0; i < files; i++) {
        int bestIdx = -1;
        for (int j = 0; j < blocks; j++) {
            if (blockSize[j] >= fileSize[i]) {
                if (bestIdx == -1 || blockSize[j] < blockSize[bestIdx]) {
                    bestIdx = j;
                }
            }
        }
        if (bestIdx != -1) {
            allocation[i] = bestIdx;                 // allocate best block to file
            fragment[i] = blockSize[bestIdx] - fileSize[i]; // calculate fragment
            blockSize[bestIdx] -= fileSize[i];       // reduce available block size
        }
    }

    // Display allocation and fragmentation details
    cout << "\nFile_no\tFile_size\tBlock_no\tBlock_size\tFragment\n";
    for (int i = 0; i < files; i++) {
        cout << i + 1 << "\t" << fileSize[i] << "\t\t";
        if (allocation[i] != -1) {
            cout << allocation[i] + 1 << "\t\t" << fileSize[i] + fragment[i] << "\t\t" << fragment[i] << endl;
        } else {
            cout << "Not Allocated\t\t--\t\t--\n";
        }
    }

    return 0;
}