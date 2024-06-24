from Crypto.Util.number import long_to_bytes, inverse
from math import gcd

# Given values
ciphertext = 6679751571680153009963904682331184917652002856700102310232283862142510059360180548700458831963141409609920551415092207709728225180286265998724528164577674542248721526251187945599585717178191437930160757806807093902793807235144537860942319684760999843630442651226130860002909404140653471185313647715181302304167348924688037557405954539411557457882044330160211329312062720746325861916622922820920104281967898138703453429045946889126965213138749635812159404760369795951532507412006588445870437729196704275485530658165559396122865023696853894261433203860671549068300198104293392003636061195320565520679305383883882898704604559634890784729197249080759946890339250163066886325287412173193725229601090022511506412230800802290674678253497769900141951607190755458800862513784646884224494722467907534558045716790058316430899730082488292110364545682645526449625284655084352824888655261021276231604789263073577754238178023201953270541398611484040131436716568377922478723737147991263070279633895970368806063613324760527575876314365886699695723894144649502485701910377316805704678920436308732783312047975198912094727120936436700875408590797953864331729040548975810138259062653692644739165742002068121098949542299582433914931491801296451377581006636483
dp = 171432559101471989605646948356373748103604947361256607378340448850139917017741253759903745507057919262287422186222940360213785420605757333138847887731767022598405608474995330651947849082078370449736651288592860283221797983119927725117149200774804739974975582585523359416946408144385855153221559461347298824391132395892996924625640872166698317735741877365806943143135835009957625457973450121352962604530814817655901697483088999524541499291037003678660130712141021632221794174249924834077632177968501757212722623350575181797794958244328870841294336463187222306714995492272643611646928249482017303542563647469595369211254712548098832095540995311841074627538151877339371487927806145948905672833767915852929856220973560840386125633752412480320584458935038302142751449534187398925662384466751897711549687947862910839873293128396014847384039868091701077519788860107065614981153691686685326821058865631742737041863375989903668129520572806351954019608985002225703602063443485842326068527683024332639834458331067102353325840535706456324422275754723563198715550407175182648240718090477435547945193732546635158601952418224352960525259751828810794856217898929112965219114783525262615310830832190730442349789460621438028345913017708361465523133564202266062786788681281757147027464002581040633319572450555353324321699056478024157129773151732670142844483164508432539498373947180375305585469627835596667356476511772733667404728958877380598398949024045379136292741643874960237432332704625052528856617384339450570121280954511126937150643703664520808218298441310306024377957237049720519185727832578500913286023909348162473989113812550805225552724830261887490591714039944400527976071373184209831845969062119462403725052459177546892619818022391873329229206364783314296446725486658518678734803325482151370648102682365593547647791628684309371655283249776091365996509876023788183283
p2q = 213170963396891562143729893832305593956284174845169799407158675577110705655852548100992539024685605819040523438354858977086250927051314265096682933654811030453120355993278986527591427479217724393594363257765113070515263721083971223242626072880720581419978650145288765887646651182214510751858103451633012485610884049514075314470934936707881750297833515167875716398286561408739074084796622722760821747711526623749451276879787567817851745356924240775796394772442579161577074751879657031608875439664580204201692487743603940603018464632550634822614684162563342914622534096899198261578687727659671151167232592054166999563570889708448262394605837628857811991515889971291433914715772638211960415936759778304390577548067679510456479994850801235456371216662187652015317755739895815495111283612397090640609867328889881660712528196291865436926052849406375373713408563964846026093263911701059393127967976555276551426913678840649401811190075325584784349447556418171890714076070692905482708888254009586154239227598710507703178655793348942676198573019759816326439893896477510901166547609616895842071430538232916809944394150298378345872103063301628330221653850388439443364638019538570767613777320343878189983973545330874737453400095937886979792088374986323520843348511102325586784495504624319448813796476293969903137538257355998338779733642119548481876998281481405692762331628893501531291329441495308243568019180766627407280078643666235573172278294075588442969374279359865601439488703565838942636582392466277488366374194890249687124242483769387553299912110196370951410060473480026800086484176574417759880104620851539589554039438701036794016648069808210636519140497455612086833766213769594997981459162235532307853956081579590271809503536822605626989725511498994042990581546736877584625171747601769972545109503616616296913370130968957785947869343438375248167319517552596218503
e = 65537
# Step 1: Compute p using gcd
p = gcd(dp, p2q)

# Step 2: Derive q from n and p
q = p2q // (p * p)
n = p * q

# Validate the computed q
assert p * q == n, "p and q do not multiply to n"

# Step 3: Compute phi and the private key d
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# Step 4: Decrypt the ciphertext
decrypted_flag = pow(ciphertext, d, n)

# Convert the decrypted flag back to bytes
decrypted_flag_bytes = long_to_bytes(decrypted_flag)

# Print the decrypted flag
print(decrypted_flag_bytes)
