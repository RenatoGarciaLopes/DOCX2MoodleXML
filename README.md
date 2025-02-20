# DOCX2MoodleXML-
Ferramenta para converter arquivos DOCX em XML compatível com o Moodle, preservando formatação e alternativas corretas
📄 DOCX to Moodle XML Converter

Este repositório contém uma ferramenta para converter arquivos .docx contendo questões de múltipla escolha em arquivos .xml compatíveis com o formato de importação do Moodle. A conversão preserva a formatação, espaçamentos e identifica corretamente a alternativa correta (destacada em negrito no documento original).
🚀 Funcionalidades

✅ Processa automaticamente todos os arquivos .docx de uma pasta específica
✅ Detecta perguntas e alternativas de forma estruturada
✅ Identifica a alternativa correta baseada na formatação do Word
✅ Gera arquivos .xml compatíveis com o Moodle
✅ Organiza os arquivos convertidos em uma pasta separada
📂 Como Usar

    Coloque os arquivos .docx na pasta bqs/
    Execute o script
    Os arquivos convertidos serão salvos na pasta bqs_conv/

📌 Requisitos

    Python 3.x
    Biblioteca python-docx para manipulação dos arquivos Word
