
# apl-source:1
# مثال 1009 — نصان متماثلان بنيوياً
# apl-source:2
# Isomorphic strings
# apl-source:3
# Demonstrates: توقيع أول ظهور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1009-isomorphic-strings.apl
# apl-source:6

# apl-source:7
# نصان متماثلان لو أمكن استبدال حروف الأول بحروف الثاني
# apl-source:8
# نحسب لكل نص توقيعاً من فهرس أول ظهور لكل حرف ونقارن التوقيعين
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
def توقيع(نص_):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in range(len(نص_)):
    # apl-source:21
    ف = 0
    # apl-source:22
    while نص_[ف] != نص_[ع]:
      # apl-source:23
      ف = ف + 1
    # apl-source:24
    ناتج = ناتج + [ف]
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
def متماثلان(أ, ب):
  # apl-source:28
  return (len(أ) == len(ب)) and (توقيع(أ) == توقيع(ب))
# apl-source:29

# apl-source:30
تأكد_يساوي(متماثلان("egg", "add"), True, "egg و add")
# apl-source:31
تأكد_يساوي(متماثلان("foo", "bar"), False, "foo و bar")
# apl-source:32
تأكد_يساوي(متماثلان("paper", "title"), True, "paper و title")
# apl-source:33
تأكد_يساوي(متماثلان("ab", "aa"), False, "ربط مزدوج")
# apl-source:34
