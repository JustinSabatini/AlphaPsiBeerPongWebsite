from django.shortcuts import render
# Create your views here
import pickle
teamdict = pickle.load(open("C:/Users/user/eclipse-workspace/Website/webapp/team.p", "rb"))

def placing(string):
    if string == "1":
        return string+"st"
    elif string == "2":
        return string+"nd"
    elif string == "3":
        return string+"rd"
    else:
        return string+"th"


bbcrank = placing(teamdict[1][7])
bbcgp = teamdict[1][1]
bbcrecord = ("%s-%s-%s" % (teamdict[1][2],teamdict[1][3],teamdict[1][4]))
bbcplusminus = teamdict[1][5]
bbcpoints = teamdict[1][6]

bbrank = placing(teamdict[2][7])
bbgp = teamdict[2][1]
bbrecord = ("%s-%s-%s" % (teamdict[2][2],teamdict[2][3],teamdict[2][4]))
bbplusminus = teamdict[2][5]
bbpoints = teamdict[2][6]

gorank = placing(teamdict[3][7])
gogp = teamdict[3][1]
gorecord = ("%s-%s-%s" % (teamdict[3][2],teamdict[3][3],teamdict[3][4]))
goplusminus = teamdict[3][5]
gopoints = teamdict[3][6]

ksrank = placing(teamdict[4][7])
ksgp = teamdict[4][1]
ksrecord = ("%s-%s-%s" % (teamdict[4][2],teamdict[4][3],teamdict[4][4]))
ksplusminus = teamdict[4][5]
kspoints = teamdict[4][6]

mjrank = placing(teamdict[5][7])
mjgp = teamdict[5][1]
mjrecord = ("%s-%s-%s" % (teamdict[5][2],teamdict[5][3],teamdict[5][4]))
mjplusminus = teamdict[5][5]
mjpoints = teamdict[5][6]

pprank = placing(teamdict[6][7])
ppgp = teamdict[6][1]
pprecord = ("%s-%s-%s" % (teamdict[6][2],teamdict[6][3],teamdict[6][4]))
ppplusminus = teamdict[6][5]
pppoints = teamdict[6][6]

pdrank = placing(teamdict[7][7])
pdgp = teamdict[7][1]
pdrecord = ("%s-%s-%s" % (teamdict[7][2],teamdict[7][3],teamdict[7][4]))
pdplusminus = teamdict[7][5]
pdpoints = teamdict[7][6]

wrrank = placing(teamdict[8][7])
wrgp = teamdict[8][1]
wrrecord = ("%s-%s-%s" % (teamdict[8][2],teamdict[8][3],teamdict[8][4]))
wrplusminus = teamdict[8][5]
wrpoints = teamdict[8][6]



def index(request):
    rowdict = pickle.load(open("C:/Users/user/eclipse-workspace/Website/webapp/save.p", "rb"))
    context= {
        'teamdict': teamdict,
        'rowdict': rowdict,
        }
    return render(request, 'webapp/home.html', context)
def rules(request):
    return render(request, 'webapp/rules.html')

def leaguerules(request):
    return render(request, 'webapp/leaguerules.html')

def games(request):
    return render(request, 'webapp/games.html')
def roster(request):
    rowdict = pickle.load(open("C:/Users/user/eclipse-workspace/Website/webapp/save.p", "rb"))
    context= {
        'bbcrank': bbcrank,
        'bbcgp': bbcgp,
        'bbcrecord': bbcrecord,
        'bbcplusminus': bbcplusminus,
        'bbcpoints': bbcpoints,
        'bbrank': bbrank,
        'bbgp': bbgp,
        'bbrecord': bbrecord,
        'bbplusminus': bbplusminus,
        'bbpoints': bbpoints,
        'gorank': gorank,
        'gogp': gogp,
        'gorecord': gorecord,
        'goplusminus': goplusminus,
        'gopoints': gopoints,
        'ksrank': ksrank,
        'ksgp': ksgp,
        'ksrecord': ksrecord,
        'ksplusminus': ksplusminus,
        'kspoints': kspoints,
        'mjrank': mjrank,
        'mjgp': mjgp,
        'mjrecord': mjrecord,
        'mjplusminus': mjplusminus,
        'mjpoints': mjpoints,
        'pprank': pprank,
        'ppgp': ppgp,
        'pprecord': pprecord,
        'ppplusminus': ppplusminus,
        'pppoints': pppoints,
        'pdrank': pdrank,
        'pdgp': pdgp,
        'pdrecord': pdrecord,
        'pdplusminus': pdplusminus,
        'pdpoints': pdpoints,
        'wrrank': wrrank,
        'wrgp': wrgp,
        'wrrecord': wrrecord,
        'wrplusminus': wrplusminus,
        'wrpoints': wrpoints,
        'teamdict': teamdict,
        'rowdict': rowdict,
        }
    return render(request, 'webapp/roster.html', context)
def teamstandings(request):
    rowdict = pickle.load(open("C:/Users/user/eclipse-workspace/Website/webapp/save.p", "rb"))
    context= {
        'bbcrank': bbcrank,
        'bbcgp': bbcgp,
        'bbcrecord': bbcrecord,
        'bbcplusminus': bbcplusminus,
        'bbcpoints': bbcpoints,
        'bbrank': bbrank,
        'bbgp': bbgp,
        'bbrecord': bbrecord,
        'bbplusminus': bbplusminus,
        'bbpoints': bbpoints,
        'gorank': gorank,
        'gogp': gogp,
        'gorecord': gorecord,
        'goplusminus': goplusminus,
        'gopoints': gopoints,
        'ksrank': ksrank,
        'ksgp': ksgp,
        'ksrecord': ksrecord,
        'ksplusminus': ksplusminus,
        'kspoints': kspoints,
        'mjrank': mjrank,
        'mjgp': mjgp,
        'mjrecord': mjrecord,
        'mjplusminus': mjplusminus,
        'mjpoints': mjpoints,
        'pprank': pprank,
        'ppgp': ppgp,
        'pprecord': pprecord,
        'ppplusminus': ppplusminus,
        'pppoints': pppoints,
        'pdrank': pdrank,
        'pdgp': pdgp,
        'pdrecord': pdrecord,
        'pdplusminus': pdplusminus,
        'pdpoints': pdpoints,
        'wrrank': wrrank,
        'wrgp': wrgp,
        'wrrecord': wrrecord,
        'wrplusminus': wrplusminus,
        'wrpoints': wrpoints,
        'teamdict': teamdict,
        'rowdict': rowdict,
        }
    return render(request, 'webapp/teamstandings.html', context)
def playerstats(request):
    rowdict = pickle.load(open("C:/Users/user/eclipse-workspace/Website/webapp/save.p", "rb"))
    context= {
        'teamdict': teamdict,
        'rowdict': rowdict,
        }
    return render(request, 'webapp/playerstats.html', context)

