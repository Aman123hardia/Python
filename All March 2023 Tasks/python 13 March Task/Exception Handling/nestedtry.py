# try:
#   try:
#     print("Inner try block")
#     print(10/0)
#   except :
#     print("Inner except block")
#   finally:
#    print("Inner finally block")
# except:
#  print("outer except block")
# finally:
#  print("outer finally block")


#if inner except block does not catch error then outer except block except exce

try:
  try:
    print("Inner try block")
    print(10/0)
  except FloatingPointError:
    print("Inner except block")
  else:
      print("Exception catched")    # else block excute when there is no exception in try block
  finally:
   print("Inner finally block")
except:
 print("outer except block")
finally:
 print("outer finally block")