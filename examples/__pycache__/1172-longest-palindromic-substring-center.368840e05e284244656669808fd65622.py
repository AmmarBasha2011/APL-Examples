
# apl-source:1
# مثال 1172 — أطول نص متناظر
# apl-source:2
# Longest palindromic substring expand
# apl-source:3
# Demonstrates: توسع من المركز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1172-longest-palindromic-substring-center.apl
# apl-source:6

# apl-source:7
# نوسع من كل مركز
# apl-source:8
# ونحتفظ بأطول نتيجة
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
def اطول_متناظر(س):
  # apl-source:19
  ن = len(س)
  # apl-source:20
  افضل = ""
  # apl-source:21
  for مركز in range(2 * ن - 1):
    # apl-source:22
    ي = مركز // 2
    # apl-source:23
    م = ي + مركز % 2
    # apl-source:24
    while (ي >= 0) and (م < ن) and (س[ي] == س[م]):
      # apl-source:25
      ي = ي - 1
      # apl-source:26
      م = م + 1
    # apl-source:27
    قطعة = س[ي + 1:م]
    # apl-source:28
    if len(قطعة) > len(افضل):
      # apl-source:29
      افضل = قطعة
  # apl-source:30
  return افضل
# apl-source:31

# apl-source:32
تأكد_يساوي(اطول_متناظر("babad"), "bab", "مثال أول")
# apl-source:33
تأكد_يساوي(اطول_متناظر("cbbd"), "bb", "زوجي")
# apl-source:34
تأكد_يساوي(اطول_متناظر("a"), "a", "حرف")
# apl-source:35
تأكد_يساوي(اطول_متناظر("forgeeksskeegfor"), "geeksskeeg", "طويل")
# apl-source:36
