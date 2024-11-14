# Aplikacja do Generowania Struktury HTML z Treści Artykułu przy użyciu API OpenAI

## Opis projektu
Aplikacja jest narzędziem do przetwarzania tekstu artykułu na odpowiednią strukturę HTML przy użyciu OpenAI API. Główne funkcje aplikacji obejmują:

1. Łączenie się z API OpenAI.
2. Przetwarzanie tekstu artykułu na kod HTML.
3. Strukturyzację treści z odpowiednim użyciem tagów HTML oraz wskazanie miejsc na grafiki.
4. Zapis wygenerowanego kodu HTML do pliku artykul.html bez CSS ani JavaScript.
   
W pliku szablon.html znajdują się style i skrypty do podglądu wygenerowanej treści, a podglad.html pozwala na pełny podgląd artykułu.

## Instalacja
- Upewnij się, że masz zainstalowane środowisko Python (w moim przypadku 3.11.4).
- Zainstaluj bibliotekę openai, aby połączyć się z API: pip install openai

## Klucz API OpenAI:
- Wymagany jest klucz API, który można uzyskać, rejestrując się na stronie OpenAI.
- Dodaj klucz API (na potrzeby zadania można go dodoać w kodzie, ale zalacene jest aby ustwić go jako zmienną środowiskową dla bezpieczeństwa).

## Uruchomienie aplikacji:
- Stwórz plik tekstowy artykul.txt w katalogu projektu, który będzie zawierał treść artykułu do przetworzenia.
- Aby wygenerować strukturę HTML, uruchom skrypt (w moim przyadku jest plik nazywa się "app.py"): python app.py

##Podgląd wygenerowanego artykułu:
Aby wyświetlić artykuł z użyciem stylów i animacji, otwórz plik podglad.html w przeglądarce, wklejając wygenerowany kod HTML do sekcji <body>.

# Ciekawostki

![image](https://github.com/user-attachments/assets/c5feac26-1ab7-4934-88f5-7cda42b3e9c4)

## Wybór Modelu
W API OpenAI można wybrać różne modele w zależności od potrzeb aplikacji. W tym projekcie wykorzystano model gpt-3.5-turbo, który jest efektywny kosztowo i dobrze sprawdza się w generowaniu tekstu HTML. Modele takie jak gpt-4 są dostępne, ale ich użycie jest droższe. Wybór modelu powinien być dostosowany do wymagań zadania i budżetu.

## Parametry API
OpenAI API pozwala na dostosowanie kilku parametrów, które wpływają na sposób generowania odpowiedzi. Oto niektóre z najważniejszych:

-Temperature: Kontroluje „kreatywność” odpowiedzi. Wartość od 0 do 1; niższe wartości powodują bardziej przewidywalne odpowiedzi, a wyższe wartości – bardziej losowe. Przykładowo, wartość 0.7 może być odpowiednia dla zadań kreatywnych, podczas gdy 0.2 lepiej sprawdzi się w generowaniu bardziej przewidywalnych odpowiedzi.
- Max Tokens: Określa maksymalną liczbę tokenów w generowanej odpowiedzi. Tokeny to jednostki tekstowe (słowa lub części słów). Zwiększenie tej wartości pozwala na dłuższe odpowiedzi, ale może wpływać na koszt.
- Top-p (nucleus sampling): Alternatywa dla temperatury, ogranicza odpowiedź do najwyżej ocenianych tokenów. Wartość 0.9 oznacza, że model wybiera spośród tokenów, które stanowią 90% prawdopodobieństwa całkowitego.
- Frequency Penalty: Określa, jak bardzo model ma karać za powtarzanie tych samych zdań czy fraz. Wartość wyższa niż 0 powoduje, że model unika powtórzeń.
- Presence Penalty: Zmniejsza prawdopodobieństwo powtarzania już wspomnianych tematów, co jest przydatne do uzyskiwania bardziej zróżnicowanych odpowiedzi.

Dokumentacja
Więcej informacji o modelach i dostępnych parametrach można znaleźć w dokumentacji OpenAI:
- https://platform.openai.com/docs/models
- https://platform.openai.com/docs/api-reference/realtime-server-events 
