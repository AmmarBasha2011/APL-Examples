
# apl-source:1
# مثال 2114 — أكبر فجوة بين أوليين متتاليين
# apl-source:2
# Largest prime gap below limit
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2114-largest-prime-gap-below-limit.apl
# apl-source:6

# apl-source:7
# # الفجوة تحت 100 هي 8 بين 89 و97
# apl-source:8
# # تحت 30 هي 6 بين 23 و29
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
  د = 2
  # apl-source:22
  while د * د <= ن:
    # apl-source:23
    if ن % د == 0:
      # apl-source:24
      return False
    # apl-source:25
    د = د + 1
  # apl-source:26
  return True
# apl-source:27

# apl-source:28
def اكبر_فجوة(حد):
  # apl-source:29
  سابق = 2
  # apl-source:30
  افضل = 0
  # apl-source:31
  for ن in range(3, حد):
    # apl-source:32
    if اولي(ن):
      # apl-source:33
      افضل = max(افضل, ن - سابق)
      # apl-source:34
      سابق = ن
  # apl-source:35
  return افضل
# apl-source:36

# apl-source:37
تأكد_يساوي(اكبر_فجوة(30), 6, "تحت ٣٠")
# apl-source:38
تأكد_يساوي(اكبر_فجوة(100), 8, "تحت ١٠٠")
# apl-source:39
تأكد_يساوي(اكبر_فجوة(4), 1, "تحت ٤")
# apl-source:40
