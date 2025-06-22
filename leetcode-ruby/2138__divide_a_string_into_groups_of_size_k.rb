# @param {String} s
# @param {Integer} k
# @param {Character} fill
# @return {String[]}
def divide_string(s, k, fill)
  groups = []
  remaining = s.length
  i = 0
  while remaining > 0 do
    if remaining >= k
      groups << s[i, k]
    else
      groups << s[i, remaining] + fill * (k - remaining)
    end
    i += k
    remaining -= k
  end

  return groups
end
