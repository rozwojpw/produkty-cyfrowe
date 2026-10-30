import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


def create_day_page(pdf, day_number, question, reflection, quote):
    width, height = A4
    margin = 20 * mm
    y = height - margin

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(margin, y, f"Dzie\u0144 {day_number}")
    y -= 30

    pdf.setFont("Helvetica", 12)
    pdf.drawString(margin, y, f"Pytanie dnia: {question}")
    y -= 20

    pdf.drawString(margin, y, f"Refleksja: {reflection}")
    y -= 20

    pdf.drawString(margin, y, f"Cytat dnia: {quote}")
    y -= 30

    # Box for notes
    box_height = height / 2
    pdf.rect(margin, y - box_height, width - 2 * margin, box_height, stroke=1, fill=0)
    pdf.showPage()


def create_summary_page(pdf, summary_text):
    width, height = A4
    margin = 20 * mm
    y = height - margin

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(margin, y, "Podsumowanie")
    y -= 30

    pdf.setFont("Helvetica", 12)
    for line in summary_text.split("\n"):
        pdf.drawString(margin, y, line)
        y -= 20

    pdf.showPage()


def main(output_path="dziennik_praktyki.pdf"):
    pdf = canvas.Canvas(output_path, pagesize=A4)

    days = [
        {
            "question": "Co dzi\u015b naprawd\u0119 czuj\u0119 i dlaczego?",
            "reflection": "Pozw\u00f3l sobie na szczero\u015b\u0107 wobec siebie. Emocje to kompas, nie przeszkoda.",
            "quote": "\u201ePoznaj samego siebie.\u201d \u2014 Sokrates",
        },
        {
            "question": "Jakie my\u015bli mnie dzi\u015b ograniczaj\u0105?",
            "reflection": "\u015awiadomo\u015b\u0107 ogranicze\u0144 to pierwszy krok do wolno\u015bci.",
            "quote": "\u201eWolno\u015b\u0107 zaczyna si\u0119 tam, gdzie ko\u0144czy si\u0119 strach.\u201d \u2014 Viktor Frankl",
        },
        {
            "question": "Czego chcia\u0142bym dzi\u015b do\u015bwiadczy\u0107?",
            "reflection": "Kreuj rzeczywisto\u015b\u0107 zgodn\u0105 z Twoimi pragnieniami.",
            "quote": "\u201eJeste\u015b tym, czym wierzysz, \u017ce jeste\u015b.\u201d \u2014 Paulo Coelho",
        },
        {
            "question": "Co dzia\u0142o si\u0119 wczoraj, co mog\u0119 zrozumie\u0107 lepiej?",
            "reflection": "Zrozumienie przesz\u0142o\u015bci otwiera drzwi do przysz\u0142o\u015bci.",
            "quote": "\u201eHistoria jest nauczycielk\u0105 \u017cycia.\u201d \u2014 Cyceron",
        },
        {
            "question": "Jak mog\u0119 dzi\u015b zadba\u0107 o siebie?",
            "reflection": "Twoje potrzeby s\u0105 wa\u017cne. Nie odk\u0142adaj ich na potem.",
            "quote": "\u201eZdrowy duch w zdrowym ciele.\u201d \u2014 Juvenalis",
        },
        {
            "question": "Komu mog\u0119 dzi\u015b okaza\u0107 wsparcie?",
            "reflection": "Empatia tworzy g\u0142\u0119bokie wi\u0119zi mi\u0119dzy lud\u017ami.",
            "quote": "\u201eTo, co dajemy innym, wraca do nas.\u201d \u2014 Laozi",
        },
        {
            "question": "Co mnie dzi\u015b najbardziej inspiruje?",
            "reflection": "Inspiracja jest iskr\u0105, kt\u00f3ra rozpala dzia\u0142anie.",
            "quote": "\u201eRzeczy wielkie zaczynaj\u0105 si\u0119 od marze\u0144.\u201d \u2014 Walt Disney",
        },
    ]

    for i, day in enumerate(days, 1):
        create_day_page(pdf, i, day["question"], day["reflection"], day["quote"])

    summary = (
        "Refleksje i odkrycia z ca\u0142ego tygodnia.\n"
        "Notatki dotycz\u0105ce dalszych pyta\u0144 i cel\u00f3w.\n"
        "Zach\u0119ta do kontynuowania praktyki."
    )

    create_summary_page(pdf, summary)
    pdf.save()


if __name__ == "__main__":
    main()
