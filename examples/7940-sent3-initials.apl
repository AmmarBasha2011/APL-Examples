# مثال 7940 — الحروف الأولى في الجملة رقم 4
# initials for sentence 4
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7940-sent3-initials.apl

# نقسم الجملة إلى كلمات
# ونعالجها حسب المطلوب

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = ""
  لكل ك في ن.split(" "):
    ر = ر + ك[0]
  ارجع ر

تأكد_يساوي(ف("one fish two fish red fish blue fish"), "oftfrfbf", "حالة 1")
تأكد_يساوي(ف("tea for two and two for tea"), "tftatft", "حالة 2")
تأكد_يساوي(ف("red blue green red blue red"), "rbgrbr", "حالة 3")
