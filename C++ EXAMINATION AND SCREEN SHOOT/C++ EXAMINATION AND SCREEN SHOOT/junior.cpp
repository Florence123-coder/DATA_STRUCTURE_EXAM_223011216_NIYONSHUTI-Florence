#NAME; NIYONSHUTI Florence
#reg no; 223011216
#EXAMINATION OF OBJECT ORIENTED OF C++
#Q82,Matrix Operation Library
#include <iostream>
#include <iomanip>
#include <stdexcept>
#include <cmath>

using namespace std;

// Function to allocate memory for int matrix
int** allocateMatrix(int r, int c) {
    int** mat = new int*[r];
    for (int i = 0; i < r; ++i)
        mat[i] = new int[c];
    return mat;
}

// Function to deallocate int matrix
void freeMatrix(int** mat, int r) {
    for (int i = 0; i < r; ++i)
        delete[] mat[i];
    delete[] mat;
}

// Print matrix
void printMatrix(int** mat, int r, int c) {
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j)
            cout << setw(6) << *(*(mat + i) + j);
        cout << endl;
    }
}

// Base class
class MatrixOp {
public:
    virtual int** apply(int** A, int** B, int r1, int c1, int r2, int c2, int& rr, int& rc) = 0;
    virtual ~MatrixOp() {}
};

// Derived class for addition
class AddMatrixOp : public MatrixOp {
public:
    int** apply(int** A, int** B, int r1, int c1, int r2, int c2, int& rr, int& rc) override {
        if (r1 != r2 || c1 != c2) {
            throw invalid_argument("Addition requires same dimensions.");
        }
        rr = r1; rc = c1;
        int** result = allocateMatrix(rr, rc);
        for (int i = 0; i < rr; i++)
            for (int j = 0; j < rc; j++)
                *(*(result + i) + j) = *(*(A + i) + j) + *(*(B + i) + j);
        return result;
    }
};

// Derived class for multiplication
class MulMatrixOp : public MatrixOp {
public:
    int** apply(int** A, int** B, int r1, int c1, int r2, int c2, int& rr, int& rc) override {
        if (c1 != r2) {
            throw invalid_argument("Multiplication requires A columns = B rows.");
        }
        rr = r1; rc = c2;
        int** result = allocateMatrix(rr, rc);
        for (int i = 0; i < rr; i++)
            for (int j = 0; j < rc; j++) {
                *(*(result + i) + j) = 0;
                for (int k = 0; k < c1; k++)
                    *(*(result + i) + j) += *(*(A + i) + k) * *(*(B + k) + j);
            }
        return result;
    }
};

// Derived class for inversion using Gaussian elimination
class InverseMatrixOp : public MatrixOp {
public:
    int** apply(int** A, int**, int r1, int c1, int, int, int& rr, int& rc) override {
        if (r1 != c1)
            throw invalid_argument("Inversion requires square matrix.");

        int n = r1;
        rr = rc = n;

        double** mat = new double*[n];
        double** inv = new double*[n];
        for (int i = 0; i < n; ++i) {
            mat[i] = new double[n];
            inv[i] = new double[n];
            for (int j = 0; j < n; ++j) {
                mat[i][j] = A[i][j];
                inv[i][j] = (i == j) ? 1 : 0;
            }
        }

        for (int i = 0; i < n; ++i) {
            double pivot = mat[i][i];
            if (fabs(pivot) < 1e-9)
                throw runtime_error("Matrix is singular or non-invertible.");

            for (int j = 0; j < n; ++j) {
                mat[i][j] /= pivot;
                inv[i][j] /= pivot;
            }

            for (int k = 0; k < n; ++k) {
                if (k == i) continue;
                double factor = mat[k][i];
                for (int j = 0; j < n; ++j) {
                    mat[k][j] -= factor * mat[i][j];
                    inv[k][j] -= factor * inv[i][j];
                }
            }
        }

        // Convert result to int matrix (rounded)
        int** result = allocateMatrix(n, n);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                result[i][j] = round(inv[i][j]);

        for (int i = 0; i < n; ++i) {
            delete[] mat[i];
            delete[] inv[i];
        }
        delete[] mat;
        delete[] inv;

        return result;
    }
};

// Read a matrix from user input
int** inputMatrix(int& rows, int& cols, const string& name) {
    cout << "Enter number of rows for " << name << ": ";
    cin >> rows;
    cout << "Enter number of columns for " << name << ": ";
    cin >> cols;
    int** mat = allocateMatrix(rows, cols);
    cout << "Enter elements of " << name << ":\n";
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j) {
            cout << name << "[" << i << "][" << j << "] = ";
            cin >> mat[i][j];
        }
    return mat;
}

// Main function
int main() {
    int r1, c1, r2, c2;

    // Input two matrices
    int** A = inputMatrix(r1, c1, "A");
    int** B = inputMatrix(r2, c2, "B");

    // Create operation objects
    MatrixOp* ops[3];
    ops[0] = new AddMatrixOp();
    ops[1] = new MulMatrixOp();
    ops[2] = new InverseMatrixOp();

    int choice;
    int** result = nullptr;
    int rr = 0, rc = 0;

    do {
        cout << "\nMenu:\n";
        cout << "1. Add A + B\n";
        cout << "2. Multiply A * B\n";
        cout << "3. Invert Matrix A\n";
        cout << "4. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        try {
            switch (choice) {
                case 1:
                    result = ops[0]->apply(A, B, r1, c1, r2, c2, rr, rc);
                    cout << "Result of A + B:\n";
                    printMatrix(result, rr, rc);
                    freeMatrix(result, rr);
                    break;
                case 2:
                    result = ops[1]->apply(A, B, r1, c1, r2, c2, rr, rc);
                    cout << "Result of A * B:\n";
                    printMatrix(result, rr, rc);
                    freeMatrix(result, rr);
                    break;
                case 3:
                    result = ops[2]->apply(A, nullptr, r1, c1, 0, 0, rr, rc);
                    cout << "Inverse of A (rounded to int):\n";
                    printMatrix(result, rr, rc);
                    freeMatrix(result, rr);
                    break;
                case 4:
                    cout << "Exiting...\n";
                    break;
                default:
                    cout << "Invalid choice.\n";
            }
        } catch (exception& e) {
            cout << "Error: " << e.what() << endl;
        }
    } while (choice != 4);

    // Free memory
    freeMatrix(A, r1);
    freeMatrix(B, r2);
    for (int i = 0; i < 3; ++i)
        delete ops[i];

    return 0;
}
