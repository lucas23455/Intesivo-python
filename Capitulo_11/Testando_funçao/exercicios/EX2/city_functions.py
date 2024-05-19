# city_functions.py

def cidade_pais(cidade, pais, populacao=None):
    """Return a formatted string 'Cidade, País' or 'Cidade, País – população xxx' if population is provided."""
    if populacao:
        return f"{cidade.title()}, {pais.title()} – população {populacao}"
    else:
        return f"{cidade.title()}, {pais.title()}"
