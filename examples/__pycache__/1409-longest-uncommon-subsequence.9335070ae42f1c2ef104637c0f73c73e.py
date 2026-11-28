
# apl-source:1
# مثال 1409 — أطول متتالية غير مشتركة
# apl-source:2
# Longest uncommon subsequence length
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1409-longest-uncommon-subsequence.apl
# apl-source:6

# apl-source:7
# لو تساوى النصان فلا توجد
# apl-source:8
# وإلا فالأطول منهما نفسه هو الجواب
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
def اطول_غير_مشتركة(أ, ب):
  # apl-source:19
  if أ == ب:
    # apl-source:20
    return -1
  # apl-source:21
  return max(len(أ), len(ب))
# apl-source:22

# apl-source:23
تأكد_يساوي(اطول_غير_مشتركة("aba", "cdc"), 3, "ثلاثة")
# apl-source:24
تأكد_يساوي(اطول_غير_مشتركة("aaa", "aaa"), -1, "متساويان")
# apl-source:25
تأكد_يساوي(اطول_غير_مشتركة("a", "bb"), 2, "طولان مختلفان")
# apl-source:26
