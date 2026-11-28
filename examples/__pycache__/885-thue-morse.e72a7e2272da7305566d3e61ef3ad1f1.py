
# apl-source:1
# مثال 885 — متتابعة ثيو-مورس
# apl-source:2
# Thue-Morse sequence
# apl-source:3
# Demonstrates: توليد بالمتمم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/885-thue-morse.apl
# apl-source:6

# apl-source:7
# متتابعة ثيو-مورس: كل حد هو متمم السابق (0 -> 01 -> 0110 -> ...)
# apl-source:8
# لا تحتوي أي تكرار ثلاثي متتال، وتظهر في نظرية الألعاب
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
def ثيو_مورس(عدد):
  # apl-source:19
  ت = [0]
  # apl-source:20
  while len(ت) < عدد:
    # apl-source:21
    نصف = len(ت)
    # apl-source:22
    for i in range(نصف):
      # apl-source:23
      if len(ت) < عدد:
        # apl-source:24
        if ت[i] == 0:
          # apl-source:25
          ت = ت + [1]
        # apl-source:26
        else:
          # apl-source:27
          ت = ت + [0]
  # apl-source:28
  return ت
# apl-source:29

# apl-source:30
ت = ثيو_مورس(16)
# apl-source:31
print("أول 16 حداً:", ت)
# apl-source:32

# apl-source:33
تأكد_يساوي(len(ت), 16, "الطول")
# apl-source:34
تأكد_يساوي(ت[0], 0, "ت[0]")
# apl-source:35
تأكد_يساوي(ت[1], 1, "ت[1]")
# apl-source:36
تأكد_يساوي(ت[3], 0, "ت[3]")
# apl-source:37
تأكد_يساوي(ت[8], 1, "ت[8]")
# apl-source:38
تأكد_يساوي(ت[15], 0, "ت[15]")
# apl-source:39

# apl-source:40
# تعريف بديل: ت[ن] = زوجية عدد الواحدات في تمثيل ن الثنائي
# apl-source:41
def زوجية_الواحدات(ن):
  # apl-source:42
  عد = 0
  # apl-source:43
  م = ن
  # apl-source:44
  while م > 0:
    # apl-source:45
    عد = عد + م % 2
    # apl-source:46
    م = م // 2
  # apl-source:47
  return عد % 2
# apl-source:48

# apl-source:49
for ن in range(16):
  # apl-source:50
  تأكد_يساوي(ت[ن], زوجية_الواحدات(ن), "التعريف البديل عند " + str(ن))
# apl-source:51

# apl-source:52
# خاصية التمام: النصف الثاني متمم الأول
# apl-source:53
for i in range(8):
  # apl-source:54
  تأكد_يساوي(ت[i] + ت[i + 8], 1, "التمام عند " + str(i))
# apl-source:55
