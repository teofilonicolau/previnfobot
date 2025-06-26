# 🧾 gitignore_explicado.md

Este documento explica as entradas do arquivo `.gitignore` utilizadas no projeto **Previnfobot**. Serve como referência para devs e contribuidores.

## 🔧 Ambiente virtual, cache e build  
`venv/` &nbsp;&nbsp;→ Pasta com dependências do ambiente Python  
`.env` &nbsp;&nbsp;→ Variáveis de ambiente locais  
`__pycache__/` &nbsp;&nbsp;→ Cache de execução Python  
`*.pyc` &nbsp;&nbsp;→ Arquivos de cache compilado Python  

---

## 📂 Dados gerados automaticamente pela pipeline  
`dados/textos_pendentes/` &nbsp;&nbsp;→ Arquivos ainda não revisados  
`dados/textos_revisados/` &nbsp;&nbsp;→ Saída da limpeza textual  
`dados/textos_limpos/` &nbsp;&nbsp;→ Arquivos aprovados  
`dados/textos_descartados/` &nbsp;&nbsp;→ Arquivos rejeitados  
`dados/*.doc / .pdf / .png` &nbsp;&nbsp;→ Entradas pesadas usadas temporariamente  
`dados/textos/.txt` &nbsp;&nbsp;→ Placeholder técnico que pode ser gerado  

---

## 📊 Logs, bancos e relatórios temporários  
`relatorios/log_revisoes.csv` &nbsp;&nbsp;→ Registro de decisões da revisão  
`relatorios/*.csv` &nbsp;&nbsp;→ Outros relatórios automáticos  
`*.log` &nbsp;&nbsp;→ Arquivos de log geral  
`*.sqlite3` &nbsp;&nbsp;→ Bancos locais temporários  

---

## 🧪 Arquivos simulados e testes  
`dados/textos_pendentes/exemplo_*.txt`  
`dados/textos_revisados/exemplo_*.txt`  

---

## 🛠️ Scripts locais e auxiliares  
`executa_tudo.py` &nbsp;&nbsp;→ Script de orquestração (pode ser recriado)  
`*.bat` &nbsp;&nbsp;→ Atalhos locais  
`*.sh` &nbsp;&nbsp;→ Scripts shell opcionais  
`drivers/` &nbsp;&nbsp;→ WebDrivers ou executáveis locais  

---

## 🖥️ Configurações locais de ambiente de desenvolvimento  
`.vscode/` &nbsp;&nbsp;→ Configurações do VS Code  
`.idea/` &nbsp;&nbsp;→ Configurações do PyCharm  
`.DS_Store` &nbsp;&nbsp;→ Arquivo oculto do macOS  

---

## 📦 Notas finais

Todas essas exclusões foram pensadas para manter o repositório limpo, leve e útil apenas com arquivos realmente necessários ao projeto e seu desenvolvimento colaborativo.

Se adicionar novas pastas temporárias, sempre consulte este arquivo e o `.gitignore`.

---

✨ Pra arrochar o nó, que seja com estilo! 😄💪🏼✨
