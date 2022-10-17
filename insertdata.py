import sys
from main import insertdata



print(sys.argv[1],sys.argv[2])
if sys.argv[1] is None and sys.argv[2] is None:
    print("send two arguments")

else:
  insertdata(sys.argv[1],sys.argv[2])
  print("added")