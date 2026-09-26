

n = None

match n:
  case None:print("None matched")
  case {"name":"cheeku","age":21}:print("Dictonary matched...")
  case ():print("Empty tuple matched")
  case (1,2): print("tuple matched")
  case []:print("Empty list")
  case [1,2,3]:print("List matched")
  case 20+5j:print("complex matched")
  case "Indore": print("String matched")
  case True: print("Boolean matched")
  case 1:print("Integer matched")
  case 1.5:print("FLoat matched")
  case _: print("Not matched")     