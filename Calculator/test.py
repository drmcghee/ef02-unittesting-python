from grappa import should
True | should.be.true
False | should.be.false
None | should.be.none


Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 



'Hello grappa' | should.contain('grappa') | should.contain('he')