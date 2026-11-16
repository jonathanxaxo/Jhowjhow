# Plano do MVP — Iniciativas Sustentáveis

## Problema e usuários
Unidades precisam registrar iniciativas sustentáveis e acompanhar resultados. O MVP atende responsáveis de unidade e gestores, utilizando somente dados fictícios.

## Requisitos funcionais
- RF01 cadastrar iniciativa com nome, unidade, impacto estimado e progresso.
- RF02 listar e consultar iniciativas.
- RF03 editar todos os campos e atualizar o progresso.
- RF04 excluir iniciativa após confirmação.
- RF05 calcular total de iniciativas, finalizadas e progresso médio.
- RF06 persistir os dados em SQLite.

## Critérios de aceite
1. Um registro válido é salvo e permanece disponível após reiniciar a API.
2. Criar, editar ou excluir recalcula os três indicadores com dados do banco.
3. Progresso aceita somente valores entre 0 e 100 e a interface funciona em desktop e celular.

## Arquitetura
React/Vite → API REST FastAPI → SQLAlchemy → SQLite. Testes automatizados com pytest.

## Sprints
- S0: contexto, estrutura e documentação.
- S1: banco, modelo, API CRUD, validação e testes.
- S2: interface responsiva e integração.
- S3: dashboard calculado com dados persistidos.
- S4: homologação, evidências, README e versionamento.
