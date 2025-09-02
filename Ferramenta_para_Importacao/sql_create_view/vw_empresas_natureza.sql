CREATE VIEW vw_empresas_natureza AS
SELECT
    e.[CNPJ Básico],
    e.[Razão Social / Nome Empresarial],
    n.[Descrição] AS Natureza_Juridica
FROM
    EMPRESAS e
    LEFT JOIN NATUREZAS n ON e.[Natureza Jurídica] = n.[Código];