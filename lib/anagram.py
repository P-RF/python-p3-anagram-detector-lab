# your code goes here!
class Anagram:

  def __init__(self, word):
    self.word = word.lower()
    self.sorted_word = sorted(self.word)

  def match(self, word_list):
    return [
      new_word for new_word in word_list
      if sorted(new_word.lower()) == self.sorted_word and new_word.lower() != self.word
    ]


