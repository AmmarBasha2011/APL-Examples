
# apl-source:1
# مثال 1422 — متتاليات دنا مكررة
# apl-source:2
# Repeated DNA sequences
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1422-repeated-dna-sequences.apl
# apl-source:6

# apl-source:7
# نعد كل نافذة بطول عشرة
# apl-source:8
# نعيد ما تكرر مرتباً
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
def دنا_مكرر(دنا):
  # apl-source:19
  عدّ = {}
  # apl-source:20
  for ع in range(len(دنا) - 9):
    # apl-source:21
    مقطع = دنا[ع:ع + 10]
    # apl-source:22
    عدّ[مقطع] = عدّ.get(مقطع, 0) + 1
  # apl-source:23
  ناتج = []
  # apl-source:24
  for م in عدّ:
    # apl-source:25
    if عدّ[م] > 1:
      # apl-source:26
      ناتج = ناتج + [م]
  # apl-source:27
  return sorted(ناتج)
# apl-source:28

# apl-source:29
تأكد_يساوي(دنا_مكرر("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC","CCCCCAAAAA"], "مقطعان")
# apl-source:30
تأكد_يساوي(دنا_مكرر("AAAAAAAAAAAAA"), ["AAAAAAAAAA"], "مقطع واحد")
# apl-source:31
تأكد_يساوي(دنا_مكرر("ACGT"), [], "قصير")
# apl-source:32
