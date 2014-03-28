def create_team_table():
    teams = [('Charlie',9), ('Chris',2), ('Chuck',8), ('Jake',10), ('Madelyn',4),('Mike',12), ('Peter',3), ('Phil',1), ('Sean',5), ('Tim',13), ('Tom',7), ('Tony',6)]

    team_table = "<table border =\"1\" cellpadding=\"20\">"
    for team in teams:
        team_table += " <tr>" \
                      "\n       <td>%s</td>" % team[0]
        for year in ['Current','2012','2013']:
            if year == "Current":
                team_table += '\n       <td><a href="http://fantasy.nfl.com/league/744960/team/%d">%s</a></td>' % (team[1],year)
            else:
                team_table += '\n       <td><a href="http://fantasy.nfl.com/league/744960/history/%s/teamhome?teamId=%d">%s</a></td>' % (year,team[1],year)
        team_table += "</tr>"

    return team_table

