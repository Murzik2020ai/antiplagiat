# Python keywords
lst_keywords = ['False', 'None', 'True', 
'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']

def take_keywords(txt):
  '''
  function to take from code Python keywords
  arg - txt : str
  return str
  '''
  txt = str(txt)
  txt = txt.split(" ")
  result = []
  for e in txt:
    if e in lst_keywords:
      result.append(e)
  return " ".join(result)

