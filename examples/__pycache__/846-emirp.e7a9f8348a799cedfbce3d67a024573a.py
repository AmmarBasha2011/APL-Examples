
# apl-source:1
# مثال 846 — أولية إيمرب
# apl-source:2
# Emirp primes
# apl-source:3
# Demonstrates: أولي يعكس أولياً مختلفاً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/846-emirp.apl
# apl-source:6

# apl-source:7
# أولية إيمرب: أولي يبقى أولياً عند عكس أرقامه (وليس متناظراً)
# apl-source:8
# "إيمرب" هو "برايم" (أولي) مقلوباً
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
def اعكس_أرقام(ن):
  # apl-source:33
  مقلوب = 0
  # apl-source:34
  م = ن
  # apl-source:35
  while م > 0:
    # apl-source:36
    مقلوب = مقلوب * 10 + م % 10
    # apl-source:37
    م = م // 10
  # apl-source:38
  return مقلوب
# apl-source:39

# apl-source:40
إيمرب = []
# apl-source:41
for ف in range(2, 100):
  # apl-source:42
  if أولي(ف):
    # apl-source:43
    مقلوب = اعكس_أرقام(ف)
    # apl-source:44
    if مقلوب != ف and أولي(مقلوب):
      # apl-source:45
      إيمرب = إيمرب + [ف]
# apl-source:46

# apl-source:47
print("إيمرب تحت 100:", إيمرب)
# apl-source:48

# apl-source:49
تأكد_يساوي(len(إيمرب), 8, "ثمانية تحت 100")
# apl-source:50
تأكد_يساوي(إيمرب[0], 13, "الأول")
# apl-source:51
تأكد_يساوي(إيمرب[7], 97, "الأخير")
# apl-source:52

# apl-source:53
# المتناظرات مستبعدة رغم أنها أولية
# apl-source:54
تأكد_يساوي(أولي(11), 1 == 1, "11 أولي")
# apl-source:55
تأكد_يساوي(اعكس_أرقام(11), 11, "لكن 11 متناظر فليس إيمرب")
# apl-source:56
