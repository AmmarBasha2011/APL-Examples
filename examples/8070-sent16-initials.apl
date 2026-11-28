# مثال 8070 — الحروف الأولى في الجملة رقم 17
# initials for sentence 17
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8070-sent16-initials.apl

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

تأكد_يساوي(ف("sun sand sea sun sand sun"), "ssssss", "حالة 1")
تأكد_يساوي(ف("yes no yes yes no maybe"), "ynyynm", "حالة 2")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), "oftfrfbf", "حالة 3")
