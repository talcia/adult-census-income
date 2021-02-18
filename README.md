# Projekt

Celem projektu jest zastosowanie technik zgłębianiadanych / uczenia maszynowego, ze szczególnym wskazaniem na algorytmy
klasyfikujące na wybranej bazie danych. Projket został wykonany w Pythonie z zastosowaniem biblioteki Keras oraz sklearn.

## Spis treści

-   Opis projektu
-   Badanie i obróbka bazy danych 
-   Porównanie poznanych klasyfikatorów
-   Rozszerzona klasyfikacja i inne techniki

## Badanie i obróbka bazy danych:
Baza danych Adult Census income stworzona została przez Ronny’ego Kohavi’ego oraz Barry’ego Becker’a. Zawiera ona informacje pobrane z bazy danych Biura Spisu Ludności.
Zawiera 48842 rekordy oraz 14 poszczególnych kolumn:
1. Kolumna: age

min: 17, max: 90

średnia: 38.64

brakujące dane: 0.0%

![column1](https://github.com/talcia/adult-census-income/blob/main/assets/age.png)

2. Kolumna: workclass

brakujące dane: 0.057%

![column2](https://github.com/talcia/adult-census-income/blob/main/assets/workclass.png)

3. Kolumna: fnlwgt

min: 12285, max: 1490400

średnia: 189664,14

brakujące dane: 0.0%

![column3](https://github.com/talcia/adult-census-income/blob/main/assets/fnlwgt.png)

4. Kolumna: education

brakujące dane: 0.0%

![column4](https://github.com/talcia/adult-census-income/blob/main/assets/education.png)

5. Kolumna: education-num

min: 1, max: 16

średnia: 10.08

brakujące dane: 0.0%

![column5](https://github.com/talcia/adult-census-income/blob/main/assets/education-num.png)

6. Kolumna: martial-status

brakujące dane: 0.0%

![column6](https://github.com/talcia/adult-census-income/blob/main/assets/martial-status.png)

7. Kolumna: occupation

brakujące dane: 0.056%

![column7](https://github.com/talcia/adult-census-income/blob/main/assets/occupation.png)

8. Kolumna: relationship

brakujące dane: 0.0%

![column8](https://github.com/talcia/adult-census-income/blob/main/assets/relationship.png)

9. Kolumna: race

brakujące dane: 0.0%

![column9](https://github.com/talcia/adult-census-income/blob/main/assets/race.png)

10. Kolumna: sex

brakujące dane: 0.0%

![column10](https://github.com/talcia/adult-census-income/blob/main/assets/sex.png)

11. Kolumna: capital-gain

min: 0, max: 999999

średnia: 1079,07

brakujące dane: 0.0%

![column11](https://github.com/talcia/adult-census-income/blob/main/assets/capitalgain.png)

12. Kolumna: capital-loss

min: 0, max: 4356

średnia: 1079,07

brakujące dane: 0.0%

![column12](https://github.com/talcia/adult-census-income/blob/main/assets/capitalloss.png)

13. Kolumna: house per week

min: 1, max: 99

średnia: 40.42

brakujące dane: 0.0%

![column13](https://github.com/talcia/adult-census-income/blob/main/assets/houseperweek.png)

14. Kolumna: native-country

brakujące dane: 0.018%

![column14](https://github.com/talcia/adult-census-income/blob/main/assets/native-country.png)

Wiersze zawierające brakujące dane zostały usunięte. Po ich usunięciu w bazie danychznajdowało się 46033 rekordów.

Kilka kolumn zostało usuniętych ze względu na brak istotnych danych. Są to kolumny: fnlwgt
(średnia wartość), capitalgain (zysk kapitałowy – większość danych zawiera 0), capitalloss
(strata kapitału – większość danych zawiera 0), native-country(ponad 95% danych zawiera
jedną wartość), education (ponieważ te same dane są zawarte w education-num).

Kilka kolumn zostało zmodyfikowanych w celu ułatwienia przeprowadzenia klasyfikacji oraz
odczytywania danych. Są to kolumny zawierające informacje o klasie roboczej, zawodzie,
stanie cywilnym oraz rasie. Stan kolumn po modyfikacjach przedstawiony poniżej.

Kolumny zawierające informacje o klasie robotniczej, zawodzie i relacji zostały zamienione
na wartości numeryczne za pomocą funkcji pd.get_dummies.

Natomiast kolumny zawierające informacje o płci, klasie (czy zarabia więcej niż 50k czy nie, 1
jeśli tak 0 jeśli nie), stanie cywilnym oraz rasie zostały zamienione na wartości numeryczne
zapisując 1 jako wartość częściej występująca oraz 0 jako druga wartość.

### Informacje o kolumnach po modyfikacjach:

![column2](https://github.com/talcia/adult-census-income/blob/main/assets/workclass2.png)

![column7](https://github.com/talcia/adult-census-income/blob/main/assets/occupation2.png)

![column6](https://github.com/talcia/adult-census-income/blob/main/assets/martial-status2.png)

![column9](https://github.com/talcia/adult-census-income/blob/main/assets/race2.png)

## Porównanie poznanych klasyfikatorów

Klasyfikacja wykonywana jest na podstawie kolumny 15 zawierającej informacje czy przychód roczny jest większy od 50k czy nie.

Zbiór treningowy zawiera 70% rekordów bazy danych, natomiast zbiór testowy 30%.

![classification](https://github.com/talcia/adult-census-income/blob/main/assets/algs.png)

![times](https://github.com/talcia/adult-census-income/blob/main/assets/times.png)

Drzewa decyzyjne – 79%

Naiwny Bayes – 73%

K najbliższych sąsiadów 3 – 79%

Sieci neuronowe – 84%


## Rozszerzona klasyfikacja i inne techniki

***Random Forest*** - będące uogólnieniem idei drzew decyzyjnych zalicza się do procedur agregujących.
Działanie lasów losowych polega na klasyfikacji za pomocą grupy drzew decyzyjnych. Końcowa
decyzja jest podejmowana w wyniku głosowania większościowego nad klasami wskazanymi przez
poszczególne drzewa decyzyjne.

***SVM*** - realizuje zadania klasyfikacyjne konstruując w wielowymiarowej przestrzeni hiperpłaszczyzny
oddzielające przypadki należące do różnych klas. Dla każdej zmiennej skategoryzowanej tworzony
jest zestaw zmiennych z kodami określającymi przynależność każdego przypadku (0 lub 1).
Optymalną hiperpłaszczyznę separującą buduje się w iteracyjnym algorytmie uczącym,
minimalizującym pewną funkcję błędu.

Drzewa decyzyjne – 79%

Naiwny Bayes – 73%

K najbliższych sąsiadów 3 – 80.07%

K najbliższych sąsiadów 5 – 80.65%

K najbliższych sąsiadów 7 – 81%

Sieci neuronowe – 84%

SVM – 82.5%

Random Forest – 80.5%


![classification](https://github.com/talcia/adult-census-income/blob/main/assets/algs2.png)

![times](https://github.com/talcia/adult-census-income/blob/main/assets/times2.png)


## Macierze błędów przetestowanych algorytmów

![confusion_matrix](https://github.com/talcia/adult-census-income/blob/main/assets/cm.png)

