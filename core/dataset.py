import datetime

data = [
    (r'(👍)(.*)', ['👍']),
    (r'(3aslema|how are|selem|hi|ahla|ehla|hello|hellowers|cha7welek|slm|salut)(.*)', ['ahla bik, m3ak fsb-gpt-demo inspiré mel produits mte3 OPENAI ama hedheya demo, chnowa t7eb ta3ref 3la FSB wla 7ata étudionnetha ?']),
    (r'(.*)(fsb)(.*)', ['t7esek ta7ki 3la fsb, alors heya faculté étatique f jarzouna fiha quelques départements kima INFORMATIQUE, PHYSIQUE, BIOLOGIE ... chnowa t7eb ta3ref e5er, ena memoire mte3i zghira barcha es2elni 3la profetna mte3 IA mathalan wla 3la étudiant meli na3mlou f présentation hedhi?']),
    (r'(.*)(chkoun |chkounou |mnewa )(dhia)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun dhia, alors dhia howa eli 5dem mini projet hedheya, étudiant f GLSI2 w motivant w maghroun y7eb ya3mel solutions yfidou mojtama3 w yet3alem hajet jdida']),
    (r'(.*)(chkoun |chkounou |mnewa )(khouloud|kholod|5ouloud|5olod)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun khouloud, alors heya ...']),
    (r'(.*)(chkoun |chkounou |mnewa )(vouad)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun vouad, alors howa etudiant mauritanien ye9re v l fsb 2 année glsi w ye9re 3le rouhu mchlh']),
    (r'(.*)(chkoun |chkounou |mnewa )(abdalah|sidi| sidi abdoulah|sidi abdelah|sidi abdolah)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun abdalah, alors howa etudiant mauritanien ye9re v l fsb 2 année glsi w ye9re 3le rouhu mchlh']),
    (r'(.*)(chkoun |chkounou |mnewa )(abdalah|sidi| sidi abdoulah|sidi abdelah|sidi abdolah)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun abdalah, alors howa etudiant mauritanien ye9re v l fsb 2 année glsi w ye9re 3le rouhu mchlh']),
    (r'(.*)(chkoun |chkounou |mnewa )(chef|chef dép|chef dep|fadi)(.*)', ['fadi kacem', 'fadi kacem howa chef département informatique f faculté des sciences de bizerte']),
    (r'(.*)(chkoun |chkounou |mnewa |chkouni| chkouni)(sourour|sorour|meddeb|medeb)(.*)', ['heya proft intelligence artificielle mte3na, t7esha sa7abet jaw ya3tiha sa7a ...']),
    (r'(.*)(chkoun |chkounou )(.*)(projet)(.*)', ['eli 3amlou projet houma dhia, vouad, khouloud w abdalah ... ']),
    (r'(.*)(chkoun |chkounou )(.*)', ['t7eb ta3ref haja ? jareb esm mel esemi hedhom trah :) : dhia, vouad, khouloud, abdalah ... ']),
    (r'(.*)(wa9t|time|heure|se3a|sa3a)(.*)', [f'el wa9t s3ib mais wa9t tawa: {datetime.datetime.now().strftime("%H:%M:%S")}']),
    (r'(.*)(day|nhar|yawm|youm)(.*)', [f'nhar lyoum bel anglais khw:{datetime.datetime.now().strftime("%A")}']),
    (r'.*', ['mafhemtekech, wla inti ma3titni chy wa7da mel thnin, jareb es2elni 3la team mte3 présentation wla 3la FSB en général...']),
    (r'(👍)(.*)', ['👍', 'nakrhou sbo3 maach tbaathou']),
    (r'', [''])
]