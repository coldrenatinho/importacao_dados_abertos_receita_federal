CREATE VIEW vw_empresas_municipio AS
SELECT
    e.[CNPJ Básico],
    e.[Razão Social / Nome Empresarial],
    est.[Município],
    m.[Descrição] AS Nome_Municipio
FROM
    EMPRESAS e
    LEFT JOIN ESTABELECIMENTOS est ON e.[CNPJ Básico] = est.[CNPJ Básico]
    LEFT JOIN MUNICIPIOS m ON est.[Município] = m.[Código];