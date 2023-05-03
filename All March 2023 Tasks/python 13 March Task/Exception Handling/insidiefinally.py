try:
 print("try")
except:
  print("except")
finally:
 try:
  print("inner try")
 except:
  print("inner except block")
 finally:
  print("inner finally block")