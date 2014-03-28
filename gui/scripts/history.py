def create_history():
    years = [2013,'Charlie','Phil','Sean','Chris','Madelyn','Chuck','Mike','Jake','Tom','Tim','Peter','Tony'],\
            [2012,'Jake','Tony','Madelyn','Tom','Peter','Mike','Tim','Charlie','Phil','Sean','Chris','Chuck']


    place = ['Champion','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th']

    all_tables = ""
    for year in years:
        count = 0
        year_table = ""
        for team in year:
            if team == year[0]:
                year_table += "\n<h1>%s</h1><table border=\"1\" cellpadding=\"20\">" % team
            else:
                if count == 0:
                    year_table += "\n<tr><td><b>%s</b></td><td><b>%s</b></td></tr>" % (place[count],team)
                else:
                    year_table += "\n<tr><td>%s</td><td>%s</td></tr>" % (place[count],team)
                count +=1
        year_table += "</table>"
        all_tables += year_table

    return all_tables


