import numpy

def possibilities(board):
    return numpy.where(board == 0)
    
possibilities(board)