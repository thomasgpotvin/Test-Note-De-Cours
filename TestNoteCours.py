#######     Test pour note de cours   #######

##    Chapitre 2     ###

##    Le module sys    ##


import sys, time, os
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

else : 

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











##### Le module OS #####

### os.getcwd####
print "\n- Repertoire courant:", os.getcwd()


### os.mkdir###
print "\n- Creation d'un dossier 'temp' dans le repertoire courant"
# mkdir retourne une erreur si le dossier existe deja.
os.mkdir("temp")


### os.chdir###
print "\n- Changement de repertoire courant"
os.chdir('temp') 


###  création de fichier  ####
print "\n- Creation de fichiers..."
for i in range(4):
    f = open("tmpfile-%d.txt" % i, "w")
    f.close()

###   os.getcwd   (encore) ##
print "\n- Repertoire courant:", os.getcwd()

print "\n- Liste des fichiers contenus dans le repertoire courant:\n"

###   os.listdir (dans le dossier courant) ###
filelist = os.listdir(os.getcwd())
print filelist

###    os.remove ####
print "\n- Suppresssion des fichiers"
for i in range(4):
    os.remove("tmpfile-%d.txt" % i)
    
#### os.chdir (encore) ###
print "\n- Changement de repertoire courant (retour en arriere d'un niveau)"
os.chdir('..')


### os.rmdir ######
print
print "- Suppression du dossier 'temp'"
# Le dossier doit etre vide!
os.rmdir('temp') 














#### Le module os.path #####


###  os.path.expanduser   ###
userpath = os.path.expanduser("~")

### Creation de paths, par concatenation, avec os.path.join  ###
temppath = os.path.join(userpath, "temp")
tempfile = os.path.join(temppath, "tempfile.txt")

print "\n- Repertoire utilisateur:", userpath

###   os.path.isdir   ####
print "\n- Teste la presence d'un dossier '%s'" % temppath
exist = os.path.isdir(temppath)

if not exist:
    print "\n- Creation du dossier '%s'" % temppath
    os.mkdir(temppath)

####   os.path.isfile   ####    
print "\n- Teste la presence d'un fichier '%s'" % tempfile
exist = os.path.isfile(tempfile)

if not exist:
    print "\n- Creation du fichier '%s'" % tempfile
    f = open(tempfile, "w")
    f.write("* Ceci est le contenu du fichier tempfile.txt! *")
    f.close()
    
print "\n- Lecture du fichier '%s'\n" % tempfile

f = open(tempfile, "r")
print f.read()
f.close()

###   os.path.split separe la base (path du dossier) du nom du fichier   ###
sppath = os.path.split(tempfile)
print "\n- Path de base du fichier:", sppath[0]
print "- Nom du fichier:", sppath[1]

# os.path.splitext separe le path du fichier de l'extension
spext = os.path.splitext(tempfile)
print "\n- Extension du fichier:", spext[1]

print "\n- Suppression du fichier '%s'" % tempfile
os.remove(tempfile)

print "\n- Suppression du dossier '%s'" % temppath
os.rmdir(temppath)





