
# apl-source:1
# مثال 1467 — جدول ترتيب الدوري
# apl-source:2
# League points table
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1467-league-points-table.apl
# apl-source:6

# apl-source:7
# نقرأ النتائج مباراة بمباراة
# apl-source:8
# ثم نرتب بالنقاط
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
def جدول(مباريات):
  # apl-source:19
  نقاط = {}
  # apl-source:20
  for م in مباريات:
    # apl-source:21
    أ = م[0]
    # apl-source:22
    ب = م[1]
    # apl-source:23
    نقاط[أ] = نقاط.get(أ, 0)
    # apl-source:24
    نقاط[ب] = نقاط.get(ب, 0)
    # apl-source:25
    if م[2] > م[3]:
      # apl-source:26
      نقاط[أ] = نقاط[أ] + 3
    # apl-source:27
    elif م[2] < م[3]:
      # apl-source:28
      نقاط[ب] = نقاط[ب] + 3
    # apl-source:29
    else:
      # apl-source:30
      نقاط[أ] = نقاط[أ] + 1
      # apl-source:31
      نقاط[ب] = نقاط[ب] + 1
  # apl-source:32
  return نقاط
# apl-source:33

# apl-source:34
ن = جدول([["أ", "ب", 2, 1], ["ب", "ج", 0, 0], ["ج", "أ", 1, 3]])
# apl-source:35
تأكد_يساوي(ن["أ"], 6, "الفائز مرتين")
# apl-source:36
تأكد_يساوي(ن["ب"], 1, "تعادل")
# apl-source:37
تأكد_يساوي(ن["ج"], 1, "تعادل ثانٍ")
# apl-source:38
