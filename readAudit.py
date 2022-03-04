from sqloperations import *
from emailoperations import *

def audit():
  k=readAudit()
  sendLogEmail(k)
  print(k)
© 2022 GitHub, Inc.
Terms
Privacy
