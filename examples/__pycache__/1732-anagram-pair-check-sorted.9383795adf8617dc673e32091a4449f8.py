
# apl-source:1
# مثال 1732 — هل الكلمتان جناس
# apl-source:2
# Anagram check by sorted letters
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1732-anagram-pair-check-sorted.apl
# apl-source:6

# apl-source:7
# نرتب حروف الكلمة
# apl-source:8
# نقارن القائمتين
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
def حروف_مرتبة(س):
  # apl-source:19
  ح = []
  # apl-source:20
  for ك in س:
    # apl-source:21
    ح.append(ك)
  # apl-source:22
  ح.sort()
  # apl-source:23
  return ح
# apl-source:24

# apl-source:25
def جناس(أ, ب):
  # apl-source:26
  return حروف_مرتبة(أ) == حروف_مرتبة(ب)
# apl-source:27

# apl-source:28
تأكد_يساوي(جناس("listen", "silent"), True, "جناس")
# apl-source:29
تأكد_يساوي(جناس("abc", "abd"), False, "ليس جناساً")
# apl-source:30
تأكد_يساوي(جناس("a", "aa"), False, "طول مختلف")
# apl-source:31
