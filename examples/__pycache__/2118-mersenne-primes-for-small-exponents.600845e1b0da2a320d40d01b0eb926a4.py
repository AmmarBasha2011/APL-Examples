
# apl-source:1
# مثال 2118 — أوليات ميرسين لأسس صغيرة
# apl-source:2
# Mersenne primes small exponents
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2118-mersenne-primes-for-small-exponents.apl
# apl-source:6

# apl-source:7
# # الأسس حتى 13
# apl-source:8
# # 11 يفشل لأن 2047 = 23×89
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
def ميرسين(حد):
  # apl-source:29
  خرج = []
  # apl-source:30
  for ب in range(2, حد + 1):
    # apl-source:31
    if اولي(ب) and اولي(2 ** ب - 1):
      # apl-source:32
      خرج = خرج + [2 ** ب - 1]
  # apl-source:33
  return خرج
# apl-source:34

# apl-source:35
تأكد_يساوي(ميرسين(13), [3, 7, 31, 127, 8191], "حتى ١٣")
# apl-source:36
تأكد_يساوي(ميرسين(3), [3, 7], "حتى ٣")
# apl-source:37
