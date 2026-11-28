
# apl-source:1
# مثال 1517 — إجمالي الفاتورة مع الضريبة
# apl-source:2
# Invoice total with VAT
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1517-invoice-total-with-vat.apl
# apl-source:6

# apl-source:7
# نجمع سعر كل بند في كميته
# apl-source:8
# نضيف 14 بالمئة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def إجمالي_الفاتورة(بنود, ضريبة):
  # apl-source:19
  صافي = 0
  # apl-source:20
  for ب in بنود:
    # apl-source:21
    صافي = صافي + ب[0] * ب[1]
  # apl-source:22
  return صافي + صافي * ضريبة / 100
# apl-source:23

# apl-source:24
تأكد_يساوي(إجمالي_الفاتورة([[100, 2], [50, 1]], 14), 285.0, "بندان")
# apl-source:25
تأكد_يساوي(إجمالي_الفاتورة([[10, 3]], 0), 30.0, "بلا ضريبة")
# apl-source:26
تأكد_يساوي(إجمالي_الفاتورة([], 14), 0.0, "فارغة")
# apl-source:27
