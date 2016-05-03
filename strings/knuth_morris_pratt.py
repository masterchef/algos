class KmpSearch(object):
  def __init__(self, s, p):
    self.s = s
    self.p = p

  def find(self):
     self.pmt_table = self.buildPmt()
     print self.s, self.p
     print self.pmt_table
     return self.search()

  def search(self):
    p_ix = 0
    s_ix = 0
    while s_ix < len(self.s):
      print p_ix, s_ix, self.p[p_ix], self.s[s_ix], self.pmt_table[p_ix]
      while(p_ix > 0 and self.s[s_ix] != self.p[p_ix]):
        p_ix = self.pmt_table[p_ix]
        print p_ix, s_ix, self.p[p_ix], self.s[s_ix], self.pmt_table[p_ix]

      p_ix += 1
      s_ix += 1

      if p_ix == len(self.p):
        return s_ix - len(self.p)

    return -1

  # Builds partial match table
  def buildPmt(self):
    i = 1
    j = 0
    result = [0] * len(self.p)
    while i < len(self.p):
      if self.p[i] == self.p[j]:
        result[i] = j + 1
        j += 1
      elif j > 0:
        j = result[j-1]
        i -= 1
      i += 1
    return result

#print KmpSearch('abcabdababdabcabdabdabc', 'abcabdabc').find()
print KmpSearch('xababababc', 'ababc').find()

