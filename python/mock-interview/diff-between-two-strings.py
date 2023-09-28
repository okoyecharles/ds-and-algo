# Difference between two strings

def diffBetweenTwoStrings(source, target):
  def split_prepend (str, pre):
    chars = [c for c in str]
    chars = list(map(lambda char: pre + char, chars))
    return chars

  def diff(i, j, res, ops):
    if i == len(source) and j == len(target): return (res, ops)
    elif i >= len(source): return (res + split_prepend(target[j:], "+"), ops + (len(target) - j))
    elif j >= len(target): return (res + split_prepend(source[i:], "-"), ops + (len(source) - i))

    if source[i] == target[j]:
      return diff(i + 1, j + 1, res + [source[i]], ops)
    else:
      add = diff(i, j + 1, res + ['+' + target[j]], ops + 1)
      delete = diff(i + 1, j, res + ['-' + source[i]], ops + 1)
      return add if add[1] < delete[1] else delete
      
  chars, operations = diff(0, 0, [], 0)
  return chars
    
diffBetweenTwoStrings("ABCDEFG", "ABDFFGH")
# source = "ABCDEFG"
# target = "ABDFFGH"
# we might return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"