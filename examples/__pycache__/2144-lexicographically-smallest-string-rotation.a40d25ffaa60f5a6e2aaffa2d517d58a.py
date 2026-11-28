
# apl-source:1
# مثال 2144 — أصغر دوران ترتيبا معجميا
# apl-source:2
# Smallest string rotation
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2144-lexicographically-smallest-string-rotation.apl
# apl-source:6

# apl-source:7
# # نبني الدوران بالتقطيع
# apl-source:8
# # ونحتفظ بالأصغر
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
def اصغر_دوران(س):
  # apl-source:19
  افضل = س
  # apl-source:20
  for ك in range(len(س)):
    # apl-source:21
    د = س[ك:] + س[:ك]
    # apl-source:22
    if د < افضل:
      # apl-source:23
      افضل = د
  # apl-source:24
  return افضل
# apl-source:25

# apl-source:26
تأكد_يساوي(اصغر_دوران("bca"), "abc", "bca")
# apl-source:27
تأكد_يساوي(اصغر_دوران("cba"), "acb", "cba")
# apl-source:28
تأكد_يساوي(اصغر_دوران("aaa"), "aaa", "aaa")
# apl-source:29
