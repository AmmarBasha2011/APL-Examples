
# apl-source:1
# مثال 5225 — الحد ن في متتالية حسابية فرقها 9
# apl-source:2
# Nth term of arithmetic sequence, step 9
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5225-arith-seq-9.apl
# apl-source:6

# apl-source:7
# الحد = الأول + (ن-1) × الفرق
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(أ, ن):
  # apl-source:18
  return أ + (ن - 1) * 9
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(1, 1), 1, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(1, 10), 82, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(5, 7), 59, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(-3, 4), 24, "حالة 4")
# apl-source:24
