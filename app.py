from openai import OpenAI

# Wprowadź swój klucz API OpenAI
client = OpenAI(api_key = 'Tutaj wprowadź swój klucz API OpenAI')
# Treść artykułu z pliku
with open('artykul.txt', 'r', encoding='utf-8') as file:
    article_content = file.read()

# Prompt i artykuł dla modelu OpenAI
prompt = f"""
Przetwórz poniższy artykuł, strukturyzując go za pomocą odpowiednich tagów HTML zgodnie z najlepszymi praktykami. Upewnij się, że:

- **Tagi są poprawnie zagnieżdżone i hierarchia dokumentu jest zachowana.**
- **Zachowujesz profesjonalizm w kodzie i poprawne użycie tagów.**
- **Cała treść artykułu została uwzględniona w wygenerowanym kodzie HTML.**

Określ miejsca, w których warto wstawić grafiki, oznaczając je za pomocą tagu `<img>` z atrybutem `src="image_placeholder.jpg"`. Dodaj atrybut `alt` do każdego obrazka z dokładnym i rozbudowanym opisem (promptem), który można użyć do wygenerowania grafiki. Opisy w atrybutach `alt` powinny być szczegółowe i zawierać:

- **Elementy wizualne**: kto lub co jest na obrazku, co robi
- **Otoczenie i tło**: gdzie dzieje się scena, jakie są szczegóły otoczenia
- **Emocje i atmosfera**: nastrój sceny, emocje postaci
- **Kolory i styl graficzny**: dominujące kolory, czy jest to styl fotorealistyczny, komiksowy, minimalistyczny, itp.

Umieść obrazki i ich podpisy wewnątrz tagu `<figure>`, a krótkie podpisy obrazków dodaj używając tagu `<figcaption>`.

Nie używaj CSS ani JavaScript. Zwróć wyłącznie kod HTML do wstawienia pomiędzy tagami `<body>` i `</body>`. Nie dołączaj znaczników `<html>`, `<head>` ani `<body>`. Pamiętaj, że wszystko, co znajduje się w artykule, musi zostać przepisane.

Artykuł:
{article_content}
"""


completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "user", "content": prompt}
    ],
)

# Wygenerowany kod HTML
generated_html = completion.choices[0].message.content.strip()

# Zapisanie kod HTML do pliku artykul.html
with open('artykul.html', 'w', encoding='utf-8') as file:
    file.write(generated_html)

print("Wygenerowany kod HTML został zapisany w pliku artykul.html.")
