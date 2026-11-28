
# apl-source:1
# مثال 973 — تحليل فيرما
# apl-source:2
# Fermat factorization
# apl-source:3
# Demonstrates: فرق بين مربعين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/973-fermat-factorization.apl
# apl-source:6

# apl-source:7
# تحليل فيرما: الأعداد القريبة من مربع كامل تتحلل بفرق مربعين
# apl-source:8
# ن = أ^2 - ب^2 = (أ - ب)(أ + ب)
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
def جذر_صحيح(ن):
  # apl-source:19
  ك = 0
  # apl-source:20
  while ((ك + 1) * (ك + 1)) <= ن:
    # apl-source:21
    ك = ك + 1
  # apl-source:22
  return ك
# apl-source:23

# apl-source:24
def حلل_فيرما(ن):
  # apl-source:25
  أ = جذر_صحيح(ن)
  # apl-source:26
  if (أ * أ) < ن:
    # apl-source:27
    أ = أ + 1
  # apl-source:28
  وجد = 0
  # apl-source:29
  عوامل = [0, 0]
  # apl-source:30
  while وجد == 0:
    # apl-source:31
    ب2 = (أ * أ) - ن
    # apl-source:32
    ب = جذر_صحيح(ب2)
    # apl-source:33
    if (ب * ب) == ب2:
      # apl-source:34
      عوامل = [أ - ب, أ + ب]
      # apl-source:35
      وجد = 1
    # apl-source:36
    else:
      # apl-source:37
      أ = أ + 1
  # apl-source:38
  return عوامل
# apl-source:39

# apl-source:40
نتيجة1 = حلل_فيرما(5959)
# apl-source:41
نتيجة2 = حلل_فيرما(10403)
# apl-source:42
تأكد_يساوي(نتيجة1[0], 59, "عامل أول من 5959")
# apl-source:43
تأكد_يساوي(نتيجة1[1], 101, "عامل ثان من 5959")
# apl-source:44
تأكد_يساوي(نتيجة2[0], 101, "عامل أول من 10403")
# apl-source:45
تأكد_يساوي(نتيجة2[1], 103, "عامل ثان من 10403")
# apl-source:46
تأكد_يساوي(5959, 5959, "تحقق الضرب")
# apl-source:47
