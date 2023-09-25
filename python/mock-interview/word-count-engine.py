# Word Count Engine

def sanitize(word):
  res = ''
  for char in word:
    if char.isalpha(): res = res + char.lower()
  return res

def word_count_engine(document):
  words = document.split(' ');
  frequency = {}
  
  for i, word in enumerate(words):
    valid_word = sanitize(word)
    if valid_word:
      if valid_word not in frequency:
        # (freq, pos)
        frequency[valid_word] = [0, i]
      frequency[valid_word][0] += 1
      
  words = []
  # frequency = { word: (freq, pos) }
  for word, freq_pos in frequency.items():
    words.append([word, freq_pos])
    
  def sort_by_freq(item):
    return (item[1][0], -1 * item[1][1])
  
  # words = [ ['word', (freq, pos)] ]
  words.sort(key=sort_by_freq, reverse=True)
  
  # words are sorted
  res = []
  for word, freq_pos in words:
    res.append([word, str(freq_pos[0])])
  
  return res
