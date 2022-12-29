import docx

document = docx.Document()

document.add_paragraph('Приветики!')

document.save('/home/lines14/projects/judicial_telegram_bot/practice.docx')