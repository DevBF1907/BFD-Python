
valor_hora = float(input("Valor da hora: "))
horas = float(input("Horas no mês: "))


bruto = valor_hora * horas
ir = bruto * 0.11
inss = bruto * 0.09
sind = bruto * 0.04
liquido = bruto - (ir + inss + sind)


print(f"\n+ Salário Bruto   : R$ {bruto:.2f}")
print(f"- IR (11%)        : R$ {ir:.2f}")
print(f"- INSS (9%)       : R$ {inss:.2f}")
print(f"- Sindicato (4%)  : R$ {sind:.2f}")
print(f"= Salário Líquido : R$ {liquido:.2f}")
