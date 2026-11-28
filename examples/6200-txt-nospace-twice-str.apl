# مثال 6200 — النص الناتج بعد أخذ غير المسافات وتحويلها إلى (حرف مكرر)
# str of twice applied to nospace chars
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6200-txt-nospace-twice-str.apl

# نمر على النص حرفاً حرفاً
# نأخذ غير المسافات فقط
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
    لو خ != " ":
      ر = ر + خ + خ
  ارجع ر

تأكد_يساوي(ف("hello world 42"), "hheelllloowwoorrlldd4422", "حالة 1")
تأكد_يساوي(ف("apl is fun"), "aapplliissffuunn", "حالة 2")
تأكد_يساوي(ف("a1b2c3"), "aa11bb22cc33", "حالة 3")
تأكد_يساوي(ف("the quick brown fox"), "tthheeqquuiicckkbbrroowwnnffooxx", "حالة 4")
تأكد_يساوي(ف(""), "", "حالة 5")
تأكد_يساوي(ف("zzz yyy xxx"), "zzzzzzyyyyyyxxxxxx", "حالة 6")
تأكد_يساوي(ف("data 2026 science"), "ddaattaa22002266sscciieennccee", "حالة 7")
تأكد_يساوي(ف("programming in arabic"), "pprrooggrraammmmiinnggiinnaarraabbiicc", "حالة 8")
