


ch = input("ENter a character:")

match ch:
  case 'a'|'i'|'e'|'o'|'u'|'A'|'I'|'o'|'E'|'U':print("Vowel")
  case _:print("Consonant")