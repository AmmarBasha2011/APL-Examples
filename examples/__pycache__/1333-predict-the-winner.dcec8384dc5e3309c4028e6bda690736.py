
# apl-source:1
# مثال 1333 — توقع الفائز
# apl-source:2
# Predict the winner
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1333-predict-the-winner.apl
# apl-source:6

# apl-source:7
# نحسب أفضل فارق للاعب الحالي في كل مجال
# apl-source:8
# الفارق غير السالب يعني فوز الأول أو التعادل
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
def الأول_يفوز(أرقام):
  # apl-source:19
  ن = len(أرقام)
  # apl-source:20
  ف = أرقام[:]
  # apl-source:21
  for بعد in range(1, ن):
    # apl-source:22
    for ي in range(0, ن - بعد):
      # apl-source:23
      ف[ي] = max(أرقام[ي] - ف[ي + 1], أرقام[ي + بعد] - ف[ي])
  # apl-source:24
  return ف[0] >= 0
# apl-source:25

# apl-source:26
تأكد_يساوي(الأول_يفوز([1,5,2]), False, "يخسر")
# apl-source:27
تأكد_يساوي(الأول_يفوز([1,5,233,7]), True, "يفوز")
# apl-source:28
تأكد_يساوي(الأول_يفوز([2]), True, "رقم واحد")
# apl-source:29
