
# apl-source:1
# مثال 1518 — غرامة التأخير بالأيام
# apl-source:2
# Late fee by days
# apl-source:3
# Demonstrates: مالية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1518-late-fee-days.apl
# apl-source:6

# apl-source:7
# لا غرامة داخل فترة السماح
# apl-source:8
# الغرامة لا تتجاوز سقفاً
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
def الغرامة(أيام_تأخير, سماح, يومية, سقف):
  # apl-source:19
  if أيام_تأخير <= سماح:
    # apl-source:20
    return 0
  # apl-source:21
  غرامة = (أيام_تأخير - سماح) * يومية
  # apl-source:22
  if غرامة > سقف:
    # apl-source:23
    return سقف
  # apl-source:24
  return غرامة
# apl-source:25

# apl-source:26
تأكد_يساوي(الغرامة(2, 3, 5, 50), 0, "في السماح")
# apl-source:27
تأكد_يساوي(الغرامة(6, 3, 5, 50), 15, "ثلاثة أيام")
# apl-source:28
تأكد_يساوي(الغرامة(100, 3, 5, 50), 50, "السقف")
# apl-source:29
