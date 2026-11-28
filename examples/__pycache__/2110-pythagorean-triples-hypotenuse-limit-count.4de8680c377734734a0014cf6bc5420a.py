
# apl-source:1
# مثال 2110 — عدد الثلاثيات الفيثاغورية حتى وتر معين
# apl-source:2
# Pythagorean triples count
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2110-pythagorean-triples-hypotenuse-limit-count.apl
# apl-source:6

# apl-source:7
# # نجرب كل a وb ونفحص c صحيح
# apl-source:8
# # الثلاثيات المضاعفة تحسب
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
def عد_ثلاثيات(حد):
  # apl-source:19
  عدد = 0
  # apl-source:20
  for ا in range(1, حد + 1):
    # apl-source:21
    for ب in range(ا + 1, حد + 1):
      # apl-source:22
      م = ا * ا + ب * ب
      # apl-source:23
      ج = 1
      # apl-source:24
      while ج * ج < م:
        # apl-source:25
        ج = ج + 1
      # apl-source:26
      if ج * ج == م and ج <= حد:
        # apl-source:27
        عدد = عدد + 1
  # apl-source:28
  return عدد
# apl-source:29

# apl-source:30
تأكد_يساوي(عد_ثلاثيات(4), 0, "٤")
# apl-source:31
تأكد_يساوي(عد_ثلاثيات(5), 1, "٥")
# apl-source:32
تأكد_يساوي(عد_ثلاثيات(13), 3, "١٣")
# apl-source:33
تأكد_يساوي(عد_ثلاثيات(20), 6, "٢٠")
# apl-source:34
