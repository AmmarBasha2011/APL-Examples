
# apl-source:1
# مثال 2119 — الأعداد التامة من أوليات ميرسين
# apl-source:2
# Perfect numbers from Mersenne primes
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2119-perfect-numbers-from-mersenne-primes.apl
# apl-source:6

# apl-source:7
# # نستخدم الأسس 2 و3 و5 و7
# apl-source:8
# # وننتج 6 و28 و496 و8128
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
def تامة(حد):
  # apl-source:29
  خرج = []
  # apl-source:30
  for ب in range(2, حد + 1):
    # apl-source:31
    if اولي(ب) and اولي(2 ** ب - 1):
      # apl-source:32
      خرج = خرج + [2 ** (ب - 1) * (2 ** ب - 1)]
  # apl-source:33
  return خرج
# apl-source:34

# apl-source:35
تأكد_يساوي(تامة(7), [6, 28, 496, 8128], "أربعة")
# apl-source:36
تأكد_يساوي(تامة(2), [6], "واحد")
# apl-source:37
