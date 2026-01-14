from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_comparison_pdf(filename="comparaison_osint.pdf"):
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Titre
    elements.append(Paragraph(
        "<b>Projet 9 – Comparaison d’outils de reconnaissance OSINT</b>",
        styles["Title"]
    ))
    elements.append(Spacer(1, 20))

    # Tableau comparatif
    data = [
        ["Critère",
         "Implémentation maison (Python)",
         "Outils professionnels (Maltego / Recon-ng)"],

        ["WHOIS",
         "Données clés (registrar, dates, NS)\nLibrairie whois",
         "Informations étendues + enrichissement automatique"],

        ["Résolution DNS",
         "A, MX, NS, TXT via dnspython",
         "Résolution complète + graphes"],

        ["Collecte d’emails",
         "API Hunter.io (clé gratuite)\nLimite 100 requêtes/mois",
         "Intégration multi-sources\nRésultats enrichis"],

        ["Vitesse d’exécution",
         "Rapide (local, script Python)",
         "Variable (dépend du moteur et API)"],

        ["Précision",
         "Bonne mais dépendante des APIs",
         "Très élevée (corrélation de sources)"],

        ["Automatisation",
         "Totale (scripts personnalisables)",
         "Avancée mais orientée GUI"],

        ["Facilité d’utilisation",
         "Nécessite des compétences Python",
         "Interface graphique intuitive"],

        ["Contrôle et transparence",
         "Contrôle total (pas de boîte noire)",
         "Fonctionnement interne opaque"],

        ["Respect éthique",
         "100 % conforme (pas de scan actif)",
         "Dépend de la configuration utilisateur"],

        ["Cas d’usage recommandé",
         "Apprentissage, audit léger, scripts dédiés",
         "Investigations OSINT avancées"]
    ]

    table = Table(data, colWidths=[120, 200, 200])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))

    elements.append(table)
    pdf.build(elements)

    print(f"[+] PDF généré avec succès : {filename}")


if __name__ == "__main__":
    generate_comparison_pdf()
