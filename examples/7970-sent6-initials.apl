# مثال 7970 — الحروف الأولى في الجملة رقم 7
# initials for sentence 7
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7970-sent6-initials.apl

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

تأكد_يساوي(ف("tea for two and two for tea"), "tftatft", "حالة 1")
تأكد_يساوي(ف("in the end the end is the start"), "iteteits", "حالة 2")
تأكد_يساوي(ف("nile river nile delta river"), "nrndr", "حالة 3")
