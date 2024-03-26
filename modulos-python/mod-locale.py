# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

# Seta locale de acordo com sistema operacional
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(locale.getlocale())
print(calendar.calendar(2024))
