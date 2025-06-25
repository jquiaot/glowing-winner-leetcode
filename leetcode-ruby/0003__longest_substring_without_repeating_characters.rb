require 'set'

# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  max_len = 0
  chars = Set.new
  i = 0
  j = 0
  while j < s.length
    if chars.include?(s[j])
      max_len = [max_len, chars.length()].max
      while i < j
        if s[i] == s[j]
          i += 1
          break
        else
          chars.delete(s[i])
        end
        i += 1
      end
    else
      chars.add(s[j])
    end
    j += 1
  end
  return [max_len, chars.length()].max
end
