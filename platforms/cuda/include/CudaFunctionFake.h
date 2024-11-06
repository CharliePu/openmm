#ifndef CUDA_FUNCTION_FAKE_H
#define CUDA_FUNCTION_FAKE_H

#include <cuda.h>
#include <vector>


// Fake CUFunction type mimicing CUfunc_st *
class CUfunctionFake {
public:
    CUfunctionFake() : func_ptr(nullptr), hasMultiple(false) {}
    CUfunctionFake(CUfunc_st* ptr) : func_ptr(ptr), hasMultiple(false) {}
    
    CUfunctionFake& operator=(CUfunc_st* ptr) {
        func_ptr = ptr;
        return *this;
    }

    operator CUfunction() {
        return reinterpret_cast<CUfunction>(func_ptr);
    }

    CUfunc_st &operator*() {
        return *func_ptr;
    }

    CUfunc_st** getPointerToPointer() {
        return &func_ptr;
    }

    void addFunction(CUfunc_st* ptr) {
        func_ptrs.push_back(ptr);
        hasMultiple = true;
    }

    bool hasMultipleFunctions() {
        return hasMultiple;
    }

    std::vector<CUfunc_st*> getFunctions() {
        return func_ptrs;
    }

private:
    CUfunc_st* func_ptr; 
    std::vector<CUfunc_st*> func_ptrs;
    bool hasMultiple;
};

#endif // CUDA_FUNCTION_FAKE_H