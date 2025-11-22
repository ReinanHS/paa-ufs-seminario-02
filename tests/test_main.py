import types
import pytest

try:
    import matplotlib

    matplotlib.use("Agg")
except ImportError:
    matplotlib = None

from src.main import welsh_powell, visualizar_grafo


def test_welsh_powell_example_graph():
    grafo = {
        "A": ["B", "C", "D"],
        "B": ["A", "C"],
        "C": ["A", "B", "D", "E"],
        "D": ["A", "C"],
        "E": ["C"],
    }

    resultado = welsh_powell(grafo)

    esperado = {"C": 0, "A": 1, "B": 2, "D": 2, "E": 1}
    assert resultado == esperado

    for v, vizinhos in grafo.items():
        for viz in vizinhos:
            assert resultado[v] != resultado[viz]

    assert max(resultado.values()) + 1 == 3


def test_welsh_powell_empty_graph():
    grafo_vazio = {}
    resultado = welsh_powell(grafo_vazio)
    assert resultado == {}


def test_welsh_powell_single_vertex():
    grafo = {"X": []}
    resultado = welsh_powell(grafo)
    assert resultado == {"X": 0}


def test_welsh_powell_graph_integrity_not_modified():
    grafo = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    original = {k: list(v) for k, v in grafo.items()}
    _ = welsh_powell(grafo)
    assert grafo == original


@pytest.mark.skipif(matplotlib is None, reason="matplotlib não instalado")
def test_visualizar_grafo_runs_without_error():
    grafo = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    cores = welsh_powell(grafo)
    retorno = visualizar_grafo(grafo, cores)
    assert retorno is None or isinstance(retorno, types.NoneType)
