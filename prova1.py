#Escreva um programa que solicite ao usuário que informe a senha secreta do sistema. A senha secreta é uma string que é pré-definida e está armazenada em uma váriavel do programa (por exemplo, você pode usar a senha = "senha1234" no seu programa). O programa deve continuar pedindo ao usuário para digitar a senha até que ele a informe corretamente ou até o usuário realizar 10 tentativas incorretas. Quando o usuário informar incorretamente a senha, o programa deve imprimir uma mensagem informando que a tentativa falhou e quantas tentativas restantes o usuário ainda tem antes que o programa seja encerrado. Quando o usuário informar a senha correta, o programa deve imprimir uma mensagem de sucesso e ser encerrado. Quando o usuário informar a senha incorretamente 10 vezes, o programa deve imprimir uma mensagem de falha e encerra sua execução. 

senha_secreta = 'senha1234'
tentativas = 10
for c in range (1,11):
    senha = str (input('Digite a senha: '))
    if senha == senha_secreta:
        print ('Senha correta')
        break
    elif senha != senha_secreta:
        print ('Senha incorreta')
        tentativas -= 1
        print (f'Você tem {tentativas} tentativas restantes')
else:
    print ('Acesso negado, você usou todas as suas tentativas')
