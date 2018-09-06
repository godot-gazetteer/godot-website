from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL, Optional, Regexp


class CyrenaicaYears(FlaskForm):
    year_reference_system = SelectField('Year Reference System:',
                                        choices=[('None', 'None'),
                                                 ('Unknown', 'Year of Unknown System'),
                                                 ('Era: Actian', 'Actian Era Year'),
                                                 ('Eponymous Officials: Apollo Priest (Cyrenaica)', 'Eponymous Apollo Priest'),
                                                 ('Regnal: Roman Emperors', 'Regnal Year (Roman Emperor)'),
                                                 ])
    year = StringField('Year:', validators=[
                        Optional(), Regexp('^[0-9_]*$')])
    apollo_priests_cyrenaica = SelectField('Apollo Priest Cyrenaica',
                                           choices=[('Διονύσιος Σότα (-19/-18)',
                                                     'Διονύσιος Σότα (-19/-18)'),
                                                    ('Φίλισκος Φιλίσκου φύσει δὲ Εὐφάνευς (-17/-16)',
                                                     'Φίλισκος Φιλίσκου φύσει δὲ Εὐφάνευς (-17/-16)'),
                                                    ('Νεικόστρατος (-16/-15)',
                                                     'Νεικόστρατος (-16/-15)'),
                                                    ('Παντα [--] (-15/-14)',
                                                     'Παντα [--] (-15/-14)'),
                                                    ('Βαρκαῖος Εὐφάνευς (begin of last quarter of 1. century BC)',
                                                     'Βαρκαῖος Εὐφάνευς (begin of last quarter of 1. century BC)'),
                                                    ('Εὐβάτας (begin of last quarter of 1. century BC)',
                                                     'Εὐβάτας (begin of last quarter of 1. century BC)'),
                                                    ('Κλήσιππος (begin of last quarter of 1. century BC)',
                                                     'Κλήσιππος (begin of last quarter of 1. century BC)'),
                                                    ('Ἀριστοτέλης Σώσιος (end of 1. century BC)',
                                                     'Ἀριστοτέλης Σώσιος (end of 1. century BC)'),
                                                    ('Εὐκλῆς Αἰγλάνορος (end of 1. century BC)',
                                                     'Εὐκλῆς Αἰγλάνορος (end of 1. century BC)'),
                                                    ('Παυσανίας Φιλίσκω φύσει δὲ Εὐφάνευς (2/3)',
                                                     'Παυσανίας Φιλίσκω φύσει δὲ Εὐφάνευς (2/3)'),
                                                    ('Ἰσοκράτης Κλεάρχω (3/4)',
                                                     'Ἰσοκράτης Κλεάρχω (3/4)'),
                                                    ('Ἀρίσταρχος Θευχρήστω',
                                                     'Ἀρίσταρχος Θευχρήστω'),
                                                    ('Θεύχρηστος Διονυσίω (19/20)',
                                                     'Θεύχρηστος Διονυσίω (19/20)'),
                                                    ('Φάος Κλεάρχω τῶ Φιλοπάτριδος',
                                                     'Φάος Κλεάρχω τῶ Φιλοπάτριδος'),
                                                    ('Ἴστρος Ἀγαθίνω',
                                                     'Ἴστρος Ἀγαθίνω'),
                                                    ('Ἀσκληπιάδης Ἐπικράτευς',
                                                     'Ἀσκληπιάδης Ἐπικράτευς'),
                                                    ('Εὐφάνης Ἰσοκράτευς',
                                                     'Εὐφάνης Ἰσοκράτευς'),
                                                    ('Πανταλέων Πανταλέοντος',
                                                     'Πανταλέων Πανταλέοντος'),
                                                    ('Ἰσοκράτης Ἀγχιστράτω',
                                                     'Ἰσοκράτης Ἀγχιστράτω'),
                                                    ('Φιλόξενος Φιλίσπω φύσει δὲ Εὐφάνευς',
                                                     'Φιλόξενος Φιλίσπω φύσει δὲ Εὐφάνευς'),
                                                    ('Αἰγλανωρ Πτολεμαίω (ca. 35 AD)',
                                                     'Αἰγλανωρ Πτολεμαίω (ca. 35 AD)'),
                                                    ('Φάος Καρνήδα',
                                                     'Φάος Καρνήδα'),
                                                    ('Φίλων Εὐφράνορος (38/39)',
                                                     'Φίλων Εὐφράνορος (38/39)'),
                                                    ('Φίλιππος Ἀριστάνδρω',
                                                     'Φίλιππος Ἀριστάνδρω'),
                                                    ('Κλέαρχος Εὐφάνευς',
                                                     'Κλέαρχος Εὐφάνευς'),
                                                    ('Ἴστρος Ἴστρω τῶ Ἀγαθίνω',
                                                     'Ἴστρος Ἴστρω τῶ Ἀγαθίνω'),
                                                    ('Πραξιάδας Πραξιἀδα τῶ Φιλίννα',
                                                     'Πραξιάδας Πραξιἀδα τῶ Φιλίννα'),
                                                    ('Εὐκλείδας Εὐκλείδα τῶ Εὐκλείδα',
                                                     'Εὐκλείδας Εὐκλείδα τῶ Εὐκλείδα'),
                                                    ('Σεραπίων Ἀριστάνδρω',
                                                     'Σεραπίων Ἀριστάνδρω'),
                                                    ('Ζηνίων Σώσου',
                                                     'Ζηνίων Σώσου'),
                                                    ('Κλέαρχος Καρνήδα',
                                                     'Κλέαρχος Καρνήδα'),
                                                    ('Μᾶρκος Κλέαρχος Φλάμμα Ἰσοκράτευς',
                                                     'Μᾶρκος Κλέαρχος Φλάμμα Ἰσοκράτευς'),
                                                    ('Λούκιος Καρνήδας Φλάμμα Ἰσοκράτευς',
                                                     'Λούκιος Καρνήδας Φλάμμα Ἰσοκράτευς'),
                                                    ('Ἄσκλαπος Ἰσοκράτους τοῦ Αγχιστράτω',
                                                     'Ἄσκλαπος Ἰσοκράτους τοῦ Αγχιστράτω'),
                                                    ('Ἀγχίστρατος Καρτισθένευς',
                                                     'Ἀγχίστρατος Καρτισθένευς'),
                                                    ('Τιβέριος Κλαύδιος Παγκλῆς',
                                                     'Τιβέριος Κλαύδιος Παγκλῆς'),
                                                    ('Μᾶρκος Αντώνιος Γέμελλος (begin of reign of Nero)',
                                                     'Μᾶρκος Αντώνιος Γέμελλος (begin of reign of Nero)'),
                                                    ('Τιβέριος Κλαύδιος Πρείσκος',
                                                     'Τιβέριος Κλαύδιος Πρείσκος'),
                                                    ('Τιβέριος Κλαύδιος Ἀρίστανδρος',
                                                     'Τιβέριος Κλαύδιος Ἀρίστανδρος'),
                                                    ('Τιβέριος Κλαύδιος Ἴστρος Φιλίσκου (59/60)',
                                                     'Τιβέριος Κλαύδιος Ἴστρος Φιλίσκου (59/60)'),
                                                    ('Τιβέριος Κλαύδιος Ἄσκλαπος Φιλίσκου (60/61)',
                                                     'Τιβέριος Κλαύδιος Ἄσκλαπος Φιλίσκου (60/61)'),
                                                    ('Μᾶρκος Ἀσίνιος Φίλωνος υἱὸς Εὐφράνωρ',
                                                     'Μᾶρκος Ἀσίνιος Φίλωνος υἱὸς Εὐφράνωρ'),
                                                    ('Τιβέριος Κλαύδιος Τιβερίω Κλαυδίω ἀρχιερέος υἱὸς Καρνήδας',
                                                     'Τιβέριος Κλαύδιος Τιβερίω Κλαυδίω ἀρχιερέος υἱὸς Καρνήδας'),
                                                    ('Μᾶρκος Ἄντωνιος Κεριάλις Πτολεμαίου τοῦ Πτολεμαίου υἱὸς Αἰγλάνωρ',
                                                     'Μᾶρκος Ἄντωνιος Κεριάλις Πτολεμαίου τοῦ Πτολεμαίου υἱὸς Αἰγλάνωρ'),
                                                    ('Μητρόδωρος Μητροδώρου τοῦ Μητροδώρου',
                                                     'Μητρόδωρος Μητροδώρου τοῦ Μητροδώρου'),
                                                    ('Τιβέριος Κλαύδιος Ἄρχιππος (67/68)',
                                                     'Τιβέριος Κλαύδιος Ἄρχιππος (67/68)'),
                                                    ('Μᾶρκος Ἀντώνιου Μᾶρκου Ἀντωνίος Φλάμμα υἱὸς Κασκέλλιος (68/69)',
                                                     'Μᾶρκος Ἀντώνιου Μᾶρκου Ἀντωνίος Φλάμμα υἱὸς Κασκέλλιος (68/69)'),
                                                    ('Σώτας Διονυσίου (begin of reign of Vespasian)',
                                                     'Σώτας Διονυσίου (begin of reign of Vespasian)'),
                                                    ('Τιβέριος Κλαύδιος Κλέαρχος',
                                                     'Τιβέριος Κλαύδιος Κλέαρχος'),
                                                    ('Μᾶρκος Ἀντώνιος Μᾶρκου Ἀντωνίου Φλάμμα υἱὸς Ἀριστομένης (73/74)',
                                                     'Μᾶρκος Ἀντώνιος Μᾶρκου Ἀντωνίου Φλάμμα υἱὸς Ἀριστομένης (73/74)'),
                                                    ('Τιβέριος Κλαύδιος Τιβερίω Κλαυδίος Ἴστρου υἱὸς Φίλισκος (75/76)',
                                                     'Τιβέριος Κλαύδιος Τιβερίω Κλαυδίος Ἴστρου υἱὸς Φίλισκος (75/76)'),
                                                    ('Τειμαγένης Θευδώρου (77/78)',
                                                     'Τειμαγένης Θευδώρου (77/78)'),
                                                    ('Εὐφράνωρ Άντιπάτρω (79/80)',
                                                     'Εὐφράνωρ Άντιπάτρω (79/80)'),
                                                    ('Φάβιος Φιλίσκου υἱὸς Φίλιππος (89/90)',
                                                     'Φάβιος Φιλίσκου υἱὸς Φίλιππος (89/90)'),
                                                    ('Τιβέριος Κλαύδιος Ἴστρος (91/92)',
                                                     'Τιβέριος Κλαύδιος Ἴστρος (91/92)'),
                                                    ('Ἄλεξις Καρνήδα (third quarter of 1. century AD)',
                                                     'Ἄλεξις Καρνήδα (third quarter of 1. century AD)'),
                                                    ('Καρνήδας Ἀλέξιος (third quarter of 1. century AD)',
                                                     'Καρνήδας Ἀλέξιος (third quarter of 1. century AD)'),
                                                    ('Φίλων Φιλοκώμω (third quarter of 1. century AD)',
                                                     'Φίλων Φιλοκώμω (third quarter of 1. century AD)'),
                                                    ('Βαρκαῖος Φίλωνος (third quarter of 1. century AD)',
                                                     'Βαρκαῖος Φίλωνος (third quarter of 1. century AD)'),
                                                    ('Ἀγχιστ[ρατ-] (1. century AD)',
                                                     'Ἀγχιστ[ρατ-] (1. century AD)'),
                                                    ('Ἄσκλαπος (1. century AD)',
                                                     'Ἄσκλαπος (1. century AD)'),
                                                    ('Θεο[-] Ἀγαθ[-] (1. century AD)',
                                                     'Θεο[-] Ἀγαθ[-] (1. century AD)'),
                                                    ('Τιβέριος Κλαύδιος Πτολεμαῖος (1. century AD)',
                                                     'Τιβέριος Κλαύδιος Πτολεμαῖος (1. century AD)'),
                                                    ('Λούκιος (1. century AD)',
                                                     'Λούκιος (1. century AD)'),
                                                    ('Ξοῦθος (1. century AD)',
                                                     'Ξοῦθος (1. century AD)'),
                                                    ('[--]ευς Πτολεμαῖου υἱὸς Πτολεμαῖος (1. century AD)',
                                                     '[--]ευς Πτολεμαῖου υἱὸς Πτολεμαῖος (1. century AD)'),
                                                    ('Φιλων Ἀγαθίνω (1. century AD)',
                                                     'Φιλων Ἀγαθίνω (1. century AD)'),
                                                    ('Φλάμμας (1. century AD)',
                                                     'Φλάμμας (1. century AD)'),
                                                    ('[--]ευς Πα[--] (1. century AD)',
                                                     '[--]ευς Πα[--] (1. century AD)'),
                                                    ('[--] Πτυλμαίου υἱὸ[ς --]ας (1. century AD)',
                                                     '[--] Πτυλμαίου υἱὸ[ς --]ας (1. century AD)'),
                                                    ('Τιβέριος Κλαύδιος Ἐπικράτευς υἱὸς Ἀσκλαπιάδας (late 1. century AD)',
                                                     'Τιβέριος Κλαύδιος Ἐπικράτευς υἱὸς Ἀσκλαπιάδας (late 1. century AD)'),
                                                    ('Μᾶρκος Ἀντώνιος Κασκέλλιος (late 1. century AD)',
                                                     'Μᾶρκος Ἀντώνιος Κασκέλλιος (late 1. century AD)'),
                                                    ('Τίτος Φλάβιος Σαβεῖνος υἱὸς Παυσανίου Παθσανίας (late 1. century AD)',
                                                     'Τίτος Φλάβιος Σαβεῖνος υἱὸς Παυσανίου Παθσανίας (late 1. century AD)'),
                                                    ('Τιβέριος Κλαυδίου Φειδίμου υἱὸς Ἴστρος (100/101)',
                                                     'Τιβέριος Κλαυδίου Φειδίμου υἱὸς Ἴστρος (100/101)'),
                                                    ('Κοίντος Φάβιος Καρνεάδης (101/102)',
                                                     'Κοίντος Φάβιος Καρνεάδης (101/102)'),
                                                    ('Τιβέριος Κλαύδιος Ἄτταλος Τιβερίου Κλαυδίου Κλεάρχου υἱὸς (102/103)',
                                                     'Τιβέριος Κλαύδιος Ἄτταλος Τιβερίου Κλαυδίου Κλεάρχου υἱὸς (102/103)'),
                                                    ('Τίτος Φλάβιος Εὐκλείδας (103/104)',
                                                     'Τίτος Φλάβιος Εὐκλείδας (103/104)'),
                                                    ('Τιβέριος Κλαύδιος Φιλόξενος Ἀντωνιανός (104/105)',
                                                     'Τιβέριος Κλαύδιος Φιλόξενος Ἀντωνιανός (104/105)'),
                                                    ('Γάιος Ποστόμιος Ὀπτάτος (106/107)',
                                                     'Γάιος Ποστόμιος Ὀπτάτος (106/107)'),
                                                    ('Τιβέριος Κλαύδιος Καρτισθένης Εὐφράνωρ (108/109)',
                                                     'Τιβέριος Κλαύδιος Καρτισθένης Εὐφράνωρ (108/109)'),
                                                    ('Πόπλιος Σήστιος Πολλίων (111/112)',
                                                     'Πόπλιος Σήστιος Πολλίων (111/112)'),
                                                    ('[--] Κλαύδιος [--] (begin of 2. century AD)',
                                                     '[--] Κλαύδιος [--] (begin of 2. century AD)'),
                                                    ('Τιβέριος Κλαύδιος Ἀρίστομένης Μᾶγνος ὁ καὶ Περικλῆς (begin of 2. century AD)',
                                                     'Τιβέριος Κλαύδιος Ἀρίστομένης Μᾶγνος ὁ καὶ Περικλῆς (begin of 2. century AD)'),
                                                    ('Ῥουτὶλιος (begin of 2. century AD)',
                                                     'Ῥουτὶλιος (begin of 2. century AD)'),
                                                    ])
    roman_emperors = SelectField('Roman Emperor:',
                                           choices=[('Augustus', 'Augustus'),
                                                    ('Tiberius', 'Tiberius'),
                                                    ('Caligula', 'Caligula'),
                                                    ('Claudius', 'Claudius'),
                                                    ('Nero', 'Nero'),
                                                    ('Galba', 'Galba'),
                                                    ('Otho', 'Otho'),
                                                    ('Vitellius', 'Vitellius'),
                                                    ('Vespasian', 'Vespasian'),
                                                    ('Titus', 'Titus'),
                                                    ('Domitian', 'Domitian'),
                                                    ('Nerva', 'Nerva'),
                                                    ('Trajan', 'Trajan'),
                                                    ('Hadrian', 'Hadrian'),
                                                    ('Antoninus Pius', 'Antoninus Pius'),
                                                    ('Marc Aurel', 'Marc Aurel'),
                                                    ('Commodus', 'Commodus'),
                                                    ('Pertinax', 'Pertinax'),
                                                    ('Pescennius Niger', 'Pescennius Niger'),
                                                    ('Septimius Severus', 'Septimius Severus'),
                                                    ('Caracalla', 'Caracalla'),
                                                    ('Macrinus', 'Macrinus'),
                                                    ('Elagabal', 'Elagabal'),
                                                    ('Severus Alexander', 'Severus Alexander'),
                                                    ('Maximinus Thrax', 'Maximinus Thrax'),
                                                    ('Gordian', 'Gordian'),
                                                    ('Phillippus Arabs', 'Phillippus Arabs'),
                                                    ('Decius', 'Decius'),
                                                    ('Gallus / Volusian', 'Gallus / Volusian'),
                                                    ('Aemilian', 'Aemilian'),
                                                    ('Valerian', 'Valerian'),
                                                    ('Macrianus / Quietus', 'Macrianus / Quietus'),
                                                    ('Gallienus', 'Gallienus'),
                                                    ('Claudius Gothicus', 'Claudius Gothicus'),
                                                    ('Aurelian', 'Aurelian'),
                                                    ('Tacitus', 'Tacitus'),
                                                    ('Probus', 'Probus'),
                                                    ('Carus / Carinus', 'Carus / Carinus'),
                                                    ('Diocletian', 'Diocletian'),
                                                    ])
    egyptian_calendar_months = SelectField('Months (Egyptian):',
                                        choices=[('None', 'None'),
                                                 ('Thot', 'Thot'),
                                                 ('Phaophi', 'Phaophi'),
                                                 ('Hathyr', 'Hathyr'),
                                                 ('Choiak', 'Choiak'),
                                                 ('Tybi', 'Tybi'),
                                                 ('Mecheir', 'Mecheir'),
                                                 ('Phamenoth', 'Phamenoth'),
                                                 ('Pharmuthi', 'Pharmuthi'),
                                                 ('Pachons', 'Pachons'),
                                                 ('Payni', 'Payni'),
                                                 ('Epeiph', 'Epeiph'),
                                                 ('Mesore', 'Mesore'),
                                                 ('epagomenal days','epagomenal days'),
                                                 ])
    day = StringField('Day:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    attestation_uri = StringField('Attestation URI:', validators=[DataRequired(), URL()])
    date_string = StringField('Date String:', validators=[DataRequired()])
    title = StringField('Title:', validators=[DataRequired()])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class RomanConsularDating(FlaskForm):
    consulship = StringField('Consulship:', validators=[DataRequired()])
    day_ref = SelectField('Kalends/Nones/Ides:',
                          choices=[('Kalends', 'Kalends'),
                                   ('Nones', 'Nones'),
                                   ('Ides', 'Ides'),
                                   ])
    months = SelectField('Month:',
                         choices=[('January', 'January'),
                                  ('February', 'February'),
                                  ('March', 'March'),
                                  ('April', 'April'),
                                  ('May', 'May'),
                                  ('June', 'June'),
                                  ('July', 'July'),
                                  ('August', 'August'),
                                  ('September', 'September'),
                                  ('October', 'October'),
                                  ('November', 'November'),
                                  ('December', 'December'),
                                  ])
    day_number = SelectField('Day:',
                             choices=[
                                 (1, ''),
                                 (2, 'a.d. II (pridie)'),
                                 (3, 'a.d. III'),
                                 (4, 'a.d. IV'),
                                 (5, 'a.d. V'),
                                 (6, 'a.d. VI'),
                                 (7, 'a.d. VII'),
                                 (8, 'a.d. VIII'),
                                 (9, 'a.d. IX'),
                                 (10, 'a.d. X'),
                                 (11, 'a.d. XI'),
                                 (12, 'a.d. XII'),
                                 (13, 'a.d. XIII'),
                                 (14, 'a.d. XIV'),
                                 (15, 'a.d. XV'),
                                 (16, 'a.d. XVI'),
                                 (17, 'a.d. XVII'),
                                 (18, 'a.d. XVIII'),
                                 (19, 'a.d. XIX'),
                             ])
    reset = SubmitField('Reset...')
    submit = SubmitField('Convert...')
