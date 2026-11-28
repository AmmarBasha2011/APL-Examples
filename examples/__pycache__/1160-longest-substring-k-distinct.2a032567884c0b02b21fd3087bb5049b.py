
# apl-source:1
# مثال 1160 — أطول نص بحروف مميزة
# apl-source:2
# Longest substring with k distinct
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1160-longest-substring-k-distinct.apl
# apl-source:6

# apl-source:7
# نوسع النافذة ونعد الحروف فيها
# apl-source:8
# ونضيق من اليسار عند تجاوز k
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
def اطول_نص(س, ك):
  # apl-source:19
  عد = {}
  # apl-source:20
  يسار = 0
  # apl-source:21
  اطول = 0
  # apl-source:22
  for يمين in range(len(س)):
    # apl-source:23
    ح = س[يمين]
    # apl-source:24
    عد[ح] = عد.get(ح, 0) + 1
    # apl-source:25
    while len(عد) > ك:
      # apl-source:26
      ي = س[يسار]
      # apl-source:27
      عد[ي] = عد[ي] - 1
      # apl-source:28
      if عد[ي] == 0:
        # apl-source:29
        عد.pop(ي)
      # apl-source:30
      يسار = يسار + 1
    # apl-source:31
    if يمين - يسار + 1 > اطول:
      # apl-source:32
      اطول = يمين - يسار + 1
  # apl-source:33
  return اطول
# apl-source:34

# apl-source:35
تأكد_يساوي(اطول_نص("eceba", 2), 3, "مثال أول")
# apl-source:36
تأكد_يساوي(اطول_نص("aa", 1), 2, "حرف واحد")
# apl-source:37
تأكد_يساوي(اطول_نص("abcabc", 3), 6, "الكل")
# apl-source:38
تأكد_يساوي(اطول_نص("abc", 0), 0, "صفر")
# apl-source:39
