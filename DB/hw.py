""" 1. Найдите 10 самых часто встречающихся слов. """
# shakespeare_db=# select plaintext, occurences FROM wordform order by occurences desc limit 10; 
#  plaintext | occurences 
# -----------+------------
#  the       |      28932
#  and       |      27296
#  i         |      21120
#  to        |      20136
#  of        |      17169
#  a         |      14943
#  you       |      13989
#  my        |      12950
#  in        |      11512
#  that      |      11487
# (10 rows)

""" 2. Найдите все слова, которые начинаются с буквы ‘a’, регистр не должен иметь
значения.a’, регистр не должен иметь значения."""

# shakespeare_db=# SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';
#      plaintext     
# -------------------
#  and
#  a
#  as
#  all
#  are
#  at
#  am
#  an
#  art
#  away
#  any
#  again
#  ay
#  against
#  aside
#  after
#  about
#  answer
#  another
#  arms
#  antony
#  alone
#  alas
#  age
#  air
#  ah
#  ask
#  almost
#  above
#  arm
#  already
#  appear
#  anon
#  attend
#  act
#  attendants
#  action
#  along
#  awhile
#  angry
#  adieu
#  alive
#  among
#  antonio
#  army
#  achilles
#  angelo
#  ass
#  although
#  amen
#  alack
#  awake
#  anne
#  alarum
#  ancient
#  affection


"""  3. Найдите все произведения,
которые относятся к жанру ‘a’, регистр не должен иметь значения.p’.  """

"""                         Если есть жанр "а" """
# shakespeare_db=# SELECT title FROM work WHERE work.genretype = 'a';
#  title 
# -------
# (0 rows)

"""                         Если жанр "р" """
# shakespeare_db=# SELECT * FROM work WHERE genretype != 'p';
#      workid     |           title           |                 longtitle                 | year | genretype | notes |  source   | totalwords | totalparagraphs 
# ----------------+---------------------------+-------------------------------------------+------+-----------+-------+-----------+------------+-----------------
#  12night        | Twelfth Night             | Twelfth Night, Or What You Will           | 1599 | c         |       | Moby      |      19837 |            1031
#  allswell       | All's Well That Ends Well | All's Well That Ends Well                 | 1602 | c         |       | Moby      |      22997 |            1025
#  antonycleo     | Antony and Cleopatra      | Antony and Cleopatra                      | 1606 | t         |       | Moby      |      24905 |            1344
#  asyoulikeit    | As You Like It            | As You Like It                            | 1599 | c         |       | Gutenberg |      21690 |             872
#  comedyerrors   | Comedy of Errors          | The Comedy of Errors                      | 1589 | c         |       | Moby      |      14692 |             661
#  coriolanus     | Coriolanus                | Coriolanus                                | 1607 | t         |       | Moby      |      27577 |            1226
#  cymbeline      | Cymbeline                 | Cymbeline, King of Britain                | 1609 | h         |       | Moby      |      27565 |             971
#  hamlet         | Hamlet                    | Tragedy of Hamlet, Prince of Denmark, The | 1600 | t         |       | Gutenberg |      30558 |            1275
#  henry4p1       | Henry IV, Part I          | History of Henry IV, Part I               | 1597 | h         |       | Moby      |      24579 |             884
#  henry4p2       | Henry IV, Part II         | History of Henry IV, Part II              | 1597 | h         |       | Gutenberg |      25692 |            1013
#  henry5         | Henry V                   | History of Henry V                        | 1598 | h         |       | Moby      |      26119 |             846
#  henry6p1       | Henry VI, Part I          | History of Henry VI, Part I               | 1591 | h         |       | Moby      |      21575 |             772
#  henry6p2       | Henry VI, Part II         | History of Henry VI, Part II              | 1590 | h         |       | Moby      |      25411 |             904
#  henry6p3       | Henry VI, Part III        | History of Henry VI, Part III             | 1590 | h         |       | Moby      |      24284 |             935
#  henry8         | Henry VIII                | History of Henry VIII                     | 1612 | h         |       | Moby      |      24629 |             779
#  juliuscaesar   | Julius Caesar             | The Tragedy of Julius Caesar              | 1599 | t         |       | Moby      |      19703 |             888
#  kingjohn       | King John                 | History of King John                      | 1596 | h         |       | Moby      |      20760 |             615
#  kinglear       | King Lear                 | The Tragedy of King Lear                  | 1605 | t         |       | Gutenberg |      26119 |            1177
#  loveslabours   | Love's Labour's Lost      | Love's Labour's Lost                      | 1594 | c         |       | Moby      |      21450 |            1120
#  macbeth        | Macbeth                   | The Tragedy of Macbeth                    | 1605 | t         |       | Moby      |      17121 |             758
#  measure        | Measure for Measure       | Measure for Measure                       | 1604 | c         |       | Moby      |      21773 |             980
#  merchantvenice | Merchant of Venice        | Merchant of Venice, The                   | 1596 | c         |       | Moby      |      21291 |             718
#  merrywives     | Merry Wives of Windsor    | Merry Wives of Windsor, The               | 1600 | c         |       | Moby      |      21845 |            1161
#  midsummer      | Midsummer Night's Dream   | A Midsummer Night's Dream                 | 1595 | c         |       | Moby      |      16511 |             603
#  muchado        | Much Ado about Nothing    | Much Ado about Nothing                    | 1598 | c         |       | Moby      |      21157 |            1059
#  othello        | Othello                   | The Tragedy of Othello, Moor of Venice    | 1604 | t         |       | Moby      |      26450 |            1308
#  pericles       | Pericles                  | Pericles, Prince of Tyre                  | 1608 | h         |       | Moby      |      18529 |             748
#  richard2       | Richard II                | History of Richard II                     | 1595 | h         |       | Moby      |      22411 |             628
#  richard3       | Richard III               | History of Richard III                    | 1592 | h         |       | Moby      |      29278 |            1210
#  romeojuliet    | Romeo and Juliet          | The Tragedy of Romeo and Juliet           | 1594 | t         |       | Moby      |      24553 |             989
#  sonnets        | Sonnets                   | Sonnets                                   | 1609 | s         |       | Moby      |      17515 |             154
#  tamingshrew    | Taming of the Shrew       | The Taming of the Shrew                   | 1593 | c         |       | Gutenberg |      21055 |             965
#  tempest        | Tempest                   | The Tempest                               | 1611 | c         |       | Moby      |      16628 |             698
#  timonathens    | Timon of Athens           | The Tragedy of Timon of Athens            | 1607 | t         |       | Moby      |      18206 |             865
#  titus          | Titus Andronicus          | Titus Andronicus                          | 1593 | t         |       | Moby      |      20710 |             654
#  troilus        | Troilus and Cressida      | Troilus and Cressida                      | 1601 | t         |       | Moby      |      26089 |            1295
#  twogents       | Two Gentlemen of Verona   | Two Gentlemen of Verona                   | 1594 | c         |       | Moby      |      17129 |             943
#  winterstale    | The Winter's Tale         | The Winter's Tale                         | 1610 | c         |       | Moby      |      24914 |             812


""" 4. Найдите среднее количество параграфов в произведения жанра ‘a’, регистр не
должен иметь значения.t’. """
# shakespeare_db=# SELECT AVG(totalparagraphs) FROM work WHERE genretype = 't';

#           avg          
# -----------------------
#  1070.8181818181818182
# (1 row)



""" 5. Выведите все произведения, в которых количество слов выше среднего. """
# shakespeare_db=# SELECT title FROM work WHERE (SELECT AVG(totalwords) FROM work) < totalwords
# shakespeare_db-# ;
#            title           
# ---------------------------
#  All's Well That Ends Well
#  Antony and Cleopatra
#  As You Like It
#  Coriolanus
#  Cymbeline
#  Hamlet
#  Henry IV, Part I
#  Henry IV, Part II
#  Henry V
#  Henry VI, Part I
#  Henry VI, Part II
#  Henry VI, Part III
#  Henry VIII
#  King John
#  King Lear
#  Love's Labour's Lost
#  Measure for Measure
#  Merchant of Venice
#  Merry Wives of Windsor
#  Much Ado about Nothing
#  Othello
#  Richard II
#  Richard III
#  Romeo and Juliet
#  Taming of the Shrew
#  Titus Andronicus
#  Troilus and Cressida
#  The Winter's Tale
# (28 rows)


""" 6. Выведите имя героя, количество его реплик, и произведение, в котором
этот герой встречается. """
# SELECT c1.charname, c1.speechcount, w.title
# FROM character c1
# JOIN character_work c2 ON c1.charid = c2.charid
# JOIN work w ON w.workid = c2.workid;

#                 charname                 | speechcount |           title           
# ------------------------------------------+-------------+---------------------------
#  First Apparition                         |           1 | Macbeth
#  First Citizen                            |           3 | Romeo and Juliet
#  First Conspirator                        |           3 | Coriolanus
#  First Gentleman                          |           1 | Othello
#  First Goth                               |           4 | Titus Andronicus
#  First Murderer                           |          21 | Macbeth
#  First Musician                           |           5 | Othello
#  First Musician                           |          10 | Romeo and Juliet
#  First Officer                            |           3 | Othello
#  First Player                             |           8 | Hamlet
#  First Senator                            |          33 | Coriolanus
#  First Senator                            |           8 | Othello
#  First Servant                            |           4 | Romeo and Juliet
#  First Serving-Man                        |           5 | Henry VI, Part I
#  First Soldier                            |           8 | Coriolanus
#  First Watchman                           |           6 | Much Ado about Nothing
#  First Watchman                           |           6 | Romeo and Juliet
#  First Witch                              |          23 | Macbeth
#  Second Apparition                        |           2 | Macbeth
#  Second Conspirator                       |           2 | Coriolanus
#  Second Gentleman                         |           5 | Othello
#  Second Goth                              |           1 | Titus Andronicus
#  Second Murderer                          |           6 | Macbeth
#  Second Musician                          |           3 | Romeo and Juliet
#  Second Patrician                         |           1 | Coriolanus
#  Second Senator                           |          10 | Coriolanus
#  Second Senator                           |           1 | Othello
#  Second Servant                           |           6 | Romeo and Juliet
#  Second Serving-Man                       |           2 | Henry VI, Part I
#  Second Soldier                           |           1 | Coriolanus
#  Second Watchman                          |           5 | Much Ado about Nothing
#  Second Watchman                          |           1 | Romeo and Juliet
#  Second Witch                             |          15 | Macbeth
#  Third Apparition                         |           1 | Macbeth
#  Third Gentleman                          |           4 | Othello
#  Third Goth                               |           1 | Titus Andronicus
#  Third Murderer                           |           6 | Macbeth
#  Third Musician                           |           1 | Romeo and Juliet
#  Third Serving-Man                        |           2 | Henry VI, Part I
#  Third Watchman                           |           1 | Romeo and Juliet
#  Third Witch                              |          13 | Macbeth
#  Fourth Gentleman                         |           1 | Othello
#  Aaron                                    |          57 | Titus Andronicus

"""7. Выведите среднее количество реплик героев в произведении,
регистр не должен иметь значения.Romeo and Juliet’"""

# SELECT AVG (c1.speechcount) 
# FROM character c1 
# JOIN character_work c2 ON c2.charid = c1.charid 
# JOIN work w ON w.workid = c2.workid 
# WHERE w.title = 'Romeo and Juliet';
#          avg         
# ---------------------
#  25.5454545454545455
# (1 row)

""" 8. Выведите общее
количество слов в каждой из секций в таблице paragraph """


# shakespeare_db=# SELECT count(plaintext) + count(phonetictext) + count(stemtext) as total FROM paragraph; 
#  total  
# --------
#  106395
# (1 row)

""" 9. Выведите
всех героев, которые имеют от 15 до 30 реплик. """

# SELECT c1.charname 
# FROM character c1 
# JOIN character_work c2 ON c2.charid = c1.charid 
# JOIN work w ON w.workid = c2.workid 
# WHERE 15 < c1.speechcount and 30 > c1.speechcount;

""" 10. Выведите все произведения, которые были написаны в 17 веке """
# shakespeare_db=# SELECT title from work WHERE year >= 1601 AND year <= 1700;
#            title           
# ---------------------------
#  All's Well That Ends Well
#  Antony and Cleopatra
#  Coriolanus
#  Cymbeline
#  Henry VIII
#  King Lear
#  Lover's Complaint
#  Macbeth
#  Measure for Measure
#  Othello
#  Pericles
#  Phoenix and the Turtle
#  Sonnets
#  Tempest
#  Timon of Athens
#  Troilus and Cressida
#  The Winter's Tale
# (17 rows)

""" 11. Найдите все произведения, которые имею в полном названии
слово ‘a’, регистр не должен иметь значения.the’ """
# shakespeare_db=#  SELECT title FROM work WHERE work.longtitle ILIKE '%the%';
#          title          
# ------------------------
#  Comedy of Errors
#  Hamlet
#  Julius Caesar
#  King Lear
#  Macbeth
#  Merchant of Venice
#  Merry Wives of Windsor
#  Othello
#  Passionate Pilgrim
#  Phoenix and the Turtle
#  Rape of Lucrece
#  Romeo and Juliet
#  Taming of the Shrew
#  Tempest
#  Timon of Athens
#  The Winter's Tale
# (16 rows)

""" 12. Выведите все уникальные секции в paragraph """
# shakespeare_db=# SELECT DISTINCT section FROM paragraph;
#  section 
# ---------
#        0
#        1
#        3
#        5
#        4
#        2
# (6 rows)


""" 13. Для каждой главы выведите: id, описание и название произведения, к которой
относится данная глава. """

# shakespeare_db=# SELECT c.chapterid, c.description, w.title 
# FROM chapter c 
# JOIN work w ON w.workid = c.workid; 

#  chapterid |                                       description                                        |           title           
# -----------+------------------------------------------------------------------------------------------+---------------------------
#      18934 | Prologue.                                                                                | Henry V
#      18704 | DUKE ORSINO's palace.                                                                    | Twelfth Night
#      18705 | The sea-coast.                                                                           | Twelfth Night
#      18706 | OLIVIA'S house.                                                                          | Twelfth Night
#      18707 | DUKE ORSINO's palace.                                                                    | Twelfth Night
#      18708 | OLIVIA'S house.                                                                          | Twelfth Night
#      18709 | The sea-coast.                                                                           | Twelfth Night
#      18710 | A street.                                                                                | Twelfth Night
#      18711 | OLIVIA's house.                                                                          | Twelfth Night
#      18712 | DUKE ORSINO's palace.                                                                    | Twelfth Night
#      18713 | OLIVIA's garden.                                                                         | Twelfth Night
#      18714 | OLIVIA's garden.                                                                         | Twelfth Night
#      18715 | OLIVIA's house.                                                                          | Twelfth Night
#      18716 | A street.                                                                                | Twelfth Night
#      18717 | OLIVIA's garden.                                                                         | Twelfth Night
#      18718 | Before OLIVIA's house.                                                                   | Twelfth Night
#      18719 | OLIVIA's house.                                                                          | Twelfth Night
#      18720 | OLIVIA's garden.                                                                         | Twelfth Night
#      18721 | Before OLIVIA's house.                                                                   | Twelfth Night
#      18722 | Rousillon. The COUNT's palace.                                                           | All's Well That Ends Well
#      18723 | Paris. The KING's palace.                                                                | All's Well That Ends Well
#      18724 | Rousillon. The COUNT's palace.                                                           | All's Well That Ends Well
#      18725 | Paris. The KING's palace.                                                                | All's Well That Ends Well
#      18726 | Rousillon. The COUNT's palace.                                                           | All's Well That Ends Well
#      18727 | Paris. The KING's palace.                                                                | All's Well That Ends Well
#      18728 | Paris. The KING's palace.                                                                | All's Well That Ends Well


""" 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество
реплик героя """
# SELECT p.paragraphnum, c1.charname, c1.speechcount 
# FROM character c1 
# JOIN paragraph p ON c1.charid = p.charid;  


#  paragraphnum |                 charname                 | speechcount 
# --------------+------------------------------------------+-------------
#             3 | (stage directions)                       |         126
#             4 | Orsino                                   |          59
#            19 | Curio                                    |           4
#            20 | Orsino                                   |          59
#            21 | Curio                                    |           4
#            22 | Orsino                                   |          59
#            30 | Valentine                                |           3
#            39 | Orsino                                   |          59
#            48 | (stage directions)                       |         126
#            50 | (stage directions)                       |         126
#            51 | Viola                                    |         121
#            52 | Captain                                  |          10
#            53 | Viola                                    |         121
#            56 | Captain                                  |          10
#            57 | Viola                                    |         121
#            58 | Captain                                  |          10
#           187 | Sir Andrew Aguecheek                     |          88
#            68 | Viola                                    |         121
#            72 | Captain                                  |          10
#            74 | Viola                                    |         121


""" 15. Для каждого параграфа выведите: номер параграфа, название произведения и
год выхода этого произведения. """

# SELECT p.paragraphnum, w.title, w.year 
# FROM paragraph p 
# JOIN work w ON w.workid = p.workid; 

#  paragraphnum |           title           | year 
# --------------+---------------------------+------
#             3 | Twelfth Night             | 1599
#             4 | Twelfth Night             | 1599
#            19 | Twelfth Night             | 1599
#            20 | Twelfth Night             | 1599
#            21 | Twelfth Night             | 1599
#            22 | Twelfth Night             | 1599
#            30 | Twelfth Night             | 1599
#            39 | Twelfth Night             | 1599
#            48 | Twelfth Night             | 1599
#            50 | Twelfth Night             | 1599
#            51 | Twelfth Night             | 1599
#            52 | Twelfth Night             | 1599
#            53 | Twelfth Night             | 1599
#            56 | Twelfth Night             | 1599
#            57 | Twelfth Night             | 1599
#            58 | Twelfth Night             | 1599
#           187 | Twelfth Night             | 1599
#            68 | Twelfth Night             | 1599
#            72 | Twelfth Night             | 1599


"""  1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100 """

# select * from work where source = 'Moby' and totalparagraphs < 100;
#       workid       |         title          |         longtitle          | year | genretype | notes | source | totalwords | totalparagraphs 
# -------------------+------------------------+----------------------------+------+-----------+-------+--------+------------+-----------------
#  loverscomplaint   | Lover's Complaint      | A Lover's Complaint        | 1609 | p         |       | Moby   |       2559 |              47
#  passionatepilgrim | Passionate Pilgrim     | The Passionate Pilgrim     | 1598 | p         |       | Moby   |       3124 |              43
#  phoenixturtle     | Phoenix and the Turtle | The Phoenix and the Turtle | 1601 | p         |       | Moby   |        353 |              19
# (3 rows)


""" 2. Найти кол-во глав в каждом произведении """
# select distinct w.title, sum(c.chapter) from work w join chapter c on c.workid = w.workid group by w.title;
#            title           |  sum  
# ---------------------------+-------
#  Henry VI, Part II         |    87
#  Antony and Cleopatra      |   257
#  Henry IV, Part II         |    50
#  Merry Wives of Windsor    |    67
#  Much Ado about Nothing    |    40
#  Pericles                  |    62
#  King John                 |    46
#  Sonnets                   | 11935
#  Lover's Complaint         |     1
#  Comedy of Errors          |    20
#  Romeo and Juliet          |    73
#  Henry VIII                |    41
#  Timon of Athens           |    43
#  Merchant of Venice        |    70
#  Measure for Measure       |    45
#  All's Well That Ends Well |    70
#  Richard II                |    52
#  Henry IV, Part I          |    47
#  Twelfth Night             |    47
#  Cymbeline                 |    89
#  As You Like It            |    65
#  Henry VI, Part I          |    89
#  Coriolanus                |   115
#  Titus Andronicus          |    30
#  Henry VI, Part III        |   101
#  Henry V                   |    81
#  King Lear                 |    87
#  Troilus and Cressida      |    88
#  Phoenix and the Turtle    |     1
#  Julius Caesar             |    43
#  The Winter's Tale         |    31
#  Taming of the Shrew       |    28
#  Hamlet                    |    59
#  Richard III               |    78
#  Rape of Lucrece           |     3
#  Venus and Adonis          |     1
#  Midsummer Night's Dream   |    13
#  Tempest                   |    14
#  Passionate Pilgrim        |   231
#  Love's Labour's Lost      |    14
#  Two Gentlemen of Verona   |    57
#  Macbeth                   |   101
#  Othello                   |    31


""" 3. Найти сколько произведений относятся к каждому  """


""" # 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений """

# select title, totalparagraphs from work;

#            title           | totalparagraphs 
# ---------------------------+-----------------
#  Twelfth Night             |            1031
#  All's Well That Ends Well |            1025
#  Antony and Cleopatra      |            1344
#  As You Like It            |             872
#  Comedy of Errors          |             661
#  Coriolanus                |            1226
#  Cymbeline                 |             971
#  Hamlet                    |            1275
#  Henry IV, Part I          |             884
#  Henry IV, Part II         |            1013
#  Henry V                   |             846
#  Henry VI, Part I          |             772
#  Henry VI, Part II         |             904
#  Henry VI, Part III        |             935
#  Henry VIII                |             779
#  Julius Caesar             |             888
#  King John                 |             615
#  King Lear                 |            1177
#  Lover's Complaint         |              47
#  Love's Labour's Lost      |            1120
#  Macbeth                   |             758
#  Measure for Measure       |             980
#  Merchant of Venice        |             718
#  Merry Wives of Windsor    |            1161
#  Midsummer Night's Dream   |             603
#  Much Ado about Nothing    |            1059
#  Othello                   |            1308
#  Passionate Pilgrim        |              43
#  Pericles                  |             748
#  Phoenix and the Turtle    |              19
#  Rape of Lucrece           |             269
#  Richard II                |             628
#  Richard III               |            1210
#  Romeo and Juliet          |             989
#  Sonnets                   |             154
#  Taming of the Shrew       |             965
#  Tempest                   |             698
#  Timon of Athens           |             865
#  Titus Andronicus          |             654
#  Troilus and Cressida      |            1295
#  Two Gentlemen of Verona   |             943
#  Venus and Adonis          |             201
#  The Winter's Tale         |             812
# (43 rows)

""" # 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания """
# SELECT c1.charname, w.title, w.genretype, w.year 
# FROM character c1 
# JOIN charaCter_work c2 ON c1.charid = c2.charid 
# JOIN work w ON w.workid = c2.workid 
# WHERE c1.speechcount > 200 
# ORDER BY w.year; 
#       charname      |         title          | genretype | year 
# --------------------+------------------------+-----------+------
#  Richard III        | Henry VI, Part III     | h         | 1590
#  Duke of Gloucester | Henry VI, Part II      | h         | 1590
#  Duke of Gloucester | Henry VI, Part I       | h         | 1591
#  Duke of Gloucester | Richard III            | h         | 1592
#  Richard III        | Richard III            | h         | 1592
#  Poet               | Venus and Adonis       | p         | 1593
#  Poet               | Rape of Lucrece        | p         | 1594
#  Falstaff           | Henry IV, Part I       | h         | 1597
#  Henry V            | Henry IV, Part II      | h         | 1597
#  Henry V            | Henry IV, Part I       | h         | 1597
#  Falstaff           | Henry IV, Part II      | h         | 1597
#  Henry V            | Henry V                | h         | 1598
#  Falstaff           | Henry V                | h         | 1598
#  Duke of Gloucester | Henry V                | h         | 1598
#  Poet               | Passionate Pilgrim     | p         | 1598
#  Antony             | Julius Caesar          | t         | 1599
#  Rosalind           | As You Like It         | c         | 1599
#  Hamlet             | Hamlet                 | t         | 1600
#  Falstaff           | Merry Wives of Windsor | c         | 1600
#  Poet               | Phoenix and the Turtle | p         | 1601
#  Iago               | Othello                | t         | 1604
#  Othello            | Othello                | t         | 1604
#  Cleopatra          | Antony and Cleopatra   | t         | 1606
#  Antony             | Antony and Cleopatra   | t         | 1606
#  Timon              | Timon of Athens        | t         | 1607
#  Poet               | Sonnets                | s         | 1609
#  Poet               | Lover's Complaint      | p         | 1609
# (27 rows)


""" # 6. Вытащить героя, который чаще всех появляется в произведениях """
# select count(charname), charname from character group by charname order by count desc;

#  count |                 charname                 
# -------+------------------------------------------
#     23 | All
#     23 | Messenger
#     21 | Servant
#      9 | Lord
#      8 | Page
#      8 | First Gentleman
#      8 | First Lord
#      8 | Second Gentleman
#      7 | Both
#      7 | First Servant
#      7 | Captain
#      7 | Gentleman
#      6 | Second Servant
#      6 | Second Lord



