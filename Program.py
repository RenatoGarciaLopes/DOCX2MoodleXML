import os
from docx import Document
import xml.etree.ElementTree as ET
from xml.dom import minidom

def docx_to_moodle_xml(input_path, output_path):
    doc = Document(input_path)
    root = ET.Element('quiz')
    
    current_question = None
    answers = []
    question_text = ""
    processing_question = False

    for para in doc.paragraphs:
        text = para.text.strip() if para.text else ""
        style = para.style.name

        # Detecta início de nova questão
        if text.startswith("Questão:") or style == 'Heading 2':
            if current_question is not None:
                # Adiciona respostas da questão anterior
                for answer in answers:
                    answer_elem = ET.SubElement(current_question, 'answer', {
                        'fraction': '100' if answer['correct'] else '0',
                        'format': 'html'
                    })
                    text_elem = ET.SubElement(answer_elem, 'text')
                    text_elem.text = f"{answer['text']}"
                    
                    feedback = ET.SubElement(answer_elem, 'feedback', {'format': 'html'})
                    ET.SubElement(feedback, 'text').text = ""

            # Reseta para nova questão
            current_question = ET.SubElement(root, 'question', {'type': 'multichoice'})
            answers = []
            question_text = text.replace("Questão:", "").strip()
            processing_question = True
            
            # Cabeçalho da questão
            name = ET.SubElement(current_question, 'name')
            ET.SubElement(name, 'text').text = f"Q{len(root.findall('question'))}"
            
            questiontext = ET.SubElement(current_question, 'questiontext', {'format': 'html'})
            text_elem = ET.SubElement(questiontext, 'text')
            text_elem.text = f"{question_text}"
            
            # Adiciona atributos obrigatórios do Moodle para questões de múltipla escolha
            ET.SubElement(current_question, 'generalfeedback', {'format': 'html'}).text = ""
            ET.SubElement(current_question, 'defaultgrade').text = "1.0000000"
            ET.SubElement(current_question, 'penalty').text = "0.3333333"
            ET.SubElement(current_question, 'hidden').text = "0"
            ET.SubElement(current_question, 'idnumber').text = ""
            ET.SubElement(current_question, 'single').text = "true"
            ET.SubElement(current_question, 'shuffleanswers').text = "true"
            ET.SubElement(current_question, 'answernumbering').text = "abc"
            ET.SubElement(current_question, 'showstandardinstruction').text = "1"
            
            # Adiciona feedback padrão
            ET.SubElement(current_question, 'correctfeedback', {'format': 'html'}).text = "Sua resposta está correta."
            ET.SubElement(current_question, 'partiallycorrectfeedback', {'format': 'html'}).text = "Sua resposta está parcialmente correta."
            ET.SubElement(current_question, 'incorrectfeedback', {'format': 'html'}).text = "Sua resposta está incorreta."
            ET.SubElement(current_question, 'shownumcorrect')
            
            continue

        # Detecta alternativas corretamente e evita adicioná-las ao enunciado
        if text[:3].strip().lower() in ['a)', 'b)', 'c)', 'd)', 'e)']:
            answer_text = text[3:].strip()
            is_correct = any(run.bold for run in para.runs)  # Detecta negrito como alternativa correta
            answers.append({'text': answer_text, 'correct': is_correct})
            continue  # Pula a adição ao enunciado

        # Coleta texto da questão (múltiplos parágrafos)
        if processing_question and text:
            text_elem = current_question.find('./questiontext/text')
            if text_elem is not None:
                if text_elem.text is None:
                    text_elem.text = text
                else:
                    text_elem.text += f"</p><p>{text}"

    # Adiciona última questão
    if current_question is not None:
        for answer in answers:
            answer_elem = ET.SubElement(current_question, 'answer', {
                'fraction': '100' if answer['correct'] else '0',
                'format': 'html'
            })
            text_elem = ET.SubElement(answer_elem, 'text')
            text_elem.text = f"{answer['text']}"
            
            feedback = ET.SubElement(answer_elem, 'feedback', {'format': 'html'})
            ET.SubElement(feedback, 'text').text = ""

    # Gera XML formatado e substitui manualmente os CDATA
    xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
    xml_str = xml_str.replace('<text>', '<text><![CDATA[').replace('</text>', ']]></text>').replace('&lt;', '<').replace('&gt;', '>').replace('&lt;br/&gt;', '<br/>')
    
    # Formata XML corretamente
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent='  ', encoding='utf-8')
    
    with open(output_path, 'wb') as f:
        f.write(pretty_xml)
    
    return True

# Configurações
target_folder = "BQS"
output_folder = "BQS-XML"
os.makedirs(output_folder, exist_ok=True)

# Processar arquivos
processed = 0
for filename in os.listdir(target_folder):
    if filename.endswith(".docx"):
        input_path = os.path.join(target_folder, filename)
        output_filename = filename.replace(".docx", ".xml")
        output_path = os.path.join(output_folder, output_filename)
        
        if docx_to_moodle_xml(input_path, output_path):
            print(f"Arquivo gerado: {output_filename}")
            processed += 1

print(f"\nConversão concluída! {processed} arquivos processados.")
