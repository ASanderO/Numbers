# Rodar os testes
python -m unittest discover -s tests

# Rodar os testes com coverage
coverage run --source=src -m unittest discover -s tests

# Gerar um relatório no console
coverage report

# Opcional: Gerar um relatório HTML mais detalhado
coverage html
