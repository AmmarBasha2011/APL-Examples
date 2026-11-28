
# apl-source:1
# مثال 1024 — الثلاثيات الفيثاغورية
# apl-source:2
# Pythagorean triples
# apl-source:3
# Demonstrates: الجذر الصحيح
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1024-pythagorean-triples.apl
# apl-source:6

# apl-source:7
# أ² + ب² = ج² بأعداد صحيحة
# apl-source:8
# نجرب كل زوج أ < ب ونتحقق أن مجموع المربعين مربع كامل
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
  ج = 0
  # apl-source:20
  while (ج + 1) * (ج + 1) <= ن:
    # apl-source:21
    ج = ج + 1
  # apl-source:22
  return ج
# apl-source:23

# apl-source:24
def ثلاثيات(حد):
  # apl-source:25
  ناتج = []
  # apl-source:26
  for أ in range(1, حد + 1):
    # apl-source:27
    for ب in range(أ + 1, حد + 1):
      # apl-source:28
      ج = جذر_صحيح((أ * أ) + (ب * ب))
      # apl-source:29
      if (ج * ج == (أ * أ) + (ب * ب)) and (ج <= حد):
        # apl-source:30
        ناتج = ناتج + [[أ, ب, ج]]
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
تأكد_يساوي(ثلاثيات(13), [[3, 4, 5], [5, 12, 13], [6, 8, 10]], "حتى ثلاثة عشر")
# apl-source:34
تأكد_يساوي(len(ثلاثيات(20)), 6, "حتى عشرين")
# apl-source:35
تأكد_يساوي(ثلاثيات(4), [], "لا شيء")
# apl-source:36
