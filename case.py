"""Case-study #4 Парсинг web-страниц
Разработчики:
Shmatov D., Bayanova A.

"""
import urllib.request

url = 'http://www.nfl.com/player/jimmygaroppolo/2543801/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
text = text.replace(",", "")
part_name = text.find("player-name")
name = text[text.find('>', part_name)+1:text.find('&', part_name)]
rate = text.find("player-totals") + 50
Comp = int(text[text.find("<td>", rate)+4:text.find("</td>", rate)])
Att = int(text[text.find("<td>", rate+50)+4:text.find("</td>", rate+50)])
Yds = int(text[text.find("<td>", rate+150)+4:text.find("</td>", rate+150)])
Td = int(text[text.find("<td>", rate+250)+4:text.find("</td>", rate+250)])
Int = int((text[text.find("<td>", rate+300)+4:text.find("</td>", rate+300)]))
Rating = ((Comp / Att - 0.3)*5 + (Yds/Att - 3) * 0.25 +(Td/Att)*20 + 2.375 - (Int/Att * 25))/6 * 100

print(Yds)
print(Att)
print(Comp)
print(Td)
print(Int)
print(Rating)

print(name)
