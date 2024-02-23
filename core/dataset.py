import datetime
from reflections import whichDay, whichTime

data = [
    (r'(👍)(.*)', ['👍']),
    # (r'(3leh |3lech |3leeech|aleh |a3lech | )'),
    (r'(3aslema|how are|selem|hi|ahla|ehla|hello|hellowers|cha7welek|slm|salut|sbe7)(.*)', ['ahla bik, m3ak fsb-gpt-demo inspiré mel produits mte3 OPENAI ama hedheya demo, chnowa t7eb ta3ref 3la FSB wla 7ata étudionnetha ?']),
    (r'(cv |cha7welek |chnowaa |mrgl |chnowa |chnwa )(7welek|oumourek|jaw)', ['wlhi cv hamdouleh f chnowa najem n3awnek']),
    (r'(.*)(fsb)(.*)', ['t7esek ta7ki 3la fsb, alors heya faculté étatique f jarzouna fiha quelques départements kima INFORMATIQUE, PHYSIQUE, BIOLOGIE ... chnowa t7eb ta3ref e5er, ena memoire mte3i zghira barcha es2elni 3la profetna mte3 IA mathalan wla 3la étudiant meli na3mlou f présentation hedhi?']),
    (r'(.*)(a3tini |ta3refha |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou |mnewa )(dhia)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun dhia, alors dhia howa eli 5dem mini projet hedheya, étudiant f GLSI2 w motivant w maghroun y7eb ya3mel solutions yfidou mojtama3 w yet3alem hajet jdida']),
    (r'(.*)(a3tini |ta3refha |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou |mnewa )(khouloud|kholod|5ouloud|5olod)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun khouloud, alors heya ...']),
    (r'(.*)(a3tini |ta3refha |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou |mnewa )(vouad)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun vouad, alors howa etudiant mauritanien ye9re v l fsb 2 année glsi w ye9re 3le rouhu mchlh']),
    (r'(.*)(a3tini |ta3refha |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou |mnewa )(abdalah|sidi| sidi abdoulah|sidi abdelah|sidi abdolah)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun abdalah, alors howa etudiant mauritanien ye9re v l fsb 2 année glsi w ye9re 3le rouhu mchlh']),
    (r'(.*)(a3tini |ta3refha |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou |mnewa )(abdalah|sidi| sidi abdoulah|sidi abdelah|sidi abdolah)(.*)', ['7asb kelemk t7esek t7eb ta3ref chkoun abdalah, alors howa etudiant mauritanien ye9re v l fsb 2 année glsi w ye9re 3le rouhu mchlh']),
    (r'(.*)(a3tini |ta3refha |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou |mnewa )(chef|chef dép|chef dep|fadi)(.*)', ['fadi kacem', 'fadi kacem howa chef département informatique f faculté des sciences de bizerte']),
    (r'(ta3refha |a3tini |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou |mnewa |chkouni |chkouni |ta3refha )(madame |ms. )(madame |ms. |proft |sourour|sorour|meddeb|medeb)(.*)', ['heya proft intelligence artificielle mte3na, t7esha sa7abet jaw ya3tiha sa7a ...']),
    (r'(.*)(ta3refha |a3tini |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou )(.*)(projet)(.*)', ['eli 3amlou projet houma dhia, vouad, khouloud w abdalah ... ']),
    (r'(.*)(ta3refha |a3tini |ta3rfou |tarfou |ta3ref |taref |tarefha |ta3ref |chkoun |chkounou )(.*)', ['t7eb ta3ref haja ? jareb esm mel esemi hedhom trah :) : dhia, vouad, khouloud, abdalah ... ']),
    (r'(.*)(wa9t|w9t|lw9t|time|heure|se3a|sa3a)(.*)', [f'el wa9t s3ib mais wa9t tawa {whichTime(datetime.datetime.now().strftime("%H:%M:%S"))}']),
    (r'(.*)(day|nhar|yawm|youm)(.*)', [f'lyoum {whichDay(datetime.datetime.now().strftime("%A"))} w fi9li 3aych sa7bi', f'lyoum {whichDay(datetime.datetime.now().strftime("%A"))} nchalah nhar mabrouk 3lina', f'lyoum {whichDay(datetime.datetime.now().strftime("%A"))} ama lezmek ta3ref ayamet jem3a bech matdhi3ech sadi9i ...']),
    (r'(chnowa |ta3ref |ta3refhom |9oli 3la )(lwilayat|wilayat|wila)(.*)', ['bizerte, beja, jendouba, tunis, manouba, ariana, ben arous, nabeul ...', ]),
    (r'.*', ['mafhemtekech, jareb es2elni 3la team mte3 présentation wla 3la FSB en général...']),
    (r'(👍)(.*)', ['👍', 'nakrhou sbo3 maach tbaathou']),
    (r'', [''])
]
