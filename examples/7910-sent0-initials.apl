# مثال 7910 — الحروف الأولى في الجملة رقم 1
# initials for sentence 1
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7910-sent0-initials.apl

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

تأكد_يساوي(ف("the cat and the dog and the bird"), "tcatdatb", "حالة 1")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), "oftfrfbf", "حالة 2")
تأكد_يساوي(ف("run run run fast fast slow"), "rrrffs", "حالة 3")
