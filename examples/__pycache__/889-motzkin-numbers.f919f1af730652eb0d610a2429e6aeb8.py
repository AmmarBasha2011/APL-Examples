
# apl-source:1
# مثال 889 — أعداد موتزكين
# apl-source:2
# Motzkin numbers
# apl-source:3
# Demonstrates: مسارات بثلاث خطوات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/889-motzkin-numbers.apl
# apl-source:6

# apl-source:7
# أعداد موتزكين: عدد مسارات الشبكة بخطوات صعود/هبوط/استواء دون النزول تحت الصفر
# apl-source:8
# M(n) = M(n-1) + مجموع M(k)*M(n-2-k)
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
def موتزكين(ن):
  # apl-source:19
  م = []
  # apl-source:20
  for _ in range(ن + 1):
    # apl-source:21
    م = م + [1]
  # apl-source:22
  for i in range(2, ن + 1):
    # apl-source:23
    مجموع = م[i - 1]
    # apl-source:24
    for ك in range(i - 1):
      # apl-source:25
      مجموع = مجموع + م[ك] * م[i - 2 - ك]
    # apl-source:26
    م[i] = مجموع
  # apl-source:27
  return م
# apl-source:28

# apl-source:29
م = موتزكين(8)
# apl-source:30
print("M0..M8:", م)
# apl-source:31

# apl-source:32
تأكد_يساوي(م[0], 1, "M0 = 1")
# apl-source:33
تأكد_يساوي(م[2], 2, "M2 = 2")
# apl-source:34
تأكد_يساوي(م[4], 9, "M4 = 9")
# apl-source:35
تأكد_يساوي(م[6], 51, "M6 = 51")
# apl-source:36
تأكد_يساوي(م[8], 323, "M8 = 323")
# apl-source:37
