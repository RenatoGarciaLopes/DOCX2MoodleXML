# 📄 DOCX to Moodle XML Converter

**Descrição:** Ferramenta para converter arquivos **DOCX** com questões de múltipla escolha em **XML** compatível com o **Moodle**, preservando formatação e identificando a alternativa correta.

## 🚀 Funcionalidades  
✅ Processa automaticamente todos os arquivos `.docx` de uma pasta específica (`BQS/`)  
✅ Detecta perguntas e alternativas de forma estruturada  
✅ Identifica a alternativa correta com base na formatação (**negrito**)  
✅ Gera arquivos `.xml` compatíveis com a importação no Moodle  
✅ Organiza os arquivos convertidos na pasta `BQS_CONV/`  

## 📦 Instalação  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/RenatoGarciaLopes/DOCX2MoodleXML.git
   cd DOCX2MoodleXML
   ```  
2. Instale as dependências:  
   ```bash
   pip install python-docx
   ```  

## 📂 Como Usar  
1. Coloque os arquivos **.docx** na pasta `BQS/`  
2. Execute o script:  
   ```bash
   python program.py
   ```  
3. Os arquivos convertidos estarão na pasta `BQS_CONV/`  

## 📜 Licença  
Este projeto está licenciado sob a **MIT License** – veja o arquivo [LICENSE](LICENSE) para mais detalhes.
