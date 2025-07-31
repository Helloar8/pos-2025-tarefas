resultado = client.service.NumberToWords(ubiNum=numero)
try:
    print(f"O número {num} por extenso em inglês é: {resultado}")
    print(f"O número {numero} por extenso em inglês é: {resultado}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")