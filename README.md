<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Ufs_principal_positiva-nova.png" alt="ufs-logo" width="20%">

<h1>Seminário 2 — PAA <br>Coloração de Grafos</h1>

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ReinanHS/paa-ufs-seminario-02?machine=standardLinux2gb)

<p align="center">
  <!-- GitHub Pages (online/offline) -->
  <a href="https://reinanhs.github.io/paa-ufs-seminario-02/">
    <img src="https://img.shields.io/website?url=https%3A%2F%2Freinanhs.github.io%2Fpaa-ufs-seminario-02%2F&label=GitHub%20Pages" alt="GitHub Pages">
  </a>
  <!-- Python version -->
  <img src="https://img.shields.io/badge/python-3.12%2B-blue.svg" alt="Python 3.12+">
  <!-- License -->
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="Licença MIT">
  </a>
  <!-- Last commit -->
  <a href="https://github.com/ReinanHS/paa-ufs-seminario-02/commits/main">
    <img src="https://img.shields.io/github/last-commit/ReinanHS/paa-ufs-seminario-02.svg" alt="Último commit">
  </a>
  <!-- Stars -->
  <a href="https://github.com/ReinanHS/paa-ufs-seminario-02/stargazers">
    <img src="https://img.shields.io/github/stars/ReinanHS/paa-ufs-seminario-02.svg?style=social" alt="Stars">
  </a>
</p>

</div>

## 📚 Sobre

Repositório do seminário de **Projeto e Análise de Algoritmos (PAA)** sobre o **Problema de Coloração de Grafos**.

Veja abaixo as principais implementações que estão contidas neste projeto:

- Implementação **em Python** (código principal a ser executado pelo professor);
- Scripts, dados e testes automatizados.

O código desse repositório implementa o algoritmo de coloração gulosa conhecido como Welsh–Powell.
O objetivo é colorir os vértices de um grafo usando o menor número possível de cores, garantindo que dois vértices adjacentes não tenham a mesma cor.

---

## Colaboradores

Apresentamos os principais membros da equipe:

<div align="center">
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/ReinanHS">
        <img src="https://github.com/reinanhs.png" height="64" width="64" alt="Reinan Gabriel"/>
      </a><br/>
      <a href="https://github.com/ReinanHS">Reinan Gabriel</a>
    </td>
    <td align="center">
      <a href="https://github.com/pauloEzequiel">
        <img src="https://github.com/pauloEzequiel.png" height="64" width="64" alt="Paulo Ezequiel"/>
      </a><br/>
      <a href="https://github.com/pauloEzequiel">Paulo Ezequiel</a>
    </td>
    <td align="center">
      <a href="https://github.com/joaorabelo">
        <img src="https://github.com/joaorabelo.png" height="64" width="64" alt="João Rabelo"/>
      </a><br/>
      <a href="https://github.com/joaorabelo">João Rabelo</a>
    </td>
  </tr>
</table>
</div>

---

## Vídeo da apresentação

O link abaixo direciona para o vídeo hospedado no YouTube, que registra a apresentação do seminário sobre o problema da coloração de grafos. Nele, são abordados os principais aspectos do tema, juntamente com um exemplo prático da execução do
algoritmo desenvolvido neste repositório.

[![Youtube Video](https://gitlab.com/reinanhs/repo-slide-presentation/-/wikis/uploads/8f7f989453c0399ee12f872147bf9032/image.png)](https://youtu.be/dtij-Yeyyz4)

- 📹 **Assista:** [https://youtu.be/dtij-Yeyyz4](https://youtu.be/dtij-Yeyyz4)

> Exigência do professor: O README deve conter o link do vídeo no YouTube.

---

## Diretrizes do seminário

### Tema do grupo

- **Problema de Coloração de Grafos.**

### O que apresentar

- **Introdução** breve ao problema e **uma aplicação real**.

- **Como o algoritmo escolhido resolve o problema** (ótimo ou aproximado), focando no **problema** e na **ideia do
  algoritmo**.

- **Exemplo funcional**:

  - Definir **uma instância** do problema,
  - Mostrar o **código-fonte**,
  - **Executar** e apresentar a **solução/resultado**.

- **Não explicar técnicas gerais** (programação dinâmica, gulosa etc.); o professor cobrirá essas bases.

### Estrutura sugerida dos slides

- Introdução
- Definição do problema
- Como o algoritmo resolve
- Código/Experimento
- Resultados
- Referências.

### Duração

- **Tempo máximo: 15 minutos.**

### Entregáveis no repositório (GitHub)

- **Slides** do seminário em **PDF**.

- **Pasta com dados e códigos** usados no experimento.

  - Evitar dependências específicas; preferir **Python, R ou Java**.
  - Código **portável** (qualquer SO) e **sem vínculo** com IDE específica.

- **README** com **link para o vídeo** da apresentação no YouTube.

> **Atenção:** a **data do último commit** **não pode** ser posterior à data de entrega do Seminário 2.

---

## Estrutura do repositório

```
├── src/                # Código Python principal
│   └── main.py
├── tests/              # Testes automatizados (pytest)
├── .github/workflows/  # CI (tests, artefatos, Pages)
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Execução

Veja abaixo as instruções de como executar o código.

### Pré-requisitos

- **Python 3.12+**

### Instalação e execução

```bash
# opcional: criar e ativar venv
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\activate

# dependências mínimas
pip install --upgrade pip
pip install -r requirements.txt  # ou: pip install numpy pandas matplotlib pytest

# executar
python src/main.py
```

Saída esperada (exemplo compacto no console):

```shell
Ordem de processamento: ['C', 'A', 'B', 'D', 'E', 'F']
------------------------------
Resultado da Coloração (Texto):
Vértice A: Cor 1
Vértice B: Cor 2
Vértice C: Cor 0
Vértice D: Cor 2
Vértice E: Cor 1
Vértice F: Cor 1

Gerando imagem...
```

O script também gera essa imagem:

<img width="450" height="350" alt="Figure_1" src="https://gitlab.com/reinanhs/repo-slide-presentation/-/wikis/uploads/08a72cfca07fd4a5b0bf1de27c0f4dcb/Figure_1.png" />

Veja abaixo um exemplo de como fica a tabela de cores para o cenário apresentado na imagem:

| Vértice | Arestas | Cor |
| ------- | ------- | --- |
| C       | 4       | 0   |
| A       | 3       | 1   |
| B       | 2       | 2   |
| D       | 2       | 2   |
| E       | 1       | 1   |

---

## Testes

A seguir, apresentamos o procedimento para execução dos testes unitários desenvolvidos para este repositório:

```bash
pytest -q
```

---

## Links úteis

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1lEKh039yEsfwVY3I6NTUHdcz6Pq1OG5x8jv9GAldyE0/edit?usp=sharing)
- [Slide em PDF](./data/slide.pdf)
- [Vídeo no Youtube](https://youtu.be/dtij-Yeyyz4)

---

## Licença

Este projeto está sob a licença [MIT](LICENSE).

---

## Contribuindo

Quer contribuir? Leia nosso guia de contribuição: [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Estatísticas do repositório

[![Contribuidores](https://contrib.rocks/image?repo=ReinanHS/paa-ufs-seminario-02)](https://github.com/ReinanHS/paa-ufs-seminario-02/graphs/contributors)
![Gráfico de commits](https://img.shields.io/github/commit-activity/m/ReinanHS/paa-ufs-seminario-02)
![Histórico de estrelas](https://starchart.cc/ReinanHS/paa-ufs-seminario-02.svg)
