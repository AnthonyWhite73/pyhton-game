import random, time, sys
from typing import ClassVar

#art variables
art_bodybuilder1 = ".......``.......``......++.......``......``.......\n........`......```...-+mMMd+-....``......``.......\n........`......```..+dMMMMNNd/...``......``.......\n``.....`````````````/dMMMMMMh/`````````````....```\n......`````````````://+dMMh/://:````````.....`````\n.......``.......`:yNMy.-//..yMMNh:`...............\n.......```.....-sNMMNs..``..yNMMMN-......``.......\n.....``````..-omMMMdyo/.```.-+dMMMmo-```.``.`````.\n````````````-sMMMd/.sMNh```yds:+dMMMmo-```````````\n..oyyo.```-odMMm+...yMMNy`yNMMy..+mmNMmo.``syy/...\n..hMMh.``+dNMmo-``..yMMMM`NMMMh..`--odNm+``NMMs...\n..hMMh../Ndds-..``..yMMMM`NNNMy..``..-omN:`NMMs...\n``hMMmssmmysssssssssdMMMMsNMNMmssssssssymmsNMNs```\n..hMMh..`.......``..yMMMM.NMMMh..``......`.NMMs.`.\n..hMMh.```.....```..yMMMM`NMMMh..``........NMMs...\n..hMMh.``.......``..omMNm`/mMNs..``........NMMs...\n.`/oo/```````````````:o+```+o:`````````````+oo:```"
art_bodybuilder2 = "     `+++`                      :hhh.\n     -MMM:                   `` oMMMo`\n `++sdMMMh:hh-------:::-----:dm:yMMMdo//`\n    ``NMMo `sms-   /NNd   /hmo` +MMM:\n      /++-   `/hms/+MMm/smm:     ...\n                /hMMMMMMN+`\n                 `mMMMMMy\n                  sMMMMN.\n                  /MMMMm\n                  yMMMMm\n                `yMMMMMMy`\n                sMMm/-mMMd`\n                hN+    +NM:\n               .Mh      -Nh\n               `N+       dh\n               `m/       sd.\n               +h+       :os`"
art_bodybuilder3 = "````.-.```````/mNm+```` ````````````````\n ```+dNN+````-NMMMh`````````````-odm+````\n ..+hMMNd-`.-:dNNdN+:.````-.```.yNMMM/```\n .-yhMNmd/:yhhmmNmmNmMNy/yhds::shMMhhs:/-\n ``/hMMMy``/NNMMNMMMMMMN/.mm+``/hMMMM/```\n ```:oy+```+NNMMNMMMMNNMNhMM:```sdNNs````\n ``````````:NMNNhhhhmNNNNMMd`````--.`````\n ```````````:o+.+hdddymdmms-`````````` ``\n ````````````+oydydyyhydy-```````````` ``\n ``````````+mNdmddddMNdNd/```````````````\n `````````:NhNhy/hMdmdhyo```` ```` ``````\n ``````````.ymNN:.sdNNs.`````````````````\n ````````````+ymd``ohNMs`````````````` ``\n `````````````.dMs```+NN-````````````` ``\n ````````````/hdMh+``+mMh.``` ```````````\n ``````````.+hhs-``.yMhN+````````````````\n ``````````````````oydho` ``````` ```` ``"
art_thief1 = ".......``......``////``........``......\n........`..../hmmddmmmdy-......``......\n........`....`hmdmdhhhddm......``......\n``......`````-Ndmhshyohsd:```````......\n.....````````.ddmy/-:/::h````````....``\n```````````` -+dmdm/--:oy.`````....````\n``-.```````.Nmmmmmdhhmmmh:``````````:h`\n``oo/`````:hyyyddddhhdhhhss:```````+/s`\n``-o:o````/hyyyddhhyhhddNhhyys+---:o//-\n````./ohshyshdmdhyydhhhmmo.ohyysymmds``\n`````mddmymdmdmdmhhhhmmdm```::ooss/````\n``...`---.mdmmMNmhohNmddo```.......````\n```....``sdmdNhyhhyysymh`....``````....\n```....`.hmddmyysyyyyshh``....``````...\n`````...sdddmysyymmdyyyhs````..````..``\n``````..dddNdhyymmddmhyydo.``````......\n`````````-/dhhhm+/oo/ddhhhh```..```````\n```....```.hddm+`````-yddd:`````....```\n````.-::/sdhhds//////:+dhhhy`...```````\n```````.......------..``````..........."
art_thief2 = ""
art_thief3 = ""
art_prof1 = "`````.-:-:--o///``````````````\n ``.-:/+//-.-/o::::````````````\n `-/-:/+oo::s-o/--:/-....`.....\n :/:::/so/o/++os:/://...`......\n `:+//+o+++-/+/s+/-`.....`.....\n `````o+-+/:/o-/+```````.``.```\n `````//.:ysh/../```````.-`````\n ``````/-+yoso:-:``````....````\n ```````:-///:./```````/.:-````\n ````````:::///.```````:./`````\n ````````:s:::++.`````//-/--```\n ```````+:s-o:/+//`.../:+s+o.``\n `````.:+o++sy/oo/:::`o:ooo/::.\n ````/:::o/+ohs+++::o:s/s//````\n ````/:::/+/yys://:/+s/+y+-````\n ````++::::+sy:/+::oo+::/.`````\n ```/:+/::::+y/+::::o/:+```````\n ``-/:++::::/o+:::::/+:.```````\n ```.:+:::::+o/::::::+`````````\n `````/:::::o//::::::/:````````\n `````+:::::+++:::::::+````````\n `````+::::::o::::::::::```````\n `````-://:::o::::::::/:```````\n ````````.+hyyhysssss-`````````\n ````./+shddhyhssyhddh+/-``````\n ```+sooss+/++++oo/yyyhhdds-```"
art_prof2 = ""
art_prof3 = ""
#art lists
art_bodybuilders = [
    art_bodybuilder1,art_bodybuilder2,art_bodybuilder3
]
art_thieves = [
    art_thief1,art_thief2,art_thief3
]
art_profs = [
    art_prof1,art_prof2,art_prof3
]
#functions to call single art pieces
def func_art_bodybuilder1():
    print(art_bodybuilder1)
def func_art_bodybuilder2():
    print(art_bodybuilder2)
def func_art_bodybuilder3():
    print(art_bodybuilder3)
def func_art_thief1():
    print(art_thief1)
def func_art_thief2():
    print(art_thief2)
def func_art_thief3():
    print(art_thief3)
def func_art_prof1():
    print(art_prof1)
def func_art_prof2():
    print(art_prof2)
def func_art_prof3():
    print(art_prof3)
#function for random art in list
def rand_art_bodybuilders():
    print(art_bodybuilders[random.randint(0,2)])
def rand_art_thieves():
    print(art_thieves[random.randint(0,2)])
def rand_art_profs():
    print(art_profs[random.randint(0,2)])
#test vvv call 1 art pieces from the bodybuilders art list vvv
rand_art_bodybuilders()
#test call thief art and prof art
func_art_thief1()
func_art_prof1()
