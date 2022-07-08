# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from heap_priority_queue import HeapPriorityQueue
# I changed a lot on this page, so I'll just highlight on the handout the lines that I changed instead of marking them all here

freq = {}
last_word = ''
sentence_start = True
excluded = ('i', 'me', 'my', 'mine', 'myself', 'you', 'you', 'your', 
            'yours', 'yourself', 'he', 'him', 'his', 'his', 'himself', 
            'she', 'her', 'her', 'hers', 'herself', 'it', 'it', 'its', 
            'itself', 'we', 'us', 'our', 'ours', 'ourselves', 'you', 
            'you', 'your', 'yours', 'yourselves', 'they', 'them', 'their', 
            'theirs', 'themselves', 'the', 'an', 'a', 'thou', 'thee', 'thine', 'thy', 'thineself')
for piece in open("KJV.txt").read().lower().split():
  # only consider alphabetic characters within this piece
  word = ''.join(c for c in piece if c.isalpha())
  if not (word == '' or word in excluded):
    if not sentence_start:
      word_pair = last_word + ' ' + word
      freq[word_pair] = 1 + freq.get(word_pair, 0)
    last_word = word
  sentence_start = (piece[-1] in '.!?;')

word_pairs = HeapPriorityQueue()
max_words = []
max_counts = []
for (w,c) in freq.items():    # (key, value) tuples represent (word, count)
  word_pairs.max_add(w,c)
for i in range(min(10, len(word_pairs))):
  word_pair = (word_pairs.remove_max())
  max_words.append(word_pair[0])
  max_counts.append(word_pair[1])
print("freq words")
for i in range(min(10, len(word_pairs))):
  print(max_counts[i], max_words[i])