-- Criando o banco de dados
DECLARE @NomeBancoDeDados sysname = N'Importacao_Dados_Receita_Federal';
DECLARE @DataDados DATE = '2025-08-01'; -- Dados importados de Agosto de 2025

IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = @NomeBancoDeDados
)
BEGIN
    DECLARE @SQL NVARCHAR(MAX);
    SET @SQL = N'CREATE DATABASE [' + @NomeBancoDeDados + N'];';
    EXEC(@SQL);
END;

-- Trocar para o banco criado

SET @SQL = N'USE [' + @NomeBancoDeDados + N'];';

EXEC(@SQL);

--------------------------------------------------------
-- Tabelas principais
--------------------------------------------------------

-- Empresas (CNPJs base)
IF OBJECT_ID('Empresa') IS NOT NULL DROP TABLE Empresa;
CREATE TABLE Empresa (
    CNPJ_Base CHAR(8) NOT NULL PRIMARY KEY, -- primeiros 8 dígitos do CNPJ
    Razao_Social NVARCHAR(255) NOT NULL,
    Natureza_Juridica CHAR(4) NULL,
    Qualificacao_Responsavel CHAR(2) NULL,
    Capital_Social DECIMAL(18,2) NULL,
    Porte_Empresa CHAR(1) NULL, -- 01=Micro, 02=Pequeno, 03=Médio/Grande
    Ente_Federativo_Responsavel NVARCHAR(100) NULL
);

-- Estabelecimentos (filiais e matriz)
IF OBJECT_ID('Estabelecimento') IS NOT NULL DROP TABLE Estabelecimento;
CREATE TABLE Estabelecimento (
    CNPJ CHAR(14) NOT NULL PRIMARY KEY, -- CNPJ completo
    CNPJ_Base CHAR(8) NOT NULL,
    Matriz_Filial CHAR(1) NOT NULL, -- 1=Matriz, 2=Filial
    Nome_Fantasia NVARCHAR(255) NULL,
    Situacao_Cadastral CHAR(2) NULL,
    Data_Situacao DATE NULL,
    Motivo_Situacao_Cadastral CHAR(2) NULL,
    Nome_Cidade_Exterior NVARCHAR(255) NULL,
    Pais CHAR(3) NULL,
    Data_Inicio DATE NULL,
    CNAE_Principal CHAR(7) NULL,
    Logradouro NVARCHAR(255) NULL,
    Numero NVARCHAR(20) NULL,
    Complemento NVARCHAR(100) NULL,
    Bairro NVARCHAR(100) NULL,
    CEP CHAR(8) NULL,
    UF CHAR(2) NULL,
    Municipio INT NULL,
    Telefone1 CHAR(12) NULL,
    Telefone2 CHAR(12) NULL,
    Email NVARCHAR(255) NULL,
    FOREIGN KEY (CNPJ_Base) REFERENCES Empresa(CNPJ_Base)
);

-- Sócios
IF OBJECT_ID('Socio') IS NOT NULL DROP TABLE Socio;
CREATE TABLE Socio (
    ID_Socio INT IDENTITY(1,1) PRIMARY KEY,
    CNPJ_Base CHAR(8) NOT NULL,
    Identificador_Socio CHAR(1) NULL, -- PJ ou PF
    Nome_Razao_Social NVARCHAR(255) NOT NULL,
    CNPJ_CPF_Socio NVARCHAR(14) NULL,
    Qualificacao CHAR(2) NULL,
    Percentual_Capital DECIMAL(5,2) NULL,
    Data_Entrada DATE NULL,
    FOREIGN KEY (CNPJ_Base) REFERENCES Empresa(CNPJ_Base)
);

-- CNAE Secundário
IF OBJECT_ID('CNAE_Secundaria') IS NOT NULL DROP TABLE CNAE_Secundaria;
CREATE TABLE CNAE_Secundaria (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    CNPJ CHAR(14) NOT NULL,
    CNAE CHAR(7) NOT NULL,
    FOREIGN KEY (CNPJ) REFERENCES Estabelecimento(CNPJ)
);

-- Simples Nacional
IF OBJECT_ID('Simples') IS NOT NULL DROP TABLE Simples;
CREATE TABLE Simples (
    CNPJ_Base CHAR(8) NOT NULL PRIMARY KEY,
    Opcao_Simples CHAR(1) NULL, -- S ou N
    Data_Opcao DATE NULL,
    Data_Exclusao DATE NULL,
    FOREIGN KEY (CNPJ_Base) REFERENCES Empresa(CNPJ_Base)