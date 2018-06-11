# matrixVec takes a matrix and a vector and multiplies them.  
def matVec(matrix, vector):
    '''
This function takes a matrix and a vector as it's arguments. It then updates each element of the vector by multiplying it by the matrix before returning the now updated vector. 
    '''
    result = []
    for i in range(len(matrix)):
      total=0
      for j in range(len(vector)):
        total += matrix[i][j] * vector[j]
      result.append(total)
    return result

# in the above code I am designating total as 0 so that when the computation of matrix and vector it will be added to the result that the matrix and vector multiplication creates. 
   
#Below are test variables being used to compute the function matVec
 
# 2x2 matrices   
     
testmatrix01 = [[2,1],[1,4]]
testvector02 = [[1,3],[5,0]]
testmatrix03 = 'this is a test'

testVector01 = [1, 1]
testmatrix02 = [2,4]
testVector03 = True

# These are test cases for the function matVec. All but one of the tests should be commented out at a time so that we can see how each pair of inputs effects the output. 

print(matVec(testmatrix01,testVector01))
#print(matVec(testmatrix02,testVector02))
#print(matVec(testmartrix03,testVector02))
