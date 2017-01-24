#######     Test pour note de cours   #######

##    Chapitre 2     ###

##    Le module sys    ##


import sys, time
from pyo import *



###   sys.platform   ###
platforms = {"darwin" : "OS X", "win32" : "Windows", "linux2" : "linux"}

if platforms.has_key(sys.platform):
    print "\n - Execute sur la platforme %s\n" % platforms[sys.platform]
else:
    print "\n - Execute sur la platforme %s\n" % sys.platform




###   sys.maxint   ####
if sys.maxint > 2**32/2:
    print "- La version courante de python est en 64 bit \n"
else :
    print "- La version courante de python est en 64 bit \n"




####   sys.path  ####
print " - Python reconnait libraries, modules et scripts dans ces dossiers : \n"
print sys.path




####   sys.argv   #### (mettre en arguments 2 chiffres sur le terminal)
args = sys.argv

if len(args) < 2:
    print 
    print "Erreur : nombre d'arguments insuffisants !"
    print "Les frequences des oscillateurs doivent etre donnees en arguments."
    print "Usage :python 02_sys_argv.py freq1 freq2 freq3 ... \n"
    exit()

s = Server(duplex=0).boot()

print "Execution du script %s" % args[0]

del args[0]
num = len(args)
freqs = [float(x) for x in args]

a = Sine(freq=freqs, mul=0.5/num).out()

s.gui(locals())






#####   Autre exemple  #### (enleve le sys.argv pour que ça marche) (mettre en argument un fichier audio à lire et juste avant -l ou -j)
def usage():
    print "\nUsage :"
    print "play [OPTIONS] file1 [file2 [file 3 [...]]]\n"
    print "Options:"
    print " -l : Actives the loop mode."
    print " -j : Uses jack engine instead of portaudio."
    print " -h : Shows this help.\n"
    
if "-h" in sys.argv:
    usage()
    exit()
    
loop = False
if "-l" in sys.argv:
    loop = True
    pos = sys.argv.index("-l")
    del sys.argv[pos]

audio = "pa"
if "-j" in sys.argv:
    audio = "jack"
    pos = sys.argv.index("-j")
    del sys.argv[pos]

if len(sys.argv) < 2:
    print "\nNot enough arguments."
    usage()
    exit()

s = Server(audio=audio).boot()
if not serverBooted():
    exit()
s.start()
if not s.getIsStarted():
    exit()

for snd in sys.argv[1:]:
    try:
        info = sndinfo(snd)
        dur,sr,chnls,format,sample = info[1],info[2],info[3],info[4],info[5]
        sf = SfPlayer(snd, loop=loop, mul=.5).out()
        print "\nFilename           :", snd
        print "Duration           :", dur
        print "Sampling Rate      :", sr
        print "Number of channels :", chnls
        print "File Format        :", format
        print "Sample Type        :", sample, "\n"
        if loop:
            dump = raw_input("Hit Enter to stop playing the sound.")
        else:
            time.sleep(dur+0.25)
        del sf
    except:
        print
        print snd, "must be a WAVE or AIFF file!"
        continue
s.stop()
time.sleep(.2)




