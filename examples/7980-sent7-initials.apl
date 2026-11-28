# مثال 7980 — الحروف الأولى في الجملة رقم 8
# initials for sentence 8
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7980-sent7-initials.apl

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

تأكد_يساوي(ف("run run run fast fast slow"), "rrrffs", "حالة 1")
تأكد_يساوي(ف("red blue green red blue red"), "rbgrbr", "حالة 2")
تأكد_يساوي(ف("learn code learn more code more"), "lclmcm", "حالة 3")
