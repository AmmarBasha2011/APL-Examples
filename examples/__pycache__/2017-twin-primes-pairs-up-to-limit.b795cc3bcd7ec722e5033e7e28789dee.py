
# apl-source:1
# مثال 2017 — الأوليات التوأم حتى حد
# apl-source:2
# Twin primes up to limit
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2017-twin-primes-pairs-up-to-limit.apl
# apl-source:6

# apl-source:7
# # نختبر كل عدد p وp+2
# apl-source:8
# # ونجمع الأزواج التي كلاها أولي
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
def توائم(حد):
  # apl-source:29
  خرج = []
  # apl-source:30
  for ع in range(2, حد - 1):
    # apl-source:31
    if اولي(ع) and اولي(ع + 2):
      # apl-source:32
      خرج = خرج + [[ع, ع + 2]]
  # apl-source:33
  return خرج
# apl-source:34

# apl-source:35
تأكد_يساوي(توائم(30), [[3, 5], [5, 7], [11, 13], [17, 19]], "حتى ٣٠")
# apl-source:36
تأكد_يساوي(len(توائم(100)), 8, "حتى ١٠٠")
# apl-source:37
تأكد_يساوي(توائم(4), [], "لا توجد")
# apl-source:38
