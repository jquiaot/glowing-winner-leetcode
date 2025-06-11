# @param {String} s
# @return {Integer}
def max_difference(s)
  frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  ord_a = 'a'.ord
  s.chars.each { |c| frequencies[c.ord - ord_a] += 1 }

  frequencies.sort!

  max_odd = s.length
  min_even = -1

  i = 0
  while i < frequencies.length
    if frequencies[i] > 0 && frequencies[i].modulo(2) == 0
      min_even = frequencies[i]
      break
    end
    i += 1
  end

  i = frequencies.length - 1
  while i >= 0
    if frequencies[i].modulo(2) == 1
      max_odd = frequencies[i]
      break
    end
    i -= 1
  end

  return max_odd - min_even
end
