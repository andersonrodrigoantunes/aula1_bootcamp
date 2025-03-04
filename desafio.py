# Variável Constante
CONSTANTE_BONUS = 1000

# 1) Solicitar ao usuário que digite ser nome
nome = input("Digite seu nome: ")

# 2) Solicitar ao usuário que digite o valor de seu salário
# Converter a entrada para número de ponto flutuante

salario = float(input("Digiteo valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus rececebido
# Converter a entrada para um numero do ponto flutuante

bonus = float(input("Digite o valor do bonus recebido: "))

# 4) Calcule o valor do bônus final

bonus_final = CONSTANTE_BONUS + salario * bonus

# 5) Imprima cálculo do kpi para o usuário

print("O Calculo utuilizado foi: 1000 + Salário * Bonus")

# 6) Imprime mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"Olá: {nome}, seu salário é: {salario} e seu bônus foi de: {bonus}%, com o valor tota a receber de: {bonus_final}")