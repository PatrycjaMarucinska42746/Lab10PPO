# Lab10PPO

Zadanie zostało wykonane w języku programowania Python ze względu na zerwanie przyjaźni z Javą na rzecz tego zadania.

Poprawiłam forme zamieszczenia zadania, bo prawdopodobnie to wpłynęło na ocenę negatywną.

Program generuje listę 100 zwierząt, należących 15 gatunków z różnych rodzin/gromad. Program jak jest to wymagane wyświetla wynik w postaci tabeli.


Spis komend do użycia w stworzonym przeze mnie programie i ich opis:

(oczywiście wszystkie i tak zostaną wyświetlone po wpisaniu zapropoowanej przez terminal komendy "help")


~ quit - wyjście z programu

~ list - wyświetlenie wszystkich zwierząt znajdujących się na liście (która po użyciu filtrów zmienia swą zawartość na ich potrzebę)

~ list x - wyświetlenie "x" pierwszych zwierząt z listy ( w miejscu "x" należy dać liczbę dodatnią)

~ count - wyświetlenie liczby zwierząt na liście

~ sort x - sortowanie listy zwierząt według filtra "x" . W tym programie poprawne komendy to:
          sort -name, sort -age, sort -id

~ filter:group x - filtrowanie listy zwierząt według rodziny/gromady. W tym programie poprawne komendy to:
          filter:group -mammal, filter:group -reptile, filter:group -birds, filter:group -snakes

~ filter:species x - (...) według gatunku. W tym programie poprawne komendy to:
          filter:species -lion, filter:species -cat, filter:species -zebra, filter:species -giraffe, filter:species -coala,
          filter:species -elephant, filter:species -gecko, filter:species -iguana, filter:species -agama, filter:species -cameleon,
          filter:species -sparrow, filter:species -penguin, filter:species -parrot, filter:species -anaconda, filter:species -boa

~ filter:gender x - (...) według płci. W moim programie mamy do wyboru tylko m - male i f - female. Komendy jak proszono:
          filter:gender m, filter:gender f

~ filter:age x - (...) według wieku. Przykład komend z liczbą 10:
          filter:age 10 - filtrowanie listy zwierząt aby wyświetlała się następnie lista zwierząt mających 10 lat lub więcej
          filter:age -10 - filtrowanie listy zwierząt aby wyświetlała się następnie lista zwierząt mających 10 lat lub mniej

~ random - wyświetlenie losowo wybranego przez program zwierzęcia z listy

~ clear - zresetowanie zastosowanych filtrów i sortowań

