# Execução local - OptiGrid Indústrias

Este é o backend da aplicação OptiGrid Indústrias, desenvolvido em Flask para fornecer APIs que alimentam o painel de controle.

## Passos para configuração e execução

### 1. Download dos arquivos

#### Alternativa 1 - GitHub:
- Clone o repositório do GitHub com os arquivos do backend e frontend: `git clone https://github.com/gustavoakira-sw/gustavoakira-sw.github.io.git`

#### Alternativa 2 - Google Drive:
- Acesse o [Google Drive](https://drive.google.com/drive/folders/1cQjysI4j4Z_mjP58VLS3m-gFFYp-962N?usp=sharing).
- Navegue até a pasta `Completo (backend + frontend)` > `backend` e baixe todos os arquivos.

### 2. Configuração do ambiente virtual (venv)
1. Abra o terminal na pasta onde os arquivos do backend foram baixados.
2. Crie e ative o ambiente virtual do Python:
   ```
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

### 3. Execução do servidor
1. Inicie o a aplicação do Flask.
   ```
   python3 app.py
   ```
- A API estará disponível em: http://localhost:5001. Certifique-se de que a porta `5001` esteja livre para o servidor Flask. Caso queira alterar a porta, modifique a linha no final do arquivo `app.py`.

   ```
    35 |  if __name__ == "__main__":
    36 |    app.run(debug=True, host="0.0.0.0", port=5001) # altere a porta aqui
   ```