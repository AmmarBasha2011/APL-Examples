
# apl-source:1
# مثال 2113 — العدد الأولي رقم ن
# apl-source:2
# Nth prime by counting
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2113-nth-prime-by-counting-primes.apl
# apl-source:6

# apl-source:7
# # نختبر الأعداد تباعا
# apl-source:8
# # الأولي رقم 100 هو 541
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
def الاولي_رقم(ن):
  # apl-source:29
  عدد = 0
  # apl-source:30
  م = 1
  # apl-source:31
  while عدد < ن:
    # apl-source:32
    م = م + 1
    # apl-source:33
    if اولي(م):
      # apl-source:34
      عدد = عدد + 1
  # apl-source:35
  return م
# apl-source:36

# apl-source:37
تأكد_يساوي(الاولي_رقم(1), 2, "الأول")
# apl-source:38
تأكد_يساوي(الاولي_رقم(6), 13, "السادس")
# apl-source:39
تأكد_يساوي(الاولي_رقم(10), 29, "العاشر")
# apl-source:40
تأكد_يساوي(الاولي_رقم(25), 97, "الخامس والعشرون")
# apl-source:41
تأكد_يساوي(الاولي_رقم(100), 541, "المئة")
# apl-source:42
