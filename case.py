"""Case-study #4 Парсинг web-страниц
Разработчики:
Shmatov D., Bayanova A.

"""
import urllib.request

with open('input.txt') as f_in:
    with open('output.txt', 'w') as f_out:
        for line in f_in:
            url = line
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
            Rating = ((Comp / Att - 0.3)*5 + (Yds / Att - 3) * 0.25 + (Td / Att)*20 + 2.375 - (Int / Att * 25))/6 * 100

            print("{:^20}".format(name), "{:^7}".format(Comp), "{:^7}".format(Att), "{:^7}".format(Yds),
                  "{:^7}".format(Td), "{:^7}".format(Int), "{:^7.2f}".format(Rating), file=f_out, end="\n")
