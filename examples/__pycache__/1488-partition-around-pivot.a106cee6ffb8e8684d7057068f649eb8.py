
# apl-source:1
# مثال 1488 — التقسيم حول محور
# apl-source:2
# Partition around a pivot
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1488-partition-around-pivot.apl
# apl-source:6

# apl-source:7
# نمرر على القائمة مرة واحدة
# apl-source:8
# نضع كل عنصر في جانبه
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def قسّم_حول(أ, محور):
  # apl-source:19
  أصغر_ = []
  # apl-source:20
  مساوٍ = []
  # apl-source:21
  أكبر_ = []
  # apl-source:22
  for ع in أ:
    # apl-source:23
    if ع < محور:
      # apl-source:24
      أصغر_.append(ع)
    # apl-source:25
    elif ع == محور:
      # apl-source:26
      مساوٍ.append(ع)
    # apl-source:27
    else:
      # apl-source:28
      أكبر_.append(ع)
  # apl-source:29
  return أصغر_ + مساوٍ + أكبر_
# apl-source:30

# apl-source:31
تأكد_يساوي(قسّم_حول([5, 1, 7, 3, 5], 5), [1, 3, 5, 5, 7], "محور خمسة")
# apl-source:32
تأكد_يساوي(قسّم_حول([2, 2], 2), [2, 2], "كلها مساوية")
# apl-source:33
تأكد_يساوي(قسّم_حول([], 1), [], "فارغة")
# apl-source:34
