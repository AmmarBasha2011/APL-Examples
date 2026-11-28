
# apl-source:1
# مثال 1411 — نصان صديقان
# apl-source:2
# Buddy strings one swap
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1411-buddy-strings.apl
# apl-source:6

# apl-source:7
# إن اختلف في موضعين متقابلين فهما صديقان
# apl-source:8
# وإن تساويا فيجب وجود حرف مكرر
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
def اصدقاء(أ, ب):
  # apl-source:19
  if len(أ) != len(ب):
    # apl-source:20
    return False
  # apl-source:21
  if أ == ب:
    # apl-source:22
    مرئي = {}
    # apl-source:23
    for ح in أ:
      # apl-source:24
      if مرئي.get(ح, False):
        # apl-source:25
        return True
      # apl-source:26
      مرئي[ح] = True
    # apl-source:27
    return False
  # apl-source:28
  فروق = []
  # apl-source:29
  for ع in range(len(أ)):
    # apl-source:30
    if أ[ع] != ب[ع]:
      # apl-source:31
      فروق = فروق + [ع]
  # apl-source:32
  if len(فروق) != 2:
    # apl-source:33
    return False
  # apl-source:34
  return (أ[فروق[0]] == ب[فروق[1]]) and (أ[فروق[1]] == ب[فروق[0]])
# apl-source:35

# apl-source:36
تأكد_يساوي(اصدقاء("ab", "ba"), True, "تبديل")
# apl-source:37
تأكد_يساوي(اصدقاء("ab", "ab"), False, "بلا تكرار")
# apl-source:38
تأكد_يساوي(اصدقاء("aa", "aa"), True, "مع تكرار")
# apl-source:39
تأكد_يساوي(اصدقاء("aaaaaaabc", "aaaaaaacb"), True, "طويل")
# apl-source:40
