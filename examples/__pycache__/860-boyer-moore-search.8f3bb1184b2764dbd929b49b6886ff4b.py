
# apl-source:1
# مثال 860 — بحث بوير-مور
# apl-source:2
# Boyer-Moore search
# apl-source:3
# Demonstrates: قاعدة الحرف السيئ، مقارنة معكوسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/860-boyer-moore-search.apl
# apl-source:6

# apl-source:7
# بوير-مور: بحث نمط بقاعدة الحرف السيئ، يقفز أكثر من موضع
# apl-source:8
# على عكس KMP يقارن النمط من نهايته لبدايته
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
def آخر_موضع(نمط, حرف):
  # apl-source:19
  آخر = -1
  # apl-source:20
  for i in range(len(نمط)):
    # apl-source:21
    if نمط[i] == حرف:
      # apl-source:22
      آخر = i
  # apl-source:23
  return آخر
# apl-source:24

# apl-source:25
def بحث_بوير_مور(نص, نمط):
  # apl-source:26
  مواضع = []
  # apl-source:27
  ط_نمط = len(نمط)
  # apl-source:28
  i = 0
  # apl-source:29
  while i <= len(نص) - ط_نمط:
    # apl-source:30
    ج = ط_نمط - 1
    # apl-source:31
    while ج >= 0 and نمط[ج] == نص[i + ج]:
      # apl-source:32
      ج = ج - 1
    # apl-source:33
    if ج < 0:
      # apl-source:34
      مواضع = مواضع + [i]
      # apl-source:35
      i = i + 1
    # apl-source:36
    else:
      # apl-source:37
      قفزة = ج - آخر_موضع(نمط, نص[i + ج])
      # apl-source:38
      if قفزة < 1:
        # apl-source:39
        قفزة = 1
      # apl-source:40
      i = i + قفزة
  # apl-source:41
  return مواضع
# apl-source:42

# apl-source:43
نص = "GCATCGCAGAGAGTATACAGTACG"
# apl-source:44
مواضع = بحث_بوير_مور(نص, "GCAG")
# apl-source:45
print("مواضع GCAG:", مواضع)
# apl-source:46

# apl-source:47
تأكد_يساوي(len(مواضع), 1, "تطابق واحد")
# apl-source:48
تأكد_يساوي(مواضع[0], 5, "في الموضع 5")
# apl-source:49

# apl-source:50
# نمط متكرر: aab في aabaaabaaab يظهر في 0 و4 و8
# apl-source:51
مواضع2 = بحث_بوير_مور("aabaaabaaab", "aab")
# apl-source:52
print("مواضع aab:", مواضع2)
# apl-source:53
تأكد_يساوي(len(مواضع2), 3, "ثلاثة تطابقات")
# apl-source:54
تأكد_يساوي(مواضع2[0], 0, "الأول")
# apl-source:55
تأكد_يساوي(مواضع2[1], 4, "الثاني")
# apl-source:56
تأكد_يساوي(مواضع2[2], 8, "الثالث")
# apl-source:57

# apl-source:58
# لا تطابق
# apl-source:59
تأكد_يساوي(len(بحث_بوير_مور("abcabc", "xyz")), 0, "لا تطابق")
# apl-source:60
