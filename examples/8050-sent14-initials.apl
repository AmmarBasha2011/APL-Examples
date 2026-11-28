# مثال 8050 — الحروف الأولى في الجملة رقم 15
# initials for sentence 15
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8050-sent14-initials.apl

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

تأكد_يساوي(ف("learn code learn more code more"), "lclmcm", "حالة 1")
تأكد_يساوي(ف("bread milk bread eggs milk bread"), "bmbemb", "حالة 2")
تأكد_يساوي(ف("to be or not to be"), "tbontb", "حالة 3")
