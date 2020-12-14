unedited_text = input().split()

"""Wenn Du mich ein wenig kennst, dann weißt Du, dass ich eine Leseratte bin. So nennt man einen 
Menschen, 
der gerne Bücher liest. Ich liebe Bücher. Und daher habe ich hier in Slow German auch schon oft über deutsche 
Literatur gesprochen. Zum Beispiel über Hermann Hesse, Heinrich Heine oder Schiller und Goethe. Eine große Figur habe 
ich bislang ausgelassen, und das hole ich heute nach: Thomas Mann. Thomas Mann wurde 1875 in Lübeck geboren, 
das liegt im Norden von Deutschland. Sein Vater war ein Kaufmann. In der Schule war Thomas nicht gut, er blieb sitzen 
und schrieb auch in Deutsch schlechte Noten. Aber er schrieb schon als Teenager gerne Geschichten. Nach dem Tod des 
Vaters wurde die Firma verkauft. Der Vater hatte im Testament angeordnet, dass das geschieht. Offenbar traute er 
seinen Söhnen nicht zu, das Unternehmen weiterzuführen. 

Also zog die Mutter mit ihren Kindern nach München. Thomas arbeitete in einem Büro und langweilte sich. Er hatte 
Glück und seine erste Novelle wurde 1894 veröffentlicht. Der Erfolg tat ihm gut: Er kündigte seinen Job und ging mit 
seinem Bruder nach Italien. 1901 folgte dann Manns erster Roman: „Buddenbrooks“. Es ist die Geschichte einer Familie. 
Thomas Mann verarbeitet darin die Geschichte seiner eigenen Familie und anderer Menschen, die er aus Lübeck kannte. 
Das Buch ist so erfolgreich, dass Thomas Mann ab jetzt keine finanzielle Unterstützung seiner Familie mehr braucht. 
28 Jahre später bekam er für dieses Buch den Nobelpreis für Literatur. Es gilt als ein wichtiges Werk der 
Weltliteratur. 

Thomas Mann heiratete und bekam mit seiner Frau sechs Kinder. Heute werden ihm „homoerotische Neigungen“ 
zugeschrieben, aber wahrscheinlich war die Zeit einfach noch nicht reif, um diese auch offen zu leben. Seine Frau 
Katia unterstützt ihn sehr. Die Kinder sagen später, dass es eine glückliche Ehe war. 

Sein Roman „Der Zauberberg“ wurde ein großer Erfolg. Als Hitler an die Macht kam war Thomas Mann ein wichtiger Gegner 
des Nationalsozialismus. Er nannte ihn barbarisch. Die Nazis nahmen den Manns Großteile ihres Vermögens weg, 
später auch die deutsche Staatsbürgerschaft. Der Schriftsteller rief jeden Monat über die BBC die Deutschen zum 
Widerstand auf. 

Die Familie emigrierte zuerst nach Frankreich und dann in die Schweiz. 1938 zogen sie dann endgültig in die USA. Es 
war schwer für die Familie, ihre Heimat zu verlassen. Thomas Mann fühlte sich entwurzelt, sagte aber in einem 
Interview mit der New York Times: „Wo ich bin, ist Deutschland. Ich trage meine deutsche Kultur in mir.“ Er arbeitete 
sehr diszipliniert. Jeden Vormittag schrieb er drei Stunden lang, dann machte er einen Spaziergang und aß zu Mittag. 
Danach widmete er sich Recherchen für neue Projekte und nach einer kleinen Pause schrieb er Briefe. Abends wurde erst 
gegessen, dann las er seiner Familie vor, was er vormittags geschrieben hatte. 

1952 zog er wieder in die Schweiz zurück. Dort starb er im Alter von 80 Jahren.

Insgesamt hat Thomas Mann acht Romane geschrieben. Schon zu seinen Lebzeiten war er sehr erfolgreich. Aber nicht alle 
mochten ihn. Viele Leser warfen ihm vor, zu intellektuell zu sein. Manchen war er zu deutsch oder zu bürgerlich. Ich 
habe seine Bücher sehr gerne gelesen, aber man braucht Zeit dafür: Der Zauberberg beispielsweise ist über 1000 Seiten 
lang. """

LIST_OF_PUNCTUATION_MARKS = [',', '.', ':', ';', '(', ')', '"', '“', '„']

LIST_OF_ARTICLES = ['der', 'das', 'die', 'den', 'dem', 'des', 'denen', 'ein', 'eine', 'einen', 'einer', 'einem',
                    'eines']

LIST_OF_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def remove_punctuation_marks(text):
    """удаление знаков пунктуации из текста / """
    edited_text = text.strip(''.join(LIST_OF_PUNCTUATION_MARKS))
    return edited_text


def remove_numbers(text):
    """Удаление цифер"""
    edited_text = text.strip(''.join(LIST_OF_NUMBERS))
    return edited_text


def remove_unnecessary_words(text):
    """удаление ненужных слов (например артиклей, союзов, часто встречающихся слов)"""
    edited_text = text.strip(''.join(LIST_OF_ARTICLES))
    return edited_text


text_after_editing = remove_punctuation_marks(unedited_text)
text_after_editing = remove_numbers(unedited_text)
text_after_editing = remove_unnecessary_words(unedited_text)

print(text_after_editing)