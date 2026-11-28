
# apl-source:1
# مثال 1162 — أصغر نافذة
# apl-source:2
# Minimum window substring
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1162-min-window-substring.apl
# apl-source:6

# apl-source:7
# نعد الحروف المطلوبة ونوسع النافذة
# apl-source:8
# وكلما اكتملت ضيقنا من اليسار وسجلنا الأقصر
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
def اصغر_نافذة(س, ن):
  # apl-source:19
  if ن == "":
    # apl-source:20
    return ""
  # apl-source:21
  مطل = {}
  # apl-source:22
  for ح in ن:
    # apl-source:23
    مطل[ح] = مطل.get(ح, 0) + 1
  # apl-source:24
  ناقص = len(ن)
  # apl-source:25
  يسار = 0
  # apl-source:26
  افضل_بداية = -1
  # apl-source:27
  افضل_طول = len(س) + 1
  # apl-source:28
  for يمين in range(len(س)):
    # apl-source:29
    ح = س[يمين]
    # apl-source:30
    if ح in مطل:
      # apl-source:31
      if مطل[ح] > 0:
        # apl-source:32
        ناقص = ناقص - 1
      # apl-source:33
      مطل[ح] = مطل[ح] - 1
    # apl-source:34
    while ناقص == 0:
      # apl-source:35
      if يمين - يسار + 1 < افضل_طول:
        # apl-source:36
        افضل_طول = يمين - يسار + 1
        # apl-source:37
        افضل_بداية = يسار
      # apl-source:38
      ي = س[يسار]
      # apl-source:39
      if ي in مطل:
        # apl-source:40
        مطل[ي] = مطل[ي] + 1
        # apl-source:41
        if مطل[ي] > 0:
          # apl-source:42
          ناقص = ناقص + 1
      # apl-source:43
      يسار = يسار + 1
  # apl-source:44
  if افضل_بداية == -1:
    # apl-source:45
    return ""
  # apl-source:46
  return س[افضل_بداية:افضل_بداية + افضل_طول]
# apl-source:47

# apl-source:48
تأكد_يساوي(اصغر_نافذة("ADOBECODEBANC", "ABC"), "BANC", "مثال أول")
# apl-source:49
تأكد_يساوي(اصغر_نافذة("a", "a"), "a", "حرف")
# apl-source:50
تأكد_يساوي(اصغر_نافذة("a", "aa"), "", "ناقص")
# apl-source:51
تأكد_يساوي(اصغر_نافذة("abc", ""), "", "نمط فارغ")
# apl-source:52
