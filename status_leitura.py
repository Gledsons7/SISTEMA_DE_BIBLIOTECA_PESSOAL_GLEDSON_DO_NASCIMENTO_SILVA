from enum import Enum


class StatusLeitura(Enum):
    """Representa os possíveis estados de leitura de uma publicação."""

    NAO_LIDO = 1
    LENDO = 2
    LIDO = 3
