from tkinter import *
import random
from tkinter.ttk import *
import sqlite3

timeCount = 0

bbdd = sqlite3.connect("registro.db")
cursor = bbdd.cursor()

cursor.execute("""
			CREATE TABLE if not exists registro ( 
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			speed INTEGER NOT NULL,
			perc INTEGER NOT NULL,
			right INTEGER NOT NULL, 
			wrong INTEGER NOT NULL
			)
	""")

def getMax() :
	try :
		a = cursor.execute("SELECT * FROM registro").fetchall()
		s = a[0][1]
		ac = a[0][2]
		rig = a[0][3]
		wro = a[0][4]
		id = a[0][0]
	except : return []

	return s, ac, rig, wro, id

GeneralCount = 0
t = 0
c = 0
rightwords = 0
wrongwords = 0
tf = False

engwords = ['the', 'be', 'of', 'and', 'a', 'to', 'in', 'he', 'have', 'it', 'that', 'for', 'they', 'I', 'with', 'as', 'not', 'on', 'she', 'at', 'by', 'this', 'we', 
			'you', 'do', 'but', 'from', 'or', 'which', 'one', 'would', 'all', 'will', 'there', 'say', 'who', 'make', 'when', 'can', 'more', 'if', 'no', 'man', 'out', 'other', 
			'so', 'what', 'time', 'up', 'go', 'about', 'than', 'into', 'could', 'state', 'only', 'new', 'year', 'some', 'take', 'come', 'these', 'know', 'see', 'use', 'get', 
			'like', 'then', 'first', 'any', 'work', 'now', 'may', 'such', 'give', 'over', 'think', 'most', 'even', 'find', 'day', 'also', 'after', 'way', 'many', 'must', 
			'look', 'before', 'great', 'back', 'through', 'long', 'where', 'much', 'should', 'well', 'people', 'down', 'own', 'just', 'because', 'good', 'each', 'those', 
			'feel', 'seem', 'how', 'high', 'too', 'place', 'little', 'world', 'very', 'still', 'nation', 'hand', 'old', 'life', 'tell', 'write', 'become', 'here', 'show', 
			'house', 'both', 'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right', 'move', 'thing', 'general', 'school', 'never', 'same', 'another', 
			'begin', 'while', 'number', 'part', 'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'off', 'child', 'few', 'small', 'since', 'against', 'ask', 'late', 
			'home', 'interest', 'large', 'person', 'end', 'open', 'public', 'follow', 'during', 'present', 'without', 'again', 'hold', 'govern', 'around', 'possible', 'head', 
			'consider', 'word', 'program', 'problem', 'however', 'lead', 'system', 'set', 'order', 'eye', 'plan', 'run', 'keep', 'face', 'fact', 'group', 'play', 'stand', 'increase', 
			'early', 'course', 'change', 'help', 'line']

spawords = ['de', 'Y', 'el', 'la', 'en', 'a', 'que', 'los', 'se', 'que', 'un', 'las', 'con', 'no', 'por', 'una', 'para', 'su', 'es', 'como', 'me', 'más', 'le', 'lo', 'o', 'pero',
			'sus', 'si', 'este', 'sobre', 'entre', 'cuando', 'también', 'todo', 'era', 'fue', 'esta', 'ya', 'son', 'mi', 'sin', 'la', 'años', 'ser', 'nos', 'te', 'qué', 'dos', 'está', 'muy', 
			'desde', 'porque', 'yo', 'hasta', 'había', 'hay', 'tiene', 'ese', 'todos', 'hacer', 'donde', 'eso', 'puede', 'parte', 'vida', 'uno', 'esa', 'tiempo', 'él', 'ella', 'sólo', 'dijo',
			'cadavez', 'ni', 'otro', 'después', 'otros', 'mismo', 'hace', 'ahora', 'les', 'estaba', 'así', 'bien', 'e', 'día', 'año', 'aunque', 'durante', 'país', 'siempre', 'otra', 'tres',
			'algo', 'ver', 'mundo', 'los', 'tan', 'antes', 'sí', 'cómo', 'casa', 'nada', 'trabajo', 'estos', 'momento', 'quien', 'están', 'gran', 'esto', 'forma', 'mayor', 'personas', 'ellos',
			'nacional', 'gobierno', 'sino', 'primera', 'unos', 'hacia', 'tenía', 'entonces', 'hoy', 'lugar', 'ante', 'luego', 'estado', 'otras', 'días', 'tener', 'pues', 'va', 'contra', 'nunca',
			'casi', 'tienen', 'según', 'algunos', 'una', 'manera', 'nuevo', 'además', 'hombre', 'millones', 'dar', 'mucho', 'veces', 'menos', 'todas', 'primer', 'presidente', 'decir', 'mujer',
			'tu', 'solo', 'mientras', 'cosas', 'mí', 'debe', 'tanto', 'aquí', 'estas', 'ciudad', 'fueron', 'historia', 'más', 'sin', 'embargo', 'toda', 'tras', 'pueden', 'dice', 'tipo', 'las', 
			'grupo', 'cual', 'social', 'gente', 'sistema', 'desarrollo', 'mejor', 'noche', 'misma', 'estar', 'lado', 'muchos', 'sea', 'cuenta', 'mujeres', 'agua', 'importante', 'aún', 'dentro',
			'cuatro', 'información', 'mis', 'madre', 'salud', 'nuestro', 'será']

italwords = ['non', 'che', 'di', 'e', 'la', 'il', 'un', 'a', 'è', 'per', 'in', 'una', 'sono', 'mi', 'ho', 'si', 'lo', 'ma', 'ti', 'ha', 'le', 'cosa', 'con', 'i', 'no', 'da', 'se', 
			'come', 'io', 'ci', 'questo', 'qui', 'hai', 'bene', 'sei', 'tu', 'del', 'me', 'mio', 'al', 'solo', 'sì', 'tutto', 'te', 'più', 'della', 'era', 'c', 'lei', 'gli', 'mia', 'questa', 
			'ne', 'fare', 'quando', 'essere', 'fatto', 'perché', 'so', 'ora', 'o', 'va', 'mai', 'chi', 'detto', 'così', 'alla', 'quello', 'tutti', 'oh', 'anche', 'molto', 'dei', 'lui', 'voglio',
			'niente', 'stato', 'grazie', 'dove', 'abbiamo', 'tuo', 'nel', 'allora', 'sta', 'posso', 'siamo', 'uno', 'vuoi', 'hanno', 'noi', 'prima', 'suo', 'stai', 'tua', 'due', 'ancora', 'casa',
			'fa', 'sua', 'qualcosa', 'vero', 'su', 'sai', 'sia', 'sempre', 'dire', 'loro', 'quella', 'andiamo', 'andare', 'delle', 'vi', 'quel', 'ehi', 'devo', 'signore', 'nella', 'ad', 'tempo', 
			'certo', 'voi', 'vita', 'forse', 'adesso', 'fuori', 'li', 'davvero', 'sto', 'anni', 'poi', 'altro', 'dio', 'via', 'visto', 'proprio', 'parte', 'ok', 'beh', 'puoi', 'credo', 'sul', 
			'ciao', 'volta', 'cose', 'quanto', 'uomo', 'nessuno', 'padre', 'dopo', 'amico', 'fai', 'può', 'vuole', 'posto', 'lavoro', 'qualcuno', 'già', 'meglio', 'devi', 'ed', 'giorno', 'vedere',
			'cazzo', 'dai', 'cui', 'cos', 'dal', 'vai', 'bisogno', 'ogni', 'vieni', 'ecco', 'senza', 'ce', 'male', 'stata', 'troppo', 'signor', 'qualche', 'mamma', 'perchè', 'tanto', 'dobbiamo',
			'avete', 'dalla', 'sarà', 'prego', 'modo', 'grande', 'tra', 'll', 'miei', 'guarda', 'favore', 'alle', 'quindi', 'sembra', 'sa', 'soldi', 'parlare']

germwords = ['abbiege', 'änder', 'antworte', 'arbeite', 'backe', 'baue', 'bedeute', 'befehle', 'beginne', 'bekomme', 'berge', 'berichte', 'beschäftige', 'bestätige', 'bestehe', 
			'beteilige', 'betone', 'bewege', 'biete', 'binde', 'bitte', 'bleibe', 'brauche', 'brenne', 'bringe', 'denke', 'diskutiere', 'drücke', 'dürfe', 'empfehle', 'entscheide', 'entstehe', 
			'entwickel', 'erhalte', 'erinner', 'erkenne', 'erkläre', 'erreiche', 'erscheine', 'erschrecke', 'erwarte', 'erzähle', 'esse', 'fahre', 'falle', 'fange', 'finde', 'fliege', 'forder',
			'frage', 'führe', 'friere', 'gebäre', 'gebe', 'gehe', 'gehöre', 'gelte', 'genieße', 'gewinne', 'gieße', 'glaube', 'gleiche', 'grabe', 'greife', 'habe', 'halte', 'handel', 'hänge', 
			'hebe', 'heiße', 'helfe', 'hoffe', 'höre', 'kaufe', 'kenne', 'koche', 'komme', 'könne', 'lache', 'lasse', 'laufe', 'lebe', 'lege', 'leihe', 'lerne', 'lese', 'liege', 'lüge', 'mache',
			'meine', 'möge', 'müsse', 'nehme', 'nenne', 'öffne', 'pfeife', 'plane', 'rate', 'rechne', 'rede', 'reise', 'reite', 'renne', 'rieche', 'ringe', 'rufe', 'sage', 'sammel', 'schaffe', 
			'scheine', 'schiebe', 'schieße', 'schlafe', 'schließe', 'schmelze', 'schneide', 'schreibe', 'schreie', 'schweige', 'schwimme', 'sehe', 'sei', 'sende', 'singe', 'sitze', 'solle',
			'spiele', 'springe', 'steche', 'stehe', 'stehle', 'steige', 'stelle', 'sterbe', 'streiche', 'streite', 'studiere', 'suche', 'tanze', 'teile', 'trage', 'treffe', 'trete', 'trinke',
			'tu', 'übe', 'übernehme', 'unterhalte', 'vergesse', 'verhinder', 'verkaufe', 'verlasse', 'verletze', 'verliere', 'versuche', 'verwende', 'verzeihe', 'wachse', 'wähle', 'wasche', 
			'weine', 'werbe', 'werfe', 'wisse', 'wolle', 'zeige', 'ziehe']

frenwords = ['être', 'avoir', 'faire', 'dire', 'pouvoir', 'aller', 'voir', 'vouloir', 'venir', 'devoir', 'prendre', 'trouver', 'donner', 'falloir', 'parler', 'mettre', 'savoir', 
			'passer', 'regarder', 'aimer', 'croire', 'demander', 'rester', 'répondre', 'entendre', 'tout', 'grand', 'petit', 'même', 'autre', 'seul', 'jeune', 'premier', 'bon', 'quel', 
			'beau', 'vieux', 'noir', 'nouveau', 'dernier', 'blanc', 'cher', 'long', 'pauvre', 'plein', 'vrai', 'toute', 'bas', 'gros', 'doux', 'bleu', 'rouge', 'jaune', 'vert', 'rose', 
			'marron', 'orange', 'violet', 'gris', 'ne', 'pas', 'plus', 'bien', 'si', 'là', 'même', 'tout', 'encore', 'aussi', 'peu', 'alors', 'toujours', 'jamais', 'non', 'très', 'ainsi', 
			'moins', 'ici', 'oui', 'trop', 'déjà', 'tant', 'enfin', 'maintenant', 'et', 'que', 'comme', 'mais', 'ou', 'quand', 'si', 'puis', 'donc', 'car', 'ni', 'parce', 'pourquoi', 'lorsque', 
			'tandis', 'puiue', 'comment', 'soit', 'or', 'le', 'un', 'son', 'ce', 'du', 'au', 'de', 'mon', 'leur', 'notre', 'votre', 'quelque', 'ton', 'tout', 'chaque', 'aucun', 'tel', 'plusieurs', 
			'autre', 'nul', 'de', 'à', 'en', 'dans', 'pour', 'par', 'sur', 'avec', 'ns', 'sous', 'après', 'entre', 'vers', 'chez', 'jusque', 'contre', 'devant', 'depuis', 'pendant', 'avant',
			'voilà', 'près', 'dès', 'malgré', 'voici', 'il', 'je', 'se', 'qui', 'elle', 'ce', 'le', 'que', 'vous', 'me', 'on', 'lui', 'nous', 'tu', 'moi', 'te', 'celui', 'rien', 'dont', 'tout',
			'ça', 'cela']

arabwords = ['كما', 'له', 'أن', 'هو', 'كان', 'إلى', 'في', 'هي', 'مع', 'هم', 'يكون', 'في', 'واحد', 'ديك', 'هذا', 'من', 'بواسطة', 'حار', 'كلمة', 'لكن', 'ما', 'بعض', 'هو', 
			'هو', 'أنت', 'أو', 'كان', 'و', 'من', 'إلى', 'و', 'و', 'في', 'نحن', 'علبة', 'خارج', 'البعض', 'و', 'التي', 'القيام', 'من', 'الوقت', 'إذا', 'سوف', 'كيف', 'قال', 'و', 'كل',
			'أقول', 'لا', 'مجموعة', 'ثلاثة', 'تريد', 'هواء', 'جيد', 'أيضا', 'لعب', 'صغير', 'نهاية', 'وضع', 'المنزل', 'قرأ', 'يد', 'ميناء', 'كبير', 'تهجى', 'إضافة', 'حتى', 'الأرض', 
			'هنا', 'يجب', 'كبير', 'ارتفاع', 'مثل', 'تابع', 'فعل', 'لماذا', 'تطلب', 'الرجال', 'تغيير', 'ذهب', 'ضوء', 'نوع', 'بعيدا', 'تحتاج', 'منزل', 'صور', 'محاولة', 'لنا', 
			'مرةأخرى', 'الحيوان', 'نقطة', 'أم', 'قرب', 'بناء', 'النفس', 'أرض', 'الأب', 'أي', 'جديدة', 'العمل', 'جزء', 'أخذ', 'الحصولعلى', 'مكان', 'مصنوع', 'حي', 'حيث', 'بعد', 
			'ظهر', 'القليل', 'فقط', 'جولة', 'رجل', 'عام', 'جاء', 'المعرض', 'كل', 'جيد', 'أنا', 'منح', 'لدينا', 'تحت', 'اسم', 'جدا', 'منخلال', 'فقط', 'شكل', 'عقوبة', 'عظيم', 
			'اعتقد', 'قول', 'مساعدة', 'منخفض', 'خط', 'اختلف', 'منعطف', 'السبب', 'كثيرا', 'متوسط', 'قبل', 'خطوة', 'الحق', 'صبي', 'قديم', 'أيضا', 'نفسه', 'هي', 'كل', 'هناك', 
			'عندما', 'فوق', 'استخدام', 'ك', 'طريق', 'حول', 'ثم', 'هم', 'إرسال', 'أراد', 'مثل', 'هكذا', 'هؤلاء', 'لها', 'طويل', 'جعل', 'شيء', 'شاهد', 'له', 'اثنين', 'لديه',
			'بحث', 'أكثر', 'يوم', 'يمكن', 'تذهب', 'جاء', 'لم', 'عدد', 'صوت', 'لا', 'أكثر', 'الناس', 'لي', 'على', 'تعرف', 'ماء', 'من', 'دعوة', 'الأول', 'الذي', 'قد', 'إلى', 
			'الجانب', 'كان', 'الآن', 'اكتشاف', 'رئيس', 'الوقوف', 'الخاصة', 'الصفحة', 'ينبغي', 'بلد', 'أسس', 'الجواب', 'المدرسة', 'تنمو', 'دراسة', 'لايزال', 'تعلم', 'مصنع', 
			'غطاء', 'غذاء', 'شمس', 'أربعة', 'بين', 'دولة', 'احتفظ', 'العين', 'أبدا', 'آخر', 'سمح', 'يعتقد', 'المدينة', 'شجرة', 'عبور', 'مزرعة', 'شاق', 'بداية', 'قد', 'قصة',
			'منشار', 'الآن', 'بحر', 'رسم', 'غادر', 'متأخر', 'تشغيل', 'لا', 'فيحين', 'الصحافة', 'قريب', 'الليل', 'حقيقية', 'حياة', 'قليل', 'شمال', 'كتاب', 'حمل', 'استغرق', 
			'علم', 'أكل', 'غرفة', 'صديق', 'بدأ', 'فكرة', 'سمك', 'الجبل', 'توقف', 'مرةواحدة', 'قاعدة', 'سمع', 'الحصان', 'قطع', 'بالتأكيد', 'راقب', 'لون', 'وجه', 'الخشب', 
			'رئيسي', 'مفتوحة', 'يبدو', 'معا', 'المقبل', 'أبيض', 'الأطفال', 'بدأ', 'حصلت', 'سير', 'مثال', 'سهولة', 'ورق', 'مجموعة', 'دائما', 'الموسيقى', 'تلك', 'كلا', 'علامة',
			'غالبا', 'الرسالة', 'حتى', 'ميل', 'النهر', 'سيارة', 'قدم', 'الرعاية', 'ثان']

portgwords = ['como', 'I', 'seu', 'que', 'ele', 'foi', 'para', 'em', 'são', 'com', 'eles', 'ser', 'em', 'uma', 'tem', 'este', 'a', 'por', 'quente', 'palavra', 'mas', 'o', 'alguns',
			'é', 'ele', 'você', 'ou', 'teve', 'o', 'de', 'a', 'e', 'uma', 'em', 'nós', 'lata', 'fora', 'outro', 'foram', 'que', 'fazer', 'seu', 'tempo', 'se', 'vontade', 'como', 'disse', 'uma', 
			'cada', 'dizer', 'faz', 'conjunto', 'três', 'quer', 'ar', 'bem', 'também', 'jogar', 'pequeno', 'fim', 'colocar', 'casa', 'ler', 'mão', 'port', 'grande', 'soletrar', 'adicionar', 
			'mesmo', 'terra', 'aqui', 'necessário', 'grande', 'alto', 'tais', 'siga', 'ato', 'por', 'perguntar', 'homens', 'mudança', 'fui', 'luz', 'tipo', 'off', 'precisa', 'casa', 'imagem', 
			'tentar', 'nós', 'novamente', 'animais', 'ponto', 'mãe', 'mundo', 'perto', 'construir', 'auto', 'terra', 'pai', 'qualquer', 'novo', 'trabalho', 'parte', 'tomar', 'obter', 'lugar',
			'feito', 'viver', 'onde', 'depois', 'de', 'pouco', 'apenas', 'rodada', 'homem', 'ano', 'veio', 'exposição', 'cada', 'bom', 'me', 'dar', 'nossa', 'sob', 'nome', 'muito', 'através',
			'justo', 'forma', 'sentença', 'grande', 'acho', 'dizer', 'ajudar', 'baixo', 'linha', 'diferir', 'vez', 'causa', 'muito', 'significar', 'antes', 'mudança', 'direito', 'menino', 
			'velho', 'também', 'mesmo', 'ela', 'tudo', 'lá', 'quando', 'up', 'usar', 'seu', 'maneira', 'sobre', 'muitos', 'depois', 'eles', 'escrever', 'faria', 'como', 'assim', 'estes', 
			'seu', 'longo', 'fazer', 'coisa', 'veja', 'ele', 'dois', 'tem', 'olhar', 'mais', 'dia', 'poderia', 'ir', 'vir', 'fez', 'número', 'som', 'não', 'mais', 'pessoas', 'meu', 'sobre',
			'sei', 'água', 'que', 'chamada', 'primeiro', 'que', 'pode', 'para', 'lado', 'sido', 'agora', 'encontrar', 'cabeça', 'ficar', 'próprio', 'página', 'deveria', 'país', 'encontrado',
			'resposta', 'escola', 'crescer', 'estudo', 'ainda', 'aprender', 'planta', 'cobertura', 'alimentos', 'sol', 'quatro', 'entre', 'estado', 'manter', 'olho', 'nunca', 'último',
			'deixar', 'pensava', 'cidade', 'árvore', 'atravessar', 'fazenda', 'difícil', 'começo', 'poder', 'história', 'serra', 'longe', 'mar', 'desenhar', 'esquerda', 'tarde', 'run',
			'não', 'enquanto', 'imprensa', 'perto', 'noite', 'reais', 'vida', 'poucos', 'norte', 'livro', 'carregam', 'tomou', 'ciência', 'comer', 'quarto', 'amigo', 'começou', 'idéia',
			'peixe', 'montanha', 'Pare', 'uma', 'base', 'ouvir', 'cavalo', 'corte', 'certo', 'assista', 'cor', 'rosto', 'madeira', 'principal', 'aberto', 'parecem', 'juntos', 'próximo', 
			'branco', 'crianças', 'início', 'tem', 'andar', 'exemplo', 'facilidade', 'papel', 'grupo', 'sempre', 'música', 'aqueles', 'tanto', 'marca', 'muitas', 'carta', 'até', 'milha',
			'rio', 'carro', 'pés', 'cuidados', 'segunda']

russwords = ['как', 'Я','что', 'он', 'было', 'для', 'на', 'являются', 'они', 'быть', 'в', 'один', 'иметь', 'это', 'от', 'по', 'горячий', 'слово', 'но', 'что', 
			'некоторые', 'является', 'это', 'вы', 'или', 'было', 'площадь', 'из', 'и', 'основной', 'взял', 'мы', 'может', 'из', 'другой', 'были', 'который', 'сделать', 'их',
			'время', 'если', 'будет', 'как', 'указанный', 'назад', 'каждый', 'сказать', 'делает', 'набор', 'три', 'хочу', 'воздух', 'хорошо', 'также', 'играть', 'небольшой', 'конец',
			'положить', 'домой', 'читать', 'рука', 'порт', 'большой', 'заклинание', 'добавлять', 'даже', 'земля', 'здесь', 'должны', 'большой', 'высокий', 'такие', 'следовать', 'акт',
			'почему', 'спросите', 'люди', 'изменение', 'пошел', 'свет', 'вид', 'от', 'нуждаться', 'дом', 'картинка', 'пытаться', 'нам', 'снова', 'животных', 'точка', 'мать', 'мир',
			'около', 'строить', 'самостоятельно', 'земля', 'отец', 'любой', 'новый', 'работа', 'часть', 'принимать', 'получать', 'место', 'сделал', 'жить', 'где', 'после', 'назад', 
			'немного', 'только', 'круглый', 'человек', 'год', 'пришел', 'шоу', 'каждый', 'хорошее', 'меня', 'давать', 'наш', 'под', 'название', 'очень', 'через', 'просто', 'форма',
			'приговор', 'большой', 'думать', 'сказать', 'помощь', 'низкий', 'линия', 'отличаются', 'поворот', 'причиной', 'много', 'означать', 'до', 'движение', 'право', 'мальчик',
			'старый', 'слишком', 'же', 'она', 'все', 'там', 'когда', 'вверх', 'использование', 'ваш', 'способ', 'многие', 'затем', 'их', 'запись', 'бы', 'подобно', 'так', 'эти', 
			'долго', 'сделать', 'вещь', 'посмотреть', 'два', 'имеет', 'искать', 'еще', 'день', 'мог', 'идти', 'приходят', 'сделал', 'число', 'звук', 'нет', 'наиболее',
			'люди', 'мой', 'над', 'знать', 'вода', 'чем', 'вызов', 'первый', 'кто', 'может', 'вниз', 'сторона', 'был', 'сейчас', 'находить', 'руководитель', 'стоять', 'самостоятельно',
			'страница', 'должны', 'страна', 'найдено', 'ответ', 'школа', 'расти', 'исследование', 'еще', 'учиться', 'завод', 'крышка', 'еда', 'солнце', 'четыре', 'между', 'состояние',
			'держать', 'глаз', 'никогда', 'Последнее', 'позволять', 'мысль', 'город', 'дерево', 'пересекают', 'ферма', 'трудно', 'начало', 'мощи', 'история', 'пила', 'далеко', 'море',
			'привлечь', 'слева', 'поздно', 'запустить', 'не', 'в', 'нажмите', 'близко', 'ночь', 'реальный', 'жизнь', 'несколько', 'к', 'книга', 'нести', 'взял', 'наука', 'есть', 
			'номер', 'друг', 'начал', 'идея', 'рыба', 'остановить', 'раз', 'база', 'слышать', 'лошадь', 'вырезать', 'уверен', 'смотреть', 'цвет', 'лицо', 'дерево', 'основной',
			'открыт', 'кажется', 'вместе', 'следующий', 'белый', 'дети', 'начать', 'получил', 'ходить', 'пример', 'легкость', 'бумага', 'группа', 'всегда', 'музыка', 'тех', 'как', 
			'знак', 'часто', 'письмо', 'до', 'км', 'река', 'автомобиль', 'футов', 'уход']

chinwords = ['一', '人', '里', '会', '没', '她', '吗', '去', '也', '有', '这', '那', '不', '什', '个', '来', '要', '就', '我', '你', '的', '是', '了', '他', '么', '们', '在', '说', '为', 
			'好', '吧', '知道', '我的', '和', '你的', '想', '只', '很', '都', '对', '把', '啊', '怎', '得', '还', '过', '不是', '到', '样', '飞', '远', '身', '任何', '生活', '够', '号', '兰', '瑞',
			'达', '或', '愿', '蒂', '別', '军', '正', '是不是', '证', '不用', '三', '乐', '吉', '男人', '告訴', '路', '搞', '可是', '与', '次', '狗', '决', '金', '史', '姆', '部', '正在', '活', '刚',
			'回家', '贝', '如何', '须', '战', '不會', '夫', '喂', '父', '亚', '肯定', '女孩', '世界', '不要', '些', '不知道', '不能', '因', '觉', '发', '像', '太', '但是', '多', '打', '机', '來', 
			'好了', '用', '他的', '诉', '德', '叫', '什麼', '真', '干', '心', '走', '比', '死', '嘿', '出', '车', '一下', '中', '好吧', '需要', '经', '妈', '候', '长', '而', '错', '好的', '间', 
			'又', '国', '起', '动', '杀', '于', '种', '去了', '担', '名', '混蛋', '礼', '幹', '不了', '有些', '過', '後', '击', '漂亮', '神', '多少', '海', '每', '哥', '教', '走吧', '好像', '单', 
			'公', '林', '女', '忙', '火', '钟', '家伙', '科', '回去', '最后', '水', '不管', '麦', '泻', '鬼', '還', '船', '永', '安全', '那個', '爾', '這麼', '满', '风', '皮', '威', '据', '鲁', 
			'转', '相', '地方', '沒有', '有人', '嗨', '看看', '自己', '一定', '事情', '屑', '希望', '所', '褉', '感', '气', '不想', '嘛', '实', '始', '給', '然后', '個', '相信', '结', '今天', '几',
			'题', '放', '讓', '确', '意思', '成', '所有', '喜', '對', '之', '一切', '记', '抱歉', '一直', '天', '褌', '钱', '面', '更', '学', '現在', '边', '你們', '不起', '脑', '呃', '论', '曼',
			'點', '普', '第一', '通', '棒', '线', '很高', '买', '求', '束', '哇', '指', '张', '文', '锌', '重', '菲', '目', '根本', '联', '丹', '愛', '不到', '這些', '自己的', '笑', '闭', '基',
			'唯一', '要是', '提', '调', '丽', '女士', '校', '公司', '况', '烦', '停', '英', '警', '险', '東西', '不可能', '坐', '区', '果']

hebrewords = ['כמו', 'אני', 'שלו', 'ש', 'הוא', 'היה', 'עבור', 'על', 'הם', 'עם', 'הם', 'להיות', 'ב', 'אחד', 'יש', 'זה', 'מ', 'על', 'חם', 'מילה', 'אבל', 'מה', 'כמה', 'הוא', 'זה',
			'אתה', 'או', 'היה', 'עבור', 'של', 'אל', 'זמן', 'ב', 'אנחנו', 'יכול', 'את', 'אחר', 'היו', 'ש', 'לעשות', 'שלהם', 'זמן', 'אם', 'יהיה', 'איך', 'אמר', 'בית', 'כל', 'לספר', 
			'עושה', 'שלוש', 'רוצה', 'אוויר', 'גם', 'גם', 'לשחק', 'קטן', 'סוף', 'לשים', 'בית', 'לקרוא', 'יד', 'נמל', 'גדול', 'לאיית', 'להוסיף', 'אפילו', 'ארץ', 'כאן', 'חייב',
			'גבוה', 'כזה', 'מעקב', 'מעשה', 'מדוע', 'שואל', 'אנשים', 'לשנות', 'הלכתי', 'אור', 'סוג', 'את', 'צריך', 'בית', 'תמונה', 'לנסות', 'שלנו', 'שוב', 'חיה', 'נקודה',
			'אמא', 'עולם', 'ליד', 'לבנות', 'עצמי', 'כדור', 'אב', 'כל', 'חדש', 'עבודה', 'חלק', 'לקחת', 'לקבל', 'מקום', 'עשיתי', 'לחיות', 'איפה', 'לאחר', 'בחזרה', 'קטן', 'רק', 'עגול',
			'גבר', 'שנה', 'הגיע', 'מופע', 'כל', 'טוב', 'לי', 'לתת', 'שלנו', 'תחת', 'שם', 'מאוד', 'דרך', 'רק', 'טופס', 'משפט', 'גדול', 'חושב', 'אומר', 'לעזור', 'נמוך', 'שורה', 'שונה',
			'תור', 'סיבה', 'הרבה', 'אומר', 'לפני', 'מהלך', 'נכון', 'ילד', 'ישן', 'גם', 'אותו', 'היא', 'כל', 'שם', 'כאשר', 'למעלה', 'שימוש', 'שלך', 'דרך', 'על', 'רבים', 'אז', 'שלהם',
			'לכתוב', 'היית', 'כמו', 'כך', 'אלה', 'שלה', 'ארוך', 'לעשות', 'דבר', 'לראות', 'שלו', 'שנים', 'יש', 'להסתכל', 'יותר', 'יום', 'יכול', 'ללכת', 'תבואו', 'עשיתי', 'מספר', 'נשמע',
			'לא', 'ביותר', 'אנשים', 'שלי', 'על', 'יודע', 'מים', 'מאשר', 'שיחה', 'ראשון', 'מי', 'רשאי', 'למטה', 'צד', 'היה', 'עכשיו', 'למצוא', 'ראש', 'לעמוד', 'של', 'דף', 'צריך', 
			'מדינה', 'מצאתי', 'תשובה', 'בית', 'לגדול', 'מחקר', 'עוד', 'ללמוד', 'צמח', 'כיסוי', 'מזון', 'שמש', 'ארבעה', 'בין', 'מדינה', 'לשמור', 'עין', 'אף', 'אחרון', 'בואו', 'חשבתי',
			'עיר', 'עץ', 'לחצות', 'החווה', 'קשה', 'התחלה', 'אולי', 'סיפור', 'מסור', 'רחוק', 'ים', 'לצייר', 'עזב', 'מאוחר', 'לרוץ', 'לא', 'תוך', 'עיתונות', 'קרוב', 'לילה', 'אמיתי',
			'חיים', 'כמה', 'צפון', 'ספר', 'לשאת', 'לקחתי', 'מדע', 'לסעוד', 'חדר', 'חבר', 'החל', 'רעיון', 'דגים', 'הר', 'להפסיק', 'פעם', 'בסיס', 'לשמוע', 'לחתוך', 'בטוח', 
			'לצפות', 'צבע', 'פנים', 'עץ', 'עיקרי', 'פתוח', 'נראה', 'יחד', 'הבא', 'לבן', 'ילדים', 'להתחיל', 'לי', 'ללכת', 'דוגמא', 'להקל', 'נייר', 'קבוצה', 'תמיד', 'מוסיקה', 'אלה', 
			'שני', 'סימן', 'לעתים', 'מכתב', 'עד', 'מייל', 'נהר', 'מכונית', 'רגליים', 'טיפול', 'שני']

norwords = ['som', 'jeg', 'hans', 'at', 'han', 'var', 'for', 'på', 'er', 'med', 'de', 'være', 'på', 'ett', 'har', 'dette', 'fra', 'etter', 'varm', 'ordet', 'men', 'Hva', 'noen', 'er',
			'den', 'du', 'eller', 'hadde', 'den', 'av', 'til', 'og', 'en', 'i', 'vi', 'kan', 'ut', 'andre', 'var', 'som', 'gjøre', 'deres', 'tid', 'hvis', 'vil', 'hvordan', 'sa', 'en', 'hver',
			'fortelle', 'gjør', 'sett', 'tre', 'ønsker', 'luft', 'godt', 'også', 'spille', 'liten', 'ende', 'sette', 'hjem', 'lese', 'hånd', 'port', 'stor', 'stave', 'legge', 'selv', 'landet',
			'her', 'må', 'big', 'høy', 'slik', 'følg', 'handle', 'hvorfor', 'spør', 'menn', 'endring', 'gikk', 'lys', 'kind', 'off', 'trenger', 'huset', 'bilde', 'prøve', 'oss', 'igjen', 'dyr',
			'punkt', 'mor', 'verden', 'nær', 'bygge', 'selv', 'jorden', 'far', 'noen', 'ny', 'arbeid', 'del', 'ta', 'få', 'sted', 'gjort', 'leve', 'der', 'etter', 'tilbake', 'lite', 'bare',
			'runde', 'mann', 'år', 'kom', 'vis', 'alle', 'god', 'meg', 'gi', 'vår', 'etter', 'navn', 'veldig', 'gjennom', 'bare', 'skjema', 'setning', 'stor', 'tror', 'si', 'hjelpe', 'lav',
			'etter', 'avvike', 'sving', 'årsaken', 'mye', 'mener', 'før', 'flytte', 'høyre', 'gutt', 'gammel', 'også', 'samme', 'hun', 'alle', 'det', 'når', 'opp', 'bruk', 'din', 'måte',
			'om', 'mange', 'deretter', 'dem', 'skrive', 'ville', 'som', 'så', 'disse', 'henne', 'lang', 'gjøre', 'ting', 'se', 'ham', 'to', 'har', 'se', 'mer', 'dag', 'kunne', 'gå', 'kommer', 
			'gjorde', 'nummer', 'høres', 'no', 'mest', 'folk', 'min', 'løpet', 'vet', 'vann', 'enn', 'samtale', 'første', 'som', 'kan', 'ned', 'side', 'vært', 'nå', 'finne', 'hode', 'stå',
			'egen', 'side', 'bør', 'landet', 'funnet', 'svar', 'skole', 'vokse', 'studien', 'fortsatt', 'lære', 'anlegg', 'dekselet', 'mat', 'sol', 'fire', 'mellom', 'stat', 'holde', 'øye',
			'aldri', 'siste', 'la', 'trodde', 'by', 'tre', 'krysse', 'gård', 'vanskelig', 'start', 'kanskje', 'historien', 'sag', 'langt', 'sea', 'tegne', 'venstre', 'sent', 'kjøre', 
			'ikke', 'mens', 'trykk', 'nær', 'natt', 'real', 'livet', 'noen', 'nord', 'bok', 'bære', 'tok', 'vitenskap', 'spise', 'rom', 'venn', 'begynte', 'ide', 'fisk', 'fjellet', 
			'stoppe', 'gang', 'basen', 'høre', 'hest', 'kutt', 'sikker', 'se', 'farge', 'ansikt', 'tre', 'hoved', 'åpent', 'synes', 'sammen', 'neste', 'hvit', 'barn', 'begynne', 'fikk', 
			'gå', 'eksempel', 'lette', 'papir', 'gruppe', 'alltid', 'musikk', 'de', 'både', 'mark', 'ofte', 'brev', 'før', 'mile', 'elv', 'bil', 'føtter', 'omsorg', 'andre']

hindiwords = ['जैस', 'मैं', 'उसके', 'कि', 'वह', 'था', 'के', 'पर', 'हैं', 'साथ', 'वे', 'हो', 'पर', 'एक', 'है', 'इस', 'से', 'द्वारा', 'गरम', 'शब्द', 'लेकिन', 'क्या', 'कुछ', 'है', 'यह', 'आप', 'या',
			'था', 'th', 'की', 'तक', 'और', 'एक', 'में', 'हम', 'कर', 'बाहर', 'अन्य', 'थे', 'जो', 'कर', 'उनके', 'समय', 'अगर', 'होगा', 'कैसे', 'कहा', 'एक', 'प्रत्येक', 'बता', 'करता', 'सेट', 'तीन', 'चाहते', 
			'हवा', 'अच्छी', 'भी', 'खेलने', 'छोटे', 'अंत', 'डाल', 'घर', 'पढ़ा', 'हाथ', 'बंदरगाह', 'बड़ा', 'जादू', 'जोड़', 'और', 'भूमि', 'यहाँ', 'चाहिए', 'बड़ा', 'उच्च', 'ऐसा', 'का', 'अधिनियम', 'क्यों', 'पूछना',
			'पुरुषों', 'परिवर्तन', 'चला', 'प्रकाश', 'तरह', 'बंद', 'आवश्यकता', 'घर', 'तस्वीर', 'कोशिश', 'हमें', 'फिर', 'पशु', 'बिंदु', 'मां', 'दुनिया', 'निकट', 'बनाना', 'आत्म', 'पृथ्वी', 'पिता', 'किसी', 'नई', 'काम',
			'हिस्सा', 'लेना', 'प्राप्त', 'जगह', 'निर्मित', 'जीना', 'जहां', 'के', 'वापस', 'थोड़ा', 'केवल', 'दौर', 'आदमी', 'वर्ष', 'आया', 'शो', 'हर', 'अच्छा', 'मुझे', 'दे', 'हमारे', 'नीचे', 'नाम', 'बहुत', 'के', 'बस',
			'फार्म', 'वाक्य', 'महान', 'लगता', 'कहना', 'मदद', 'कम', 'रेखा', 'अलग', 'बारी', 'कारण', 'ज्यादा', 'मतलब', 'पहले', 'चाल', 'सही', 'लड़का', 'पुराना', 'भी', 'वही', 'वह', 'सब', 'वहाँ', 'जब', 'ऊपर',
			'उपयोग', 'अपने', 'रास्ता', 'के', 'कई', 'तो', 'उन्हें', 'लिखना', 'होगा', 'जैसा', 'तो', 'इन', 'उसके', 'लंबे', 'कर', 'बात', 'देखना', 'उसे', 'दो', 'है', 'देखो', 'अधिक', 'दिन', 'सकता', 'जाना', 'आ',
			'किया', 'संख्या', 'ध्वनि', 'नहीं', 'सबसे', 'लोग', 'मेरे', 'अधिक', 'पता', 'पानी', 'से', 'कॉल', 'पहले', 'कौन', 'मई', 'नीचे', 'पक्ष', 'गया', 'अब', 'लगता', 'सिर', 'खड़े', 'खुद', 'पेज', 'चाहिए', 'देश', 
			'पाया', 'जवाब', 'स्कूल', 'बढ़ने', 'अध्ययन', 'अब', 'सीखना', 'संयंत्र', 'कवर', 'भोजन', 'सूरज', 'चार', 'के', 'राज्य', 'रखना', 'आंख', 'कभी', 'पिछले', 'चलो', 'सोचा', 'शहर', 'पेड़', 'पार', 'खेत',
			'कठिन', 'शुरुआत', 'हो', 'कहानी', 'देखा', 'दूर', 'समुद्र', 'आकर्षित', 'छोड़ा', 'देर', 'चलाने', 'ऐसा', 'जबकि', 'प्रेस', 'करीब', 'रात', 'असली', 'जीवन', 'कुछ', 'उत्तर', 'किताब', 'ले', 'ले', 'विज्ञान',
			'खाने', 'कमरे', 'दोस्त', 'शुरू', 'विचार', 'मछली', 'पहाड़', 'रोक', 'एक', 'आधार', 'सुनना', 'घोड़ा', 'कटौती', 'यकीन', 'घड़ी', 'रंग', 'चेहरा', 'लकड़ी', 'मुख्य', 'खुला', 'प्रतीत', 'एक', 'अगला',
			'सफेद', 'बच्चों', 'प्रारंभ', 'मिला', 'चलना', 'उदाहरण', 'आसानी', 'कागज', 'समूह', 'सदैव', 'संगीत', 'उन', 'दोनों', 'मार्क', 'अक्सर', 'पत्र', 'जब', 'मील', 'नदी', 'कार', 'पैर', 'देखभ']

language = engwords

def seeLangs() :

	def chgL(lang) :
		global language
		language=lang
		if language == russwords : root.geometry("800x300")
		elif language == germwords : root.geometry("750x300")
		else : root.geometry("645x300")
		restartCommand()
		rl.destroy()

	rl = Tk() 
	rl.title("Choose Language")

	e = Button(rl, text="English", command = lambda : chgL(engwords))
	e.grid(row=0, column=0)

	s = Button(rl, text="Spanish", command = lambda : chgL(spawords))
	s.grid(row=1, column=0)

	i = Button(rl, text="Italian", command = lambda : chgL(italwords))
	i.grid(row=2, column=0)

	g = Button(rl, text="German", command = lambda : chgL(germwords))
	g.grid(row=3, column=0)


	f = Button(rl, text="French", command = lambda : chgL(frenwords))
	f.grid(row=0, column=1)

	a = Button(rl, text="Arab", command = lambda : chgL(arabwords))
	a.grid(row=1, column=1)

	p = Button(rl, text="Portuguese", command = lambda : chgL(portgwords))
	p.grid(row=2, column=1)

	r = Button(rl, text="Russian", command = lambda : chgL(russwords))
	r.grid(row=3, column=1)

	c = Button(rl, text="Chinese", command = lambda : chgL(chinwords))
	c.grid(row=0, column=2)

	he = Button(rl, text="Hebrew", command = lambda : chgL(hebrewords))
	he.grid(row=1, column=2)

	n = Button(rl, text="Norwegian", command = lambda : chgL(norwords))
	n.grid(row=2, column=2)

	hi = Button(rl, text="Hindi", command = lambda : chgL(hindiwords))
	hi.grid(row=3, column=2)

	rl.mainloop()

def generateWords(words) :
	global language
	st = []

	for i in range(15) :
		a = random.randint(0, 20)
		b = random.randint(0, 20)

		if a == b :
			res = (words[random.randint(0, len(language)-1)]).capitalize()
		else : res = (words[random.randint(0, len(language)-1)])

		st.append(res)

	return st

seconds2 = 60

def updateTable(s,a,r,w, id) :
	if getMax() == [] :
		cursor.execute("INSERT INTO registro (speed, perc, right, wrong) VALUES (?,?,?,?)", (0,0,0,0))
	cursor.execute("UPDATE registro SET speed = ?, perc = ?, right = ?, wrong = ? where id >= 0", (s,a,r,w))
	bbdd.commit()

def restartCommand() :

	global GeneralCount, rightwords, wrongwords, t, seconds, word, c, mixedwords1, mixedwords2, w, listwords1, listwords2, timeCount, tf

	barra["state"] = NORMAL
	GeneralCount = 0
	rightwords = 0
	wrongwords = 0
	t = 0
	seconds = seconds2
	word.set("")
	c = 0
	timeCount = 0
	tf = False

	listwords1 = generateWords(language)
	listwords2 = generateWords(language)

	mixedwords1.set(" ".join(listwords1))
	mixedwords2.set(" ".join(listwords2))
	timevar.set(seconds)

	barra.delete(0, END)
	wr.set("")
	ri.set("")
	sp.set("")
	ac.set("")

def startCommand() :

	global c, mixedwords1, mixedwords2, listwords1, listwords2, rightwords, wrongwords, texto1, texto2, t, GeneralCount, language, timeCount, seconds, start, tf
	global sp, ac, ri, wr

	start["state"] = DISABLED
	restart["state"] = NORMAL
	timeCount += 1

	barra.focus()

	if timeCount == (10) :
		timeCount = 0
		if seconds > 0 :
			seconds -= 1
			timevar.set(seconds)
		if seconds == 0 : timevar.set("Finished")

	if seconds == 0 :
		try :
			if not tf :
				GeneralCount *= (60/seconds2)
				tf = True

			accuracy = (rightwords / (wrongwords + rightwords)) * 100
			spiid = int(GeneralCount // 5)

			
			spe = Label(frame, text=sp, textvariable=sp)
			spe.grid(row=7, column=1)
			sp.set(f"Speed : {spiid}wpm")

			
			accur = Label(frame, text=ac, textvariable=ac)
			accur.grid(row=8, column=1)
			ac.set(f"Accuracy : {round(accuracy)}%")

			
			right = Label(frame, text=ri, textvariable=ri)
			right.grid(row=7, column=3)
			ri.set("Right Words : " + str(rightwords))

			
			wrong = Label(frame, text=wr, textvariable=wr)
			wrong.grid(row=8, column=3)
			wr.set("Wrong Words : " + str(wrongwords))

			m = getMax()
			id = m[4]

			if m == [] : updateTable(spiid, round(accuracy), rightwords, wrongwords, id)
			elif spiid > m[0] or spiid == m[0] and round(accuracy) > m[1] :
				updateTable(spiid, round(accuracy), rightwords, wrongwords, id)

			barra["state"] = DISABLED
		except : pass

	word.set((listwords1[c] + " "))

	if barra.get() in ((listwords1[c] + " ")[:len(barra.get())]) :

		w["foreground"] = "green"
	else :
		w["foreground"]  = "red"

	if " " in barra.get() :
		if barra.get() == (listwords1[c] + " ") : 
			GeneralCount += (len(barra.get()) - 1)
			rightwords += 1
		else : wrongwords += 1

		barra.delete(0, END)

		c += 1
		if c == 15 : 
			c = 0

			texto1.destroy()
			texto2.destroy()
			cop = mixedwords2.get()
			mixedwords1.set("")
			mixedwords1.set(cop)
			listwords1 = listwords2

			mixedwords2.set("")
			listwords2 = generateWords(language)
			mixedwords2.set(" ".join(listwords2))

			texto1 = Label(frame, text=mixedwords1, textvariable=mixedwords1)
			texto1.grid(row=1, column=1, columnspan=3)

			texto2 = Label(frame, text=mixedwords2, textvariable=mixedwords2)
			texto2.grid(row=2, column=1, columnspan=3)
		
	root.after(100, startCommand)

def changeTimer(secs) :
	global seconds, seconds2, stat

	if seconds == seconds2 or seconds == 0 :
		stat = "normal"
		timevar.set(secs)
		seconds = secs
		seconds2 = secs
	else :
		stat = "DISABLED"
	

def seeMax() :
	m = getMax()
	r2 = Toplevel()
	r2.resizable(0,0)

	r22 = LabelFrame(r2, text="Best Attempt")
	r22.grid(row=0, column=0, padx=10, pady=10)

	Label(r22, text=f"Best Speed : {m[0]}", anchor="w").grid(row=0, column=0)
	Label(r22, text="").grid(row=1, column=0)
	Label(r22, text=f"Best Accuracy : {m[1]}", anchor="w").grid(row=2, column=0)
	Label(r22, text="").grid(row=3, column=0)
	Label(r22, text=f"Right Words : {m[2]}", anchor="w").grid(row=4, column=0)
	Label(r22, text="").grid(row=5, column=0)
	Label(r22, text=f"Wrong Words : {m[3]}", anchor="w").grid(row=6, column=0)

	r2.mainloop()

root = Tk()
root.title("Typing Test")
root.geometry("645x300")

#language = engwords

barramenu = Menu(root)
root.config(menu = barramenu)

barramenu.add_cascade(label="Best", command=seeMax)
barramenu.add_cascade(label="Language", command=seeLangs)


stat = "normal"
time = Menu(barramenu, tearoff = 0)
time.add_command(label = "30s", command = lambda : changeTimer(30), state=stat)
time.add_command(label = "60s", command = lambda : changeTimer(60), state=stat)
time.add_command(label = "120s", command = lambda : changeTimer(120), state=stat)

barramenu.add_cascade(label="Time", menu=time)

frame = Frame(root)
frame.pack()

title = Label(frame, text="Typing Test\n")
title.grid(row=0, column=1, columnspan=3)
title.config(font=("Times New Roman", 15))

listwords1 = generateWords(language)
listwords2 = generateWords(language)
mixedwords1 = StringVar()
mixedwords2 = StringVar()
mixedwords1.set(" ".join(listwords1))
mixedwords2.set(" ".join(listwords2))

texto1 = Label(frame, text=mixedwords1, textvariable=mixedwords1)
texto1.grid(row=1, column=1, columnspan=3)

texto2 = Label(frame, text=mixedwords2, textvariable=mixedwords2)
texto2.grid(row=2, column=1, columnspan=3)

Label(frame, text="").grid(row=3, column=0)

barra = Entry(frame, width=40)
barra.grid(row=4, column=1, columnspan=3)

Label(frame, text="").grid(row=5, column=0)

restart = Button(frame, text="Restart", command = restartCommand, width=6, state = DISABLED)
restart.grid(row=8, column=2)

start = Button(frame, text="Start", command = startCommand, width=6)
start.grid(row=7, column=2)

word = StringVar()
word.set(" ")

ac, sp, ri, wr = StringVar(),StringVar(),StringVar(),StringVar()


Label(frame, text="").grid(row=9, column=0)

w = Label(frame, text=word, textvariable=word, font=("Times New Roman", 20))
w.grid(row=10, column=2)

timevar = IntVar()

seconds = 60
timevar.set(seconds)
clo = Label(frame,textvariable=str(timevar), font=("Times New Roman", 15))
clo.grid(row=10, column=3)

root.mainloop()

