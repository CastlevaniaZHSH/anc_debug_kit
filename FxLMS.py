"""
    Fxlms by 2h5h_CN
    March 29th
    
"""""

import numpy as np

"""

 input         {w[.....]}   output      
--------> [ unknown system]---------> 

input_signal      ->      x(n)  input to the system we estimate
output_signal     ->      d(n)  output of the system
order             ->      filter order for system
learning_rate     ->      learning rate for Fxlms
iter_max          ->      maximun number of iter times
error_min         ->      the target error  

"""

CONVEGETHRESHLOD = 10000

class FxLMS(object):

    def __init__(self, input_signal, output_signal, order=300,learning_rate=0.0001):
        self.input      =   input_signal
        self.output     =   output_signal
        self.miu        =   learning_rate
        self.filter     =   np.zeros(order)
        self.error      =   np.zeros(self.input.size)
        self.order      =   order

    def solve(self):

        filterInput     =   np.zeros(self.order);

        # considering the boundary
        for index in range (self.input.size):

            filterInput         = np.hstack((self.input[index],filterInput[0:self.order-1]))

            filterOutput        = np.dot(filterInput,self.filter.T)

            self.error[index]   = self.output[index] - filterOutput

            self.filter         = self.filter + self.miu  * self.error[index] * filterInput

            if (abs(self.error[index]) > CONVEGETHRESHLOD ):
                raise RuntimeError('Failed to converge make sure it a steady random signal')


    def getResults(self):

        return (self.filter, self.error)




if(__name__=='__main__'):
    print "This is a py file for FxLMS "
