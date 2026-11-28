
# apl-source:1
# مثال 2112 — مجموع الأعداد الأولية تحت حد
# apl-source:2
# Sum of primes below limit
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2112-sum-of-primes-below-limit-trial.apl
# apl-source:6

# apl-source:7
# # نختبر كل عدد بالقسمة
# apl-source:8
# # المجموع تحت 100 هو 1060
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
def مجموع(حد):
  # apl-source:29
  مج = 0
  # apl-source:30
  for ن in range(2, حد):
    # apl-source:31
    if اولي(ن):
      # apl-source:32
      مج = مج + ن
  # apl-source:33
  return مج
# apl-source:34

# apl-source:35
تأكد_يساوي(مجموع(10), 17, "تحت ١٠")
# apl-source:36
تأكد_يساوي(مجموع(2), 0, "تحت ٢")
# apl-source:37
تأكد_يساوي(مجموع(100), 1060, "تحت ١٠٠")
# apl-source:38
