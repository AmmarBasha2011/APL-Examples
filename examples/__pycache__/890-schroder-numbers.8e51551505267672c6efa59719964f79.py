
# apl-source:1
# مثال 890 — أعداد شرودر
# apl-source:2
# Schroder numbers
# apl-source:3
# Demonstrates: مسارات بخطوة قطرية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/890-schroder-numbers.apl
# apl-source:6

# apl-source:7
# أعداد شرودر الكبيرة: مسارات شبكة بخطوات يمين/أعلى/قطر دون تجاوز القطر
# apl-source:8
# S(n) = S(n-1) + مجموع S(k)*S(n-1-k) مع S0=1 و S1=2
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
def شرودر(ن):
  # apl-source:19
  س = [1, 2]
  # apl-source:20
  for i in range(2, ن + 1):
    # apl-source:21
    مجموع = س[i - 1]
    # apl-source:22
    for ك in range(i - 1):
      # apl-source:23
      مجموع = مجموع + س[ك] * س[i - 1 - ك]
    # apl-source:24
    س = س + [مجموع]
  # apl-source:25
  return س
# apl-source:26

# apl-source:27
س = شرودر(6)
# apl-source:28
print("S0..S6:", س)
# apl-source:29

# apl-source:30
تأكد_يساوي(س[0], 1, "S0 = 1")
# apl-source:31
تأكد_يساوي(س[1], 2, "S1 = 2")
# apl-source:32
تأكد_يساوي(س[2], 4, "S2 = 4")
# apl-source:33
تأكد_يساوي(س[3], 12, "S3 = 12")
# apl-source:34
تأكد_يساوي(س[4], 40, "S4 = 40")
# apl-source:35
تأكد_يساوي(س[5], 144, "S5 = 144")
# apl-source:36
تأكد_يساوي(س[6], 544, "S6 = 544")
# apl-source:37

# apl-source:38
# شرودر الصغيرة هي نصف الكبيرة (ما عدا الأولى)
# apl-source:39
تأكد_يساوي(س[3] // 2, 6, "الصغيرة s3 = 6")
# apl-source:40
تأكد_يساوي(س[4] // 2, 20, "الصغيرة s4 = 20")
# apl-source:41
