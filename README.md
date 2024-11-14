**Aplikacja do Generowania Struktury HTML z Treści Artykułu przy użyciu API OpenAI

*Opis projektu
Aplikacja jest narzędziem do przetwarzania tekstu artykułu na odpowiednią strukturę HTML przy użyciu OpenAI API. Główne funkcje aplikacji obejmują:

1. Łączenie się z API OpenAI.
2. Przetwarzanie tekstu artykułu na kod HTML.
3. Strukturyzację treści z odpowiednim użyciem tagów HTML oraz wskazanie miejsc na grafiki.
4. Zapis wygenerowanego kodu HTML do pliku artykul.html bez CSS ani JavaScript.
   
W pliku szablon.html znajdują się style i skrypty do podglądu wygenerowanej treści, a podglad.html pozwala na pełny podgląd artykułu.

*Instalacja
- Upewnij się, że masz zainstalowane środowisko Python (w moim przypadku 3.11.4).
- Zainstaluj bibliotekę openai, aby połączyć się z API: pip install openai

*Klucz API OpenAI:
- Wymagany jest klucz API, który można uzyskać, rejestrując się na stronie OpenAI.
- Dodaj klucz API (na potrzeby zadania można go dodoać w kodzie, ale zalacene jest aby ustwić go jako zmienną środowiskową dla bezpieczeństwa).

*Uruchomienie aplikacji:
- Stwórz plik tekstowy artykul.txt w katalogu projektu, który będzie zawierał treść artykułu do przetworzenia.
- Aby wygenerować strukturę HTML, uruchom skrypt (w moim przyadku jest plik nazywa się "app.py"): python app.py

*Podgląd wygenerowanego artykułu:
Aby wyświetlić artykuł z użyciem stylów i animacji, otwórz plik podglad.html w przeglądarce, wklejając wygenerowany kod HTML do sekcji <body>.
