problem 1)

input : 10 + 20 - 30 - 40 % 80 * 50 / 60 // 5
  
Output : -6.0
  
evualuation order : % * / // + -
 
------------------------------------------------------------------------
problem 2)

input :  10 + 20 + +30 - -40 + 10
    
Output: 110
  
evualuation order : unaryPlus , UnaryMinus , addition
  -----------------------------------------------------------------------
  
problem 3)

input :  10 + +20 + ~1+ -2 + (10+10)
  
output: 46
  
order of evualuation : () , ~ , unaryMinus , 10 +20
  
-------------------------------------------------------------------------
problem 4)

input : 8>>2 + 10 + 5 ** 2
  
output : 0
  
order of evualuation : ** , + , >>
  
-------------------------------------------------------------------------

problem 5)

input : 1<<1 + 2 & 3 + ~1 + +10
  
output : 8
  
order of evualuation :  unary operators , addition , shift operators, bitwise &
  
--------------------------------------------------------------------------------
problem 6)

input :  1 | 2 | 3 |4 | 5 >>1 ^ 2 * 2
  
output : 7
  
order of evualuation : * ,  >> , ^ , bitwise or 
  
-------------------------------------------------------------------------------
problem 7)

input :   10 == 30 >> 1 + 2 // 2
  
output : false
  
order of evualuation : // , + , >> , ==
  
-------------------------------------------------------------------------------
problem 8)

input :  2  is 2 | 2 is not 2.1
  
output : True
  
order of evualuation : logial  or  , identity operator
  
--------------------------------------------------------------------------------------------

problem 9)

input :   1+3*4 - 1 and 2 not in [1,2,3] or 3 in [1,2,3]
  
output :   True
  
order of evualuation : * , + , - , not in , in , and , or
 

-------------------------------------------------------------------------------------------

problem 10)

input :    1 & 1 and 1 or 1 | 1 ^ 2
  
output :   1
  
order of evualuation : bitwiseAND , bitwise Xor , bitwise OR , logical and logical or.
  
  
--------------------------------------------------------------------------------------------------
 



    
