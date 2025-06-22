# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  result = []
  i = 0
  carry = false
  a = l1
  b = l2
  while a != nil or b != nil do
    s = 0
    if a != nil
      s += a.val
      a = a.next
    end
    if b != nil
      s += b.val
      b = b.next
    end
    if carry
      s += 1
    end
    if s >= 10
      s -= 10
      carry = true
    else
      carry = false
    end
    result << s
  end
  # don't forget the last carry
  if carry
    result << 1
  end
  return result
end
