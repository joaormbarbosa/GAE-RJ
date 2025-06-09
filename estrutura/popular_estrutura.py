from estrutura.models import Estado, RegionalAdministrativa, Administracao

def popular():
    estado_rj, _ = Estado.objects.get_or_create(nome="RJ")

    estrutura = {
        "Rio de Janeiro": ["Rio de Janeiro"],
        "Angra dos Reis": ["Angra dos Reis", "Paraty"],
        "Duque de Caxias": ["Duque de Caxias", "Belford Roxo"],
        "Itaperuna": ["Itaperuna", "Campos", "Itaocara"],
        "Macaé": ["Macaé", "Cabo Frio"],
        "Nova Iguaçu": ["Nova Iguaçu", "Nilópolis"],
        "São Gonçalo": ["São Gonçalo", "Tanguá"],
        "Resende": ["Resende", "Barra do Piraí", "Volta Redonda"],
        "Nova Friburgo": ["Nova Friburgo", "Bom Jardim", "Sumidouro", "Três Rios"]
    }

    for nome_regional, adms in estrutura.items():
        regional, _ = RegionalAdministrativa.objects.get_or_create(nome=nome_regional, estado=estado_rj)
        for nome_adm in adms:
            Administracao.objects.get_or_create(nome=nome_adm, regional=regional)

    print("Base populada com sucesso!")
