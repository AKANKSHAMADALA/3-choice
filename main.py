print ( "1-rectangle" ) 
figure = input ( "Select a shape:" )

if figure == '1' : 
    print ( "The lengths of the sides of the rectangle:" ) 
    a = float (input ( "a =" )) 
    b = float (input ( "b =" )) 
    print ( "Area:% .2f" % (a * b)) 
print("2-triangle")
print ( "The lengths of the sides of the triangle:" ) 
figure==input("select a shape")


if figure == '2':
    a = float (input ( "a =" )) 
    b = float (input ( "b =" )) 
    c = float (input ( "c =")) 
    p = (a + b + c) / 2 
    from math import sqrt 
    s = sqrt (p * (p - a) * (p - b) * (p - c))
    print ( "Area:% .2f" % s) 
print("3-square")
print("the length of the sides of the square")
figure==("select the shape")

if figure=='3':
  a = float ( input ( "a=" ) )
  b = float ( input ( "b=" ) )
  c = float ( input ( "c=" ) )
  d = float ( input ( "d=" ) )
  from math import sqrt
  Area = s*s
  print("Area of the square="+str(Area))