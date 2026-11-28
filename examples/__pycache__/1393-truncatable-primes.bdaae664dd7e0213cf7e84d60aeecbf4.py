
# apl-source:1
# مثال 1393 — أولية قابلة للبتر
# apl-source:2
# Truncatable primes
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1393-truncatable-primes.apl
# apl-source:6

# apl-source:7
# نبتر من اليمين ومن اليسار
# apl-source:8
# كل ناتج يجب أن يكون أولياً
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
def اولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  ع = 2
  # apl-source:22
  while ع * ع <= ن:
    # apl-source:23
    if ن % ع == 0:
      # apl-source:24
      return False
    # apl-source:25
    ع = ع + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def قابل_للبتر(ن):
  # apl-source:29
  if ن < 10:
    # apl-source:30
    return False
  # apl-source:31
  ن_نص = str(ن)
  # apl-source:32
  for ع in range(len(ن_نص)):
    # apl-source:33
    if not اولي(int(ن_نص[ع:])):
      # apl-source:34
      return False
    # apl-source:35
    if not اولي(int(ن_نص[:ع + 1])):
      # apl-source:36
      return False
  # apl-source:37
  return True
# apl-source:38

# apl-source:39
def ابحث(حد):
  # apl-source:40
  ناتج = []
  # apl-source:41
  for ن in range(10, حد):
    # apl-source:42
    if قابل_للبتر(ن):
      # apl-source:43
      ناتج = ناتج + [ن]
  # apl-source:44
  return ناتج
# apl-source:45

# apl-source:46
تأكد_يساوي(قابل_للبتر(3797), True, "ثلاثة آلاف")
# apl-source:47
تأكد_يساوي(قابل_للبتر(313), True, "ثلاثمئة وثلاثة عشر")
# apl-source:48
تأكد_يساوي(قابل_للبتر(13), False, "ثلاثة عشر")
# apl-source:49
تأكد_يساوي(ابحث(1000), [23,37,53,73,313,317,373,797], "أقل من ألف")
# apl-source:50
