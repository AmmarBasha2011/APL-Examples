
# apl-source:1
# مثال 2092 — عدد مرات الجمعة الثالث عشر في سنة
# apl-source:2
# Friday the thirteenth count
# apl-source:3
# Demonstrates: تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2092-friday-thirteenth-count-in-year.apl
# apl-source:6

# apl-source:7
# # الجمعة تساوي 5 في طريقة ساكاموتو
# apl-source:8
# # نعد المرات خلال السنة
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
def يوم(س, ش, ي):
  # apl-source:19
  ج = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  # apl-source:20
  if ش < 3:
    # apl-source:21
    س = س - 1
  # apl-source:22
  return (س + س // 4 - س // 100 + س // 400 + ج[ش - 1] + ي) % 7
# apl-source:23

# apl-source:24
def جمعات(س):
  # apl-source:25
  عدد = 0
  # apl-source:26
  for ش in range(1, 13):
    # apl-source:27
    if يوم(س, ش, 13) == 5:
      # apl-source:28
      عدد = عدد + 1
  # apl-source:29
  return عدد
# apl-source:30

# apl-source:31
تأكد_يساوي(جمعات(2026), 3, "٢٠٢٦")
# apl-source:32
تأكد_يساوي(جمعات(2012), 3, "٢٠١٢")
# apl-source:33
تأكد_يساوي(جمعات(2020), 2, "٢٠٢٠")
# apl-source:34
