#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[33m-=-\033[m'*20)
print('\033[33mEmpréstimo Bancário\033[m')
print('\033[33m-=-\033[m'*20)
#cliente colocando as infos
casa=float(input('Qual é o valor da casa?: R$'))
s=float(input('Informe o seu salário: R$'))
anos=int(input('Quantos anos  pretende pagar?(informe numeros inteiros pfvr) '))
#calculos
meses=anos*12
pres = casa/meses
por=(30*s)/100
if pres<=por:
    print('\033[32mTrato feito amigo!\033[m')
elif pres>por:
    print('''Lamento amigo, \033[31mnão\033[m temos como fechar negócio!.
A parcela fica R${:.2f}, oq ultrapassa os 30% do seu salário'''.format(pres))

