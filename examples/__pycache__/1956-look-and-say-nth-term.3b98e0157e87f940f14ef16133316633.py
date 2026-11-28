
# apl-source:1
# مثال 1956 — متتالية انظر وقل
# apl-source:2
# Look-and-say sequence
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1956-look-and-say-nth-term.apl
# apl-source:6

# apl-source:7
# # نعد التكرارات المتتالية لكل رقم
# apl-source:8
# # ونكتب العدد ثم الرقم
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
def التالي(س):
  # apl-source:19
  خرج = ""
  # apl-source:20
  ك = 0
  # apl-source:21
  while ك < len(س):
    # apl-source:22
    ي = ك
    # apl-source:23
    while ي < len(س) and س[ي] == س[ك]:
      # apl-source:24
      ي = ي + 1
    # apl-source:25
    خرج = خرج + str(ي - ك) + س[ك]
    # apl-source:26
    ك = ي
  # apl-source:27
  return خرج
# apl-source:28

# apl-source:29
def حد(ن):
  # apl-source:30
  س = "1"
  # apl-source:31
  for ك in range(ن - 1):
    # apl-source:32
    س = التالي(س)
  # apl-source:33
  return س
# apl-source:34

# apl-source:35
تأكد_يساوي(حد(1), "1", "الأول")
# apl-source:36
تأكد_يساوي(حد(4), "1211", "الرابع")
# apl-source:37
تأكد_يساوي(حد(6), "312211", "السادس")
# apl-source:38
تأكد_يساوي(len(حد(10)), 20, "طول العاشر")
# apl-source:39
