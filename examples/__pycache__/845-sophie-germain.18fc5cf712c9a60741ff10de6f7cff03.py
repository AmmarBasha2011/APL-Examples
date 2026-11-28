
# apl-source:1
# مثال 845 — أولية صوفي جرمان
# apl-source:2
# Sophie Germain primes
# apl-source:3
# Demonstrates: ف و 2ف+1 أوليان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/845-sophie-germain.apl
# apl-source:6

# apl-source:7
# أولية صوفي جرمان: ف أولي و 2ف+1 أولي أيضاً
# apl-source:8
# فُقدت في برهان صوفي جرمان لحالة من مبرهنة فيرما الأخيرة
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
def أولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  if ن < 4:
    # apl-source:22
    return 1 == 1
  # apl-source:23
  if ن % 2 == 0:
    # apl-source:24
    return False
  # apl-source:25
  قاسم = 3
  # apl-source:26
  while قاسم * قاسم <= ن:
    # apl-source:27
    if ن % قاسم == 0:
      # apl-source:28
      return False
    # apl-source:29
    قاسم = قاسم + 2
  # apl-source:30
  return 1 == 1
# apl-source:31

# apl-source:32
صوفي = []
# apl-source:33
for ف in range(2, 100):
  # apl-source:34
  if أولي(ف) and أولي(2 * ف + 1):
    # apl-source:35
    صوفي = صوفي + [ف]
# apl-source:36

# apl-source:37
print("أولية صوفي جرمان تحت 100:", صوفي)
# apl-source:38

# apl-source:39
تأكد_يساوي(len(صوفي), 10, "عشرة تحت 100")
# apl-source:40
تأكد_يساوي(صوفي[0], 2, "الأول")
# apl-source:41
تأكد_يساوي(صوفي[3], 11, "الرابع")
# apl-source:42
تأكد_يساوي(صوفي[9], 89, "الأخير")
# apl-source:43

# apl-source:44
# تحقق: 2*41+1 = 83 أولي (الزوج الآمن المقابل)
# apl-source:45
تأكد_يساوي(أولي(83), 1 == 1, "83 أولي آمن")
# apl-source:46
تأكد_يساوي(أولي(15), False, "7 ليست صوفي لأن 15 مفكك")
# apl-source:47
