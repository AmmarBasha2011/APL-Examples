# مثال 6202 — الناتج معكوس بعد أخذ غير المسافات وتحويلها إلى (حرف مكرر)
# rev of twice applied to nospace chars
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6202-txt-nospace-twice-rev.apl

# نمر على النص حرفاً حرفاً
# نأخذ غير المسافات فقط
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
    لو خ != " ":
      ر = ر + خ + خ
  ارجع ر[::-1]

تأكد_يساوي(ف("hello world 42"), "2244ddllrroowwoolllleehh", "حالة 1")
تأكد_يساوي(ف("apl is fun"), "nnuuffssiillppaa", "حالة 2")
تأكد_يساوي(ف("a1b2c3"), "33cc22bb11aa", "حالة 3")
تأكد_يساوي(ف("the quick brown fox"), "xxooffnnwwoorrbbkkcciiuuqqeehhtt", "حالة 4")
تأكد_يساوي(ف(""), "", "حالة 5")
تأكد_يساوي(ف("zzz yyy xxx"), "xxxxxxyyyyyyzzzzzz", "حالة 6")
تأكد_يساوي(ف("data 2026 science"), "eeccnneeiiccss66220022aattaadd", "حالة 7")
تأكد_يساوي(ف("programming in arabic"), "cciibbaarraanniiggnniimmmmaarrggoorrpp", "حالة 8")
