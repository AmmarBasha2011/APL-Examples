
# apl-source:1
# مثال 2031 — نصان متشابهان في البنية
# apl-source:2
# Isomorphic strings
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2031-isomorphic-strings-two-way-map.apl
# apl-source:6

# apl-source:7
# # نبني خريطتين من الأول للثاني والعكس
# apl-source:8
# # أي تعارض يعني أنهما غير متشابهين
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
def متشابهان(ا, ب):
  # apl-source:19
  if len(ا) != len(ب):
    # apl-source:20
    return False
  # apl-source:21
  خ1 = {}
  # apl-source:22
  خ2 = {}
  # apl-source:23
  for ك in range(len(ا)):
    # apl-source:24
    if ا[ك] in خ1 and خ1[ا[ك]] != ب[ك]:
      # apl-source:25
      return False
    # apl-source:26
    if ب[ك] in خ2 and خ2[ب[ك]] != ا[ك]:
      # apl-source:27
      return False
    # apl-source:28
    خ1[ا[ك]] = ب[ك]
    # apl-source:29
    خ2[ب[ك]] = ا[ك]
  # apl-source:30
  return True
# apl-source:31

# apl-source:32
تأكد_يساوي(متشابهان("egg", "add"), True, "egg")
# apl-source:33
تأكد_يساوي(متشابهان("foo", "bar"), False, "foo")
# apl-source:34
تأكد_يساوي(متشابهان("paper", "title"), True, "paper")
# apl-source:35
تأكد_يساوي(متشابهان("ab", "aa"), False, "اتجاه عكسي")
# apl-source:36
