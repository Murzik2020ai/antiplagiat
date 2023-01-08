import re

TOKEN_RE = re.compile(r'[\w\d]+')

def tokenize_text_simple_regex(txt):
  '''
  tokenizer
  args txt : str
  return str
  '''
  txt = txt.lower()
  all_tokens = TOKEN_RE.findall(txt)
  return all_tokens
