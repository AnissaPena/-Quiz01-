# matrixVec takes a matrix and a vector and multiplies them.  
def matVec(matrix, vector):
    '''
This function takes a matrix and a vector as it's arguments. It then updates each element of the vector by multiplying it by the matrix before returning the now updated vector. 
    '''
def matvec(matrix, vector):
    
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result = matrix[i][j] * vector[j]
        result.append(total)
        
    return result
   
#Below are test variables being used to compute the function matVec
 
 def matvec(matrix, vector):
     matrix = A
     vector = x
 # 2x2 matrices   
     

testmatrix01 = [2,3],[1,4]
testmatrix02 = [1,3],[5,0]
testmatrix03 = 'this is a test'

testVector01 = [1, 2]
testVector02 = [2,4]
testVector03 = True

# These are test cases for the function matVec. All but one of the tests should be commented out at a time so that we can see how each pair of inputs effects the output. 

print(matVec(testmatrix01,testVector01))
#print(matVec(testmatrix02,testVector02))
#print(matVec(testmatrix03,testVector03))


