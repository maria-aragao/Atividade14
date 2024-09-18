# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))

média =(nota1 + nota2 + nota3) / 3 

print('Tirando {} e {}, média do aluno é {:.1f}'. format(nota1, nota2, nota3, média))

if média >=7:
    print('Aprovado')

elif 5 == média and média <7:
    print('Recuperação')

elif média < 5:
    print('Reprovado')