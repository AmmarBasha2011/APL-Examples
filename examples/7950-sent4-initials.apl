# مثال 7950 — الحروف الأولى في الجملة رقم 5
# initials for sentence 5
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7950-sent4-initials.apl

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

تأكد_يساوي(ف("a rose is a rose is a rose"), "ariariar", "حالة 1")
تأكد_يساوي(ف("run run run fast fast slow"), "rrrffs", "حالة 2")
تأكد_يساوي(ف("up down up down up up down"), "ududuud", "حالة 3")
