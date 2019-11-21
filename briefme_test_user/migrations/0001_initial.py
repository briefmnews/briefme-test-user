# Generated by Django 2.2.4 on 2019-11-21 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates if the user can log in.', verbose_name='active status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, default='', max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, default='', max_length=255, verbose_name='last name')),
                ('address', models.CharField(blank=True, default='', max_length=100, verbose_name='adresse')),
                ('city', models.CharField(blank=True, default='', max_length=40, verbose_name='ville')),
                ('zip', models.CharField(blank=True, default='', max_length=12, verbose_name='code postal')),
                ('country', models.CharField(blank=True, choices=[('FR', 'France'), ('AF', 'Afghanistan'), ('ZA', 'Afrique du Sud'), ('AL', 'Albanie'), ('DZ', 'Algérie'), ('DE', 'Allemagne'), ('AD', 'Andorre'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctique'), ('AG', 'Antigua-et-Barbuda'), ('AN', 'Antilles Néerlandaises'), ('SA', 'Arabie Saoudite'), ('AR', 'Argentine'), ('AM', 'Arménie'), ('AW', 'Aruba'), ('AU', 'Australie'), ('AT', 'Autriche'), ('AZ', 'Azerbaïdjan'), ('BS', 'Bahamas'), ('BH', 'Bahreïn'), ('BD', 'Bangladesh'), ('BB', 'Barbade'), ('BY', 'Bélarus'), ('BE', 'Belgique'), ('BZ', 'Belize'), ('BJ', 'Bénin'), ('BM', 'Bermudes'), ('BT', 'Bhoutan'), ('BO', 'Bolivie'), ('BA', 'Bosnie-Herzégovine'), ('BW', 'Botswana'), ('BR', 'Brésil'), ('BN', 'Brunéi Darussalam'), ('BG', 'Bulgarie'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodge'), ('CM', 'Cameroun'), ('CA', 'Canada'), ('CV', 'Cap-vert'), ('CL', 'Chili'), ('CN', 'Chine'), ('CY', 'Chypre'), ('CO', 'Colombie'), ('KM', 'Comores'), ('CR', 'Costa Rica'), ('CI', "Côte d'Ivoire"), ('HR', 'Croatie'), ('CU', 'Cuba'), ('DK', 'Danemark'), ('DJ', 'Djibouti'), ('DM', 'Dominique'), ('EG', 'Égypte'), ('SV', 'El Salvador'), ('AE', 'Émirats Arabes Unis'), ('EC', 'Équateur'), ('ER', 'Érythrée'), ('ES', 'Espagne'), ('EE', 'Estonie'), ('FM', 'États Fédérés de Micronésie'), ('US', 'États-Unis'), ('ET', 'Éthiopie'), ('RU', 'Fédération de Russie'), ('FJ', 'Fidji'), ('FI', 'Finlande'), ('GA', 'Gabon'), ('GM', 'Gambie'), ('GE', 'Géorgie'), ('GS', 'Géorgie du Sud et les Îles Sandwich du Sud'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Grèce'), ('GD', 'Grenade'), ('GL', 'Groenland'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GN', 'Guinée'), ('GQ', 'Guinée Équatoriale'), ('GW', 'Guinée-Bissau'), ('GY', 'Guyana'), ('GF', 'Guyane Française'), ('HT', 'Haïti'), ('HN', 'Honduras'), ('HK', 'Hong-Kong'), ('HU', 'Hongrie'), ('BV', 'Île Bouvet'), ('CX', 'Île Christmas'), ('IM', 'Île de Man'), ('NF', 'Île Norfolk'), ('FK', 'Îles (malvinas) Falkland'), ('AX', 'Îles Åland'), ('KY', 'Îles Caïmanes'), ('CC', 'Îles Cocos (Keeling)'), ('CK', 'Îles Cook'), ('FO', 'Îles Féroé'), ('HM', 'Îles Heard et Mcdonald'), ('MP', 'Îles Mariannes du Nord'), ('MH', 'Îles Marshall'), ('UM', 'Îles Mineures Éloignées des États-Unis'), ('SB', 'Îles Salomon'), ('TC', 'Îles Turks et Caïques'), ('VG', 'Îles Vierges Britanniques'), ('VI', 'Îles Vierges des États-Unis'), ('IN', 'Inde'), ('ID', 'Indonésie'), ('IQ', 'Iraq'), ('IE', 'Irlande'), ('IS', 'Islande'), ('IL', 'Israël'), ('IT', 'Italie'), ('LY', 'Jamahiriya Arabe Libyenne'), ('JM', 'Jamaïque'), ('JP', 'Japon'), ('JO', 'Jordanie'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KG', 'Kirghizistan'), ('KI', 'Kiribati'), ('KW', 'Koweït'), ('MK', "L'ex-République Yougoslave de Macédoine"), ('LS', 'Lesotho'), ('LV', 'Lettonie'), ('LB', 'Liban'), ('LR', 'Libéria'), ('LI', 'Liechtenstein'), ('LT', 'Lituanie'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MG', 'Madagascar'), ('MY', 'Malaisie'), ('MW', 'Malawi'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malte'), ('MA', 'Maroc'), ('MQ', 'Martinique'), ('MU', 'Maurice'), ('MR', 'Mauritanie'), ('YT', 'Mayotte'), ('MX', 'Mexique'), ('MC', 'Monaco'), ('MN', 'Mongolie'), ('MS', 'Montserrat'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibie'), ('NR', 'Nauru'), ('NP', 'Népal'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigéria'), ('NU', 'Niué'), ('NO', 'Norvège'), ('NC', 'Nouvelle-Calédonie'), ('NZ', 'Nouvelle-Zélande'), ('OM', 'Oman'), ('UG', 'Ouganda'), ('UZ', 'Ouzbékistan'), ('PK', 'Pakistan'), ('PW', 'Palaos'), ('PA', 'Panama'), ('PG', 'Papouasie-Nouvelle-Guinée'), ('PY', 'Paraguay'), ('NL', 'Pays-Bas'), ('PE', 'Pérou'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Pologne'), ('PF', 'Polynésie Française'), ('PR', 'Porto Rico'), ('PT', 'Portugal'), ('QA', 'Qatar'), ('SY', 'République Arabe Syrienne'), ('CF', 'République Centrafricaine'), ('KR', 'République de Corée'), ('MD', 'République de Moldova'), ('CD', 'République Démocratique du Congo'), ('LA', 'République Démocratique Populaire Lao'), ('DO', 'République Dominicaine'), ('CG', 'République du Congo'), ('IR', "République Islamique d'Iran"), ('KP', 'République Populaire Démocratique de Corée'), ('CZ', 'République Tchèque'), ('TZ', 'République-Unie de Tanzanie'), ('RE', 'Réunion'), ('RO', 'Roumanie'), ('GB', 'Royaume-Uni'), ('RW', 'Rwanda'), ('EH', 'Sahara Occidental'), ('KN', 'Saint-Kitts-et-Nevis'), ('SM', 'Saint-Marin'), ('PM', 'Saint-Pierre-et-Miquelon'), ('VA', 'Saint-Siège (état de la Cité du Vatican)'), ('VC', 'Saint-Vincent-et-les Grenadines'), ('SH', 'Sainte-Hélène'), ('LC', 'Sainte-Lucie'), ('WS', 'Samoa'), ('AS', 'Samoa Américaines'), ('ST', 'Sao Tomé-et-Principe'), ('SN', 'Sénégal'), ('CS', 'Serbie-et-Monténégro'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapour'), ('SK', 'Slovaquie'), ('SI', 'Slovénie'), ('SO', 'Somalie'), ('SD', 'Soudan'), ('LK', 'Sri Lanka'), ('SE', 'Suède'), ('CH', 'Suisse'), ('SR', 'Suriname'), ('SJ', 'Svalbard etÎle Jan Mayen'), ('SZ', 'Swaziland'), ('TJ', 'Tadjikistan'), ('TW', 'Taïwan'), ('TD', 'Tchad'), ('TF', 'Terres Australes Françaises'), ('IO', "Territoire Britannique de l'Océan Indien"), ('PS', 'Territoire Palestinien Occupé'), ('TH', 'Thaïlande'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinité-et-Tobago'), ('TN', 'Tunisie'), ('TM', 'Turkménistan'), ('TR', 'Turquie'), ('TV', 'Tuvalu'), ('UA', 'Ukraine'), ('UY', 'Uruguay'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Viet Nam'), ('WF', 'Wallis et Futuna'), ('YE', 'Yémen'), ('ZM', 'Zambie'), ('ZW', 'Zimbabwe')], default='', max_length=2, verbose_name='pays')),
                ('expertise', models.CharField(blank=True, default='', max_length=50)),
                ('organization', models.CharField(blank=True, default='', max_length=255, verbose_name='Organisation')),
                ('receives_emails', models.BooleanField(default=True, verbose_name='Reçoit les emails')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]