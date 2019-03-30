import pickle
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/user/eclipse-workspace/Website/webapp/AlphaPsiPlayerData-f8561cb78a9c.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('APBPL Statistics').sheet1
wks2 = gc.open('TeamStats').sheet1
rowdict = {}
teamdict = {}
i = 1
while i < 25: 
    rowdict[i] = wks.row_values(i+1)
    i += 1
for key, values in rowdict.items():
    for n, i in enumerate(values):
        if i == '#DIV/0!':
            values[n]="n/a"
for x, y in rowdict.items():
    print(x, y)
print(wks2.get_all_values())
teamdict = wks2.get_all_values()
pickle.dump(teamdict, open( "team.p", "wb" ))
pickle.dump(rowdict, open( "save.p", "wb" ))

bbcrank = teamdict[1][7]
bbcgp = teamdict[1][1]
bbcrecord = ("%s-%s-%s" % (teamdict[1][2],teamdict[1][3],teamdict[1][4]))
bbcplusminus = teamdict[1][5]
bbcpoints = teamdict[1][6]

bbrank = teamdict[2][7]
bbgp = teamdict[2][1]
bbrecord = ("%s-%s-%s" % (teamdict[2][2],teamdict[2][3],teamdict[2][4]))
bbplusminus = teamdict[2][5]
bbpoints = teamdict[2][6]

gorank = teamdict[3][7]
gogp = teamdict[3][1]
gorecord = ("%s-%s-%s" % (teamdict[3][2],teamdict[3][3],teamdict[3][4]))
goplusminus = teamdict[3][5]
gopoints = teamdict[3][6]

ksrank = teamdict[4][7]
ksgp = teamdict[4][1]
ksrecord = ("%s-%s-%s" % (teamdict[4][2],teamdict[4][3],teamdict[4][4]))
ksplusminus = teamdict[4][5]
kspoints = teamdict[4][6]

mjrank = teamdict[5][7]
mjgp = teamdict[5][1]
mjrecord = ("%s-%s-%s" % (teamdict[5][2],teamdict[5][3],teamdict[5][4]))
mjplusminus = teamdict[5][5]
mjpoints = teamdict[5][6]

pprank = teamdict[6][7]
ppgp = teamdict[6][1]
pprecord = ("%s-%s-%s" % (teamdict[6][2],teamdict[6][3],teamdict[6][4]))
ppplusminus = teamdict[6][5]
pppoints = teamdict[6][6]

pdrank = teamdict[7][7]
pdgp = teamdict[7][1]
pdrecord = ("%s-%s-%s" % (teamdict[7][2],teamdict[7][3],teamdict[7][4]))
pdplusminus = teamdict[7][5]
pdpoints = teamdict[7][6]

wrrank = teamdict[8][7]
wrgp = teamdict[8][1]
wrrecord = ("%s-%s-%s" % (teamdict[8][2],teamdict[8][3],teamdict[8][4]))
wrplusminus = teamdict[8][5]
wrpoints = teamdict[8][6]
