
# apl-source:1
# مثال 1237 — بادئة مشتركة بشجرة
# apl-source:2
# Longest common prefix via sorting
# apl-source:3
# Demonstrates: ترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1237-longest-common-prefix-trie.apl
# apl-source:6

# apl-source:7
# بعد الترتيب أبعد كلمتين هما الأولى والأخيرة
# apl-source:8
# فالبادئة المشتركة بينهما مشتركة للجميع
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
def بادئة(كلمات):
  # apl-source:19
  if len(كلمات) == 0:
    # apl-source:20
    return ""
  # apl-source:21
  م = sorted(كلمات)
  # apl-source:22
  أ = م[0]
  # apl-source:23
  ب = م[-1]
  # apl-source:24
  ع = 0
  # apl-source:25
  while (ع < len(أ)) and (ع < len(ب)) and (أ[ع] == ب[ع]):
    # apl-source:26
    ع = ع + 1
  # apl-source:27
  return أ[:ع]
# apl-source:28

# apl-source:29
تأكد_يساوي(بادئة(["flower","flow","flight"]), "fl", "مثال أول")
# apl-source:30
تأكد_يساوي(بادئة(["dog","racecar","car"]), "", "لا بادئة")
# apl-source:31
تأكد_يساوي(بادئة(["a"]), "a", "كلمة")
# apl-source:32
تأكد_يساوي(بادئة([]), "", "فارغة")
# apl-source:33
