def exists_word(word, instance):
    result = list()

    for text in instance._data:
        occurrence = list()
        for index, line in enumerate(text["linhas_do_arquivo"]):

            if word.lower() in line.lower():
                occurrence.append({"linha": index + 1})
        if len(occurrence) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": text["nome_do_arquivo"],
                    "ocorrencias": occurrence,
                }
            )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
