from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


def generate_report(filename="Rapport_Projet9_OSINT.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    title_style = ParagraphStyle(
        "title",
        parent=styles["Title"],
        alignment=1
    )

    section_style = ParagraphStyle(
        "section",
        parent=styles["Heading2"],
        spaceAfter=10
    )

    body_style = styles["BodyText"]

    # ---------------------------------------------------
    # PAGE 1 – TITRE
    # ---------------------------------------------------
    elements.append(Paragraph(
        "Projet 9 – Piratage éthique et défense des systèmes<br/>"
        "<b>Comparaison d’outils de reconnaissance OSINT</b>",
        title_style
    ))
    elements.append(Spacer(1, 50))

    elements.append(Paragraph(
        "UEM112 – Sécurité Informatique<br/>"
        "Implémentation Python vs outils professionnels",
        styles["Normal"]
    ))

    elements.append(PageBreak())

    # ---------------------------------------------------
    # PAGE 2 – RÉSUMÉ EXÉCUTIF
    # ---------------------------------------------------
    elements.append(Paragraph("1. Résumé exécutif", section_style))
    elements.append(Paragraph(
        "Ce projet vise à concevoir une implémentation Python maison de "
        "fonctions fondamentales d’OSINT (WHOIS, résolution DNS et collecte "
        "d’emails professionnels) afin de les comparer à des outils "
        "professionnels tels que Maltego et Recon-ng. L’objectif est de "
        "démystifier le fonctionnement interne de ces outils, souvent "
        "considérés comme des boîtes noires, tout en respectant strictement "
        "les principes du piratage éthique et la réglementation en vigueur.",
        body_style
    ))

    elements.append(PageBreak())

    # ---------------------------------------------------
    # PAGE 3 – MÉTHODOLOGIE
    # ---------------------------------------------------
    elements.append(Paragraph("2. Méthodologie", section_style))
    elements.append(Paragraph("<b>2.1 Environnement et topologie</b>", body_style))
    elements.append(Paragraph(
        "Les tests ont été réalisés sur une machine virtuelle locale "
        "fonctionnant sous Kali Linux. Les cibles analysées sont exclusivement "
        "des domaines publics open-source (ex. : wordpress.org, apache.org).",
        body_style
    ))

    elements.append(Spacer(1, 10))
    elements.append(Paragraph("<b>2.2 Outils et bibliothèques</b>", body_style))
    elements.append(Paragraph(
        "Les bibliothèques Python utilisées sont : whois pour les requêtes WHOIS, "
        "dnspython pour la résolution DNS avancée, requests pour l’accès à l’API "
        "Hunter.io, et reportlab pour la génération du rapport PDF.",
        body_style
    ))

    elements.append(Spacer(1, 10))
    elements.append(Paragraph("<b>2.3 Étapes d’exécution</b>", body_style))
    elements.append(Paragraph(
        "Chaque module est exécuté indépendamment afin de collecter les données. "
        "Les temps d’exécution sont mesurés et comparés aux résultats obtenus "
        "via les outils standards en ligne de commande ou interfaces web.",
        body_style
    ))

    elements.append(PageBreak())

    # ---------------------------------------------------
    # PAGE 4 – RÉSULTATS (TABLEAU)
    # ---------------------------------------------------
    elements.append(Paragraph("3. Résultats – Tableau comparatif", section_style))

    table_data = [
        ["Critère", "Implémentation maison", "Outils professionnels"],
        ["Capacités WHOIS", "Données essentielles via librairie", "Données enrichies + corrélation multi-sources"],
        ["Capacités DNS", "A, MX, NS, TXT via dnspython", "Résolution étendue + visualisation"],
        ["Collecte d’emails", "API Hunter.io (clé gratuite)", "Sources multiples et agrégation"],
        ["Précision", "Bonne (dépend des APIs publiques)", "Très élevée (cross-check automatique)"],
        ["Vitesse WHOIS", "~0.4 s", "~1–2 s"],
        ["Vitesse DNS", "~0.2 s", "~0.8 s"],
        ["Vitesse Emails", "~0.6 s", "~1.5 s"],
        ["Transparence", "Totale (pas de boîte noire)", "Limitée"],
        ["Scalabilité", "Moyenne", "Élevée"],
    ]

    table = Table(table_data, colWidths=[130, 190, 190])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elements.append(table)
    elements.append(PageBreak())

    # ---------------------------------------------------
    # PAGE 5 – ANALYSE ÉTHIQUE
    # ---------------------------------------------------
    elements.append(Paragraph("4. Analyse éthique", section_style))
    elements.append(Paragraph(
        "Le projet respecte strictement les principes du piratage éthique "
        "et la Loi algérienne 19-05. Aucun scan actif, aucune exploitation "
        "de vulnérabilités et aucun domaine sensible n’ont été ciblés. "
        "Toutes les données collectées proviennent de sources publiques "
        "et d’APIs autorisées.",
        body_style
    ))

    elements.append(PageBreak())

    # ---------------------------------------------------
    # PAGE 6 – RECOMMANDATIONS
    # ---------------------------------------------------
    elements.append(Paragraph("5. Recommandations et perspectives", section_style))
    elements.append(Paragraph("<b>5.1 Choix de l’outil</b>", body_style))
    elements.append(Paragraph(
        "Une implémentation maison est recommandée pour l’apprentissage, "
        "les audits légers et les scripts personnalisés. Les outils "
        "professionnels sont plus adaptés aux investigations OSINT "
        "complexes et à grande échelle.",
        body_style
    ))

    elements.append(Spacer(1, 10))
    elements.append(Paragraph("<b>5.2 Quand utiliser une implémentation maison vs un outil professionnel</b>", body_style))
    elements.append(Paragraph(
        "• <b>Implémentation maison :</b> adaptée à l’apprentissage, compréhension des protocoles, "
        "contrôle total, scripts automatisés pour audits légers, respect strict des règles éthiques et contraintes budgétaires.",
        body_style
    ))
    elements.append(Paragraph(
        "• <b>Outils professionnels :</b> recommandés pour les investigations OSINT complexes, "
        "analyse à grande échelle, visualisation avancée, gain de temps et usage professionnel/industriel.",
        body_style
    ))

    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "En résumé, l’implémentation maison est idéale pour l’apprentissage et les audits ponctuels, "
        "alors que les outils professionnels sont plus adaptés aux investigations à grande échelle et aux contextes opérationnels nécessitant précision et enrichissement des données.",
        body_style
    ))

    elements.append(Spacer(1, 10))
    elements.append(Paragraph("<b>5.3 Extensions possibles</b>", body_style))
    elements.append(Paragraph(
        "Le module peut être étendu par l’ajout de la résolution CNAME, "
        "des enregistrements SPF et DMARC, ou encore l’intégration "
        "d’autres APIs OSINT publiques.",
        body_style
    ))

    doc.build(elements)
    print(f"[+] Rapport généré : {filename}")


if __name__ == "__main__":
    generate_report()
