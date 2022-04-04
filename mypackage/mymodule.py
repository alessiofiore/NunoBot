'''
Created on 06 giu 2017

@author: ealesfi
'''

class MyClass:
    '''
    classdocs
    '''
    count = 0

    def __init__(self):
        '''
        Constructor
        '''
    
    def displayCount(self):
        print("Count " + str(self.count))

    def increaseCount(self):
        self.count = self.count + 1 