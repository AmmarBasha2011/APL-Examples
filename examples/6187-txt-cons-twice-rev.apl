# مثال 6187 — الناتج معكوس بعد أخذ الحروف الساكنة وتحويلها إلى (حرف مكرر)
# rev of twice applied to cons chars
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6187-txt-cons-twice-rev.apl

# نمر على النص حرفاً حرفاً
# نأخذ الحروف الساكنة فقط
# ونحوّل كل حرف إلى: حرف مكرر
# ثم نحسب: الناتج معكوس

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
  ارجع ر[::-1]

تأكد_يساوي(ف("hello world 42"), "ddllrrwwllllhh", "حالة 1")
تأكد_يساوي(ف("apl is fun"), "nnffssllpp", "حالة 2")
تأكد_يساوي(ف("a1b2c3"), "ccbb", "حالة 3")
تأكد_يساوي(ف("the quick brown fox"), "xxffnnwwrrbbkkccqqhhtt", "حالة 4")
تأكد_يساوي(ف(""), "", "حالة 5")
تأكد_يساوي(ف("zzz yyy xxx"), "xxxxxxyyyyyyzzzzzz", "حالة 6")
تأكد_يساوي(ف("data 2026 science"), "ccnnccssttdd", "حالة 7")
تأكد_يساوي(ف("programming in arabic"), "ccbbrrnnggnnmmmmrrggrrpp", "حالة 8")
