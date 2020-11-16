Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 21:01:17) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
  def romanToInt(self, s):
    m = {'I' : 1, 'V': 5, 'X': 10, 'L' : 50,
         'C' : 100, 'D': 500, 'M': 1000}
    ans = m[s[0]]
    for c, p in zip(s[1:], s[0:-1]):
      ans += m[c]
      if m[c] > m[p]: ans -= 2 * m[p]
    return ans
