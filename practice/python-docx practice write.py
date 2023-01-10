import docx

doc = docx.Document()

p = doc.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

doc.save('/home/lines14/projects/judicial_telegram_bot/documents/practice.docx')