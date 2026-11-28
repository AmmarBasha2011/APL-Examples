
# apl-source:1
# مثال 1175 — وسيط متدفق
# apl-source:2
# Running median of a stream
# apl-source:3
# Demonstrates: إدراج مرتب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1175-running-median-stream.apl
# apl-source:6

# apl-source:7
# ندرج كل رقم في مكانه بقائمة مرتبة
# apl-source:8
# ونقرأ الوسيط بعد كل إدراج
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
class وسيط_متدفق:
  # apl-source:19
  def __init__(ذات):
    # apl-source:20
    ذات.مرتبة = []
# apl-source:21

  # apl-source:22
  def اضف(ذات, س):
    # apl-source:23
    ع = 0
    # apl-source:24
    while (ع < len(ذات.مرتبة)) and (ذات.مرتبة[ع] < س):
      # apl-source:25
      ع = ع + 1
    # apl-source:26
    ذات.مرتبة.insert(ع, س)
# apl-source:27

  # apl-source:28
  def الوسيط(ذات):
    # apl-source:29
    ن = len(ذات.مرتبة)
    # apl-source:30
    if ن % 2 == 1:
      # apl-source:31
      return ذات.مرتبة[ن // 2] * 1.0
    # apl-source:32
    return (ذات.مرتبة[ن // 2 - 1] + ذات.مرتبة[ن // 2]) / 2
# apl-source:33

# apl-source:34
م = وسيط_متدفق()
# apl-source:35
نتائج = []
# apl-source:36
for س in [5, 15, 1, 3]:
  # apl-source:37
  م.اضف(س)
  # apl-source:38
  نتائج = نتائج + [م.الوسيط()]
# apl-source:39
تأكد_يساوي(نتائج, [5.0, 10.0, 5.0, 4.0], "تدفق")
# apl-source:40
