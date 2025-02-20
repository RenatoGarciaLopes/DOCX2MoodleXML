📄 DOCX to Moodle XML Converter

Descrição: Ferramenta para converter arquivos DOCX com questões de múltipla escolha em XML compatível com o Moodle, preservando formatação e identificando a alternativa correta.
🚀 Funcionalidades

✅ Processa automaticamente todos os arquivos .docx de uma pasta específica (bqs/)
✅ Detecta perguntas e alternativas de forma estruturada
✅ Identifica a alternativa correta com base na formatação (negrito)
✅ Gera arquivos .xml compatíveis com a importação no Moodle
✅ Organiza os arquivos convertidos na pasta bqs_conv/
📦 Instalação

    Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Instale as dependências:

    pip install python-docx

📂 Como Usar

    Coloque os arquivos .docx na pasta bqs/
    Execute o script:

    python converter.py

    Os arquivos convertidos estarão na pasta bqs_conv/

📜 Licença

Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para mais detalhes.
