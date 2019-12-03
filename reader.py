import pandas as pd
import numpy

equals_cnpj = []
inscricao_estadual = []
inscricao_suframa = []
inscricao_municipal = []
gerar_boleto = []
cont = 0

doc = pd.read_excel('planilha.xls')


cnpj_cpf_Values = doc["CNPJ/CPF"].values
cnpj_Values = doc["CNPJ"].values

insc_estadual_Values = doc["Insc. Estadual"].values
insc_municipal_Values = doc["Insc. Municipal"].values
insc_suframa_Values = doc["Insc. Suframa"].values
boleto_Values = doc["E-mail"].values


for i in range(0, 702):
    for l in range(0, 11051):
        if cnpj_cpf_Values[i] == cnpj_Values[l]:
            equals_cnpj.append(cnpj_cpf_Values[i])
            inscricao_estadual.append(insc_estadual_Values[i])
            inscricao_municipal.append(insc_municipal_Values[i])
            inscricao_suframa.append(insc_suframa_Values[i])
            gerar_boleto.append(boleto_Values[i])


data = {'Cnpj/Cpf':equals_cnpj, 'Inscricao Estadual':inscricao_estadual, 'Inscricao Municipal':inscricao_municipal, 
                                    'Inscricao Suframa':inscricao_suframa, 'Gerar Boleto ao Emitir MF':gerar_boleto}

df = pd.DataFrame(data)

df.to_excel("planilhaTop.xls")
