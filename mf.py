import numpy

"""
@INPUT :
    R  : a matrix to be factorized, dimension N X M
    P  : an intial matrix of dimension N X K
    Q  : an intial matrix of dimension M X K
    K  : the numbers of latent features
    steps : the maximum number of steps to perform the optimisation
    alpha : the learning rate
    beta  : the regularization parameter
@OUTPUT : the final matrices P and Q
"""
def matrix_factorization(R,P,Q,K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range (len(R[i])):
                if R[i][j] >0:
                    eij= R[i][j]- numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] = alpha*(2*eij*Q[k][j] - beta*P[i][j])
                        Q[k][j] = Q[k][j]+alpha*(2*eij*P[i][k] - beta*Q[k][j])
                        eR = numpy.dot(P,Q)
                        e = 0
                        for i in range(len(R)):
                            for j in range(len(R[i])):
                                if R[i][j]>0:
                                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]),2)
                                    for k in range(k):
                                        e = e + (beta/2) * (pow(P[i][k],2)+pow(Q[k][j],2))
                                        if e <0.001:
                                            break
                                        return P, Q.T

if __name__=="__main__":
    R= [
    [5,3,0,1],
    [4,0,0,1],
    [1,1,0,5],
    [1,0,0,4],
    [2,1,3,0],
                ],
    R = numpy.array(R)
    N= len(R)
    M= len(R[0])
    K=2

    P= numpy.random.rand(N,K)
    Q= numpy.random.rand(M,K)

print(P, Q)