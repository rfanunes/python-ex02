altura = float(input("Qual a sua altura? "));
peso = float(input("Qual o seu peso? "));

imc = peso / (altura * altura);

if imc < 18.5:
    print ("Abaixo do peso");
elif imc < 25:
    print ("Você tem um peso normal");
elif imc < 30:
    print ("Você está acima do peso");
elif imc < 35:
    print ("Você tá obeso");
else:
    print ("Você está com obesidade mórbida");

