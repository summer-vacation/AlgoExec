# -*- coding: utf-8 -*-
"""

   File Name：     all_any
   Author :       jing
   Date：          2020/3/27
"""

# any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
# all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False

# any 一真则真，全假才假
# all 一假则假，全真才真

print("1----", any([0, '', 'false']))
print("2----", any([0, '', bool('false')]))
print("3----", any([0, '', False]))      # 全都是 空、0、false
print("4----", any(('a', 'b', '')))

print("5----", all(['a', 'b', 'c', 'd']))
print("6----", all(('a', 'b', '', 'd')))    # 元组tuple，存在一个为空的元素)


