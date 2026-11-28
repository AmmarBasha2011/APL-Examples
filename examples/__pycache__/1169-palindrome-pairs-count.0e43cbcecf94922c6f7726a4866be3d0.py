
# apl-source:1
# مثال 1169 — أزواج متناظرة
# apl-source:2
# Palindrome pairs
# apl-source:3
# Demonstrates: فحص مباشر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1169-palindrome-pairs-count.apl
# apl-source:6

# apl-source:7
# نجرب كل زوج مرتب من الكلمات
# apl-source:8
# ونفحص هل اللصق يقرأ بالاتجاهين
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
def متناظر(س):
  # apl-source:19
  return س == س[::-1]
# apl-source:20

# apl-source:21
def ازواج(كلمات):
  # apl-source:22
  ناتج = []
  # apl-source:23
  for ع in range(len(كلمات)):
    # apl-source:24
    for ج in range(len(كلمات)):
      # apl-source:25
      if ع != ج:
        # apl-source:26
        if متناظر(كلمات[ع] + كلمات[ج]):
          # apl-source:27
          ناتج = ناتج + [[ع, ج]]
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(ازواج(["abcd","dcba","lls","s","sssll"]), [[0,1],[1,0],[2,4],[3,2]], "مثال أول")
# apl-source:31
تأكد_يساوي(ازواج(["bat","tab","cat"]), [[0,1],[1,0]], "مثال ثان")
# apl-source:32
تأكد_يساوي(ازواج(["a",""]), [[0,1],[1,0]], "فارغة")
# apl-source:33
