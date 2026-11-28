# مثال 6185 — النص الناتج بعد أخذ الحروف الساكنة وتحويلها إلى (حرف مكرر)
# str of twice applied to cons chars
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6185-txt-cons-twice-str.apl

# نمر على النص حرفاً حرفاً
# نأخذ الحروف الساكنة فقط
# ونحوّل كل حرف إلى: حرف مكرر
# ثم نحسب: النص الناتج

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = ""
  لكل خ في ن:
    لو خ في "bcdfghjklmnpqrstvwxyz":
      ر = ر + خ + خ
  ارجع ر

تأكد_يساوي(ف("hello world 42"), "hhllllwwrrlldd", "حالة 1")
تأكد_يساوي(ف("apl is fun"), "ppllssffnn", "حالة 2")
تأكد_يساوي(ف("a1b2c3"), "bbcc", "حالة 3")
تأكد_يساوي(ف("the quick brown fox"), "tthhqqcckkbbrrwwnnffxx", "حالة 4")
تأكد_يساوي(ف(""), "", "حالة 5")
تأكد_يساوي(ف("zzz yyy xxx"), "zzzzzzyyyyyyxxxxxx", "حالة 6")
تأكد_يساوي(ف("data 2026 science"), "ddttssccnncc", "حالة 7")
تأكد_يساوي(ف("programming in arabic"), "pprrggrrmmmmnnggnnrrbbcc", "حالة 8")
