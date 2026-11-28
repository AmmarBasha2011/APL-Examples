
# apl-source:1
# مثال 1228 — عد الأوليات
# apl-source:2
# Count primes with bit sieve
# apl-source:3
# Demonstrates: غربال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1228-count-primes-segment.apl
# apl-source:6

# apl-source:7
# نشطب مضاعفات كل أولي بدءاً من مربعه
# apl-source:8
# ونعد ما بقي
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
def عد_اوليات(ن):
  # apl-source:19
  if ن < 3:
    # apl-source:20
    return 0
  # apl-source:21
  اولي = [True] * ن
  # apl-source:22
  اولي[0] = False
  # apl-source:23
  اولي[1] = False
  # apl-source:24
  ع = 2
  # apl-source:25
  while ع * ع < ن:
    # apl-source:26
    if اولي[ع]:
      # apl-source:27
      for ك in range(ع * ع, ن, ع):
        # apl-source:28
        اولي[ك] = False
    # apl-source:29
    ع = ع + 1
  # apl-source:30
  ناتج = 0
  # apl-source:31
  for ق in اولي:
    # apl-source:32
    if ق:
      # apl-source:33
      ناتج = ناتج + 1
  # apl-source:34
  return ناتج
# apl-source:35

# apl-source:36
تأكد_يساوي(عد_اوليات(10), 4, "عشرة")
# apl-source:37
تأكد_يساوي(عد_اوليات(100), 25, "مئة")
# apl-source:38
تأكد_يساوي(عد_اوليات(2), 0, "اثنان")
# apl-source:39
تأكد_يساوي(عد_اوليات(1000), 168, "ألف")
# apl-source:40
