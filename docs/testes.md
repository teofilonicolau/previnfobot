# ✅ Testes Automatizados – Previnfobot

Este documento detalha a implementação dos testes automatizados, com foco didático e rastreável.

## 📦 Estrutura dos Arquivos de Teste

Local: `tests/`

- `test_limpeza.py`: testa a função `limpar_texto`
- `test_hash_utils.py`: garante integridade com `gerar_hash_sha256`
- `test_api.py`: verifica resposta e status da rota `/consultar`
- `test_estrutura.py`: estrutura base para testes futuros

---

## 🧪 Como rodar os testes

1. Instale as dependências:

```bash
pip install pytest pytest-cov
```

2. Execute os testes com cobertura:

```bash
$env:PYTHONPATH="."
pytest --cov=app tests/
```

> Use o comando acima no PowerShell, estando na raiz do projeto.

---

## 📊 Cobertura Atual

```text
app/api/router.py                 100%
app/services/hash_utils.py       100%
app/services/limpeza.py          100%
app/services/rag.py               77%
TOTAL                             68%
```

Badge sugerido para o `README.md`:

```markdown
![Cobertura de Testes](https://img.shields.io/badge/cobertura-68%25-yellowgreen)
```

---

## 🧠 Por que testar?

- Garante que o código continua funcionando após mudanças
- Dá segurança para refatorações
- Cria base para automação com GitHub Actions
- Inspira confiança no projeto — inclusive por outras pessoas

🧪 *Testar é escrever software que protege seu próprio software.*
