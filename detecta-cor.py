# Projeto Detecção de Cores - Python e OpenCV
# Autor: Iuri Lopes Almeida
# Perfil GitHub: https://github.com/Iuri-Almeida
# Data: 19/05/2020
# Descrição: Esse programa foi escrito na linguagem python e faz a detecção
# 			 de cores em objetos a partir de uma câmera (webcam) ou de uma
# 			 imagem. Você consegue escolher como usar e qual cor deseja captar.
# Forma de uso: python detecta-cor.py


# Cores testadas:
# Foram testadas nesse site: http://alloyui.com/examples/color-picker/hsv
# Obs.: Quanto mais específica for a cor, menor terá que ser a distância 
# 		entre a cor mínima e máxima.

	# vermelho mais claro: corMinima = (0, 100, 100), corMaxima = (15, 255, 255)
	# vermelho mais escuro: corMinima = (140, 100, 100), corMaxima = (180, 255, 255)
	# verde: corMinima = (38, 100, 100), corMaxima = (75, 255, 255)
	# azul: corMinima = (100, 100, 100), corMaxima = (130, 255, 255)
	# amarelo: corMinima = (25, 100, 100), corMaxima = (32, 255, 255)
	# ciano: corMinima = (80, 100, 100), corMaxima = (100, 255, 255)
	# rosa: corMinima = (140, 100, 100), corMaxima = (180, 255, 255)
	# branco: corMinima = (0, 0, 100), corMaxima = (179, 0, 255)
	# laranja: corMinima = (8, 100, 100), corMaxima = (24, 255, 255)


# Importações necessárias para uso.
import cv2
import numpy as np 
import imutils


# Função que fará a detecção da cor em uma imagem.
# corMinima -> é o menor valor de cor que vc deseja captar.
# corMaxima -> é o maior valor de cor que vc deseja captar.
# corContorno -> é a cor que fará o contorno do objeto quando identificado.
# caminhoImagem -> é o local onde está a imagem que quer detectar a cor.
def detectaCorImagem(corMinima, corMaxima, corContorno, caminhoImagem):

	print("[INFO] Iniciando o programa...")
	
	print("[INFO] Lendo a imagem...")

	# Faz a leitura da imagem.
	imagem = cv2.imread(caminhoImagem)
	
	print("[INFO] Aperte qualquer tecla para fechar.")

	# Redimensione o tamanho da imagem.
	# imagem = imutils.resize(imagem, width=600)

	# Converta a cor da imagem de BRG (padrão do OpenCV) para HSV.
	hsv_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

	# Faz a detecção (em HSV) da cor escolhida.
	# Obs.: A máscara pode ser mostrada em uma janela, como a imagem.
	#		Dessa forma vc consegue ver como o HSV funciona.
	# Obs.: O HSV "transforma" em branco a cor escolhida e
	# 		deixa todas as outras cores como preto.
	mascara = cv2.inRange(hsv_imagem, corMinima, corMaxima)

	# Faz algumas alterações na apresentação da imagem, não é obrigatório.
	mascara = cv2.erode(mascara, None, iterations=2)
	mascara = cv2.dilate(mascara, None, iterations=2)

	# Nessa opção o HSV não usa o branco para a cor do objeto e
	# sim a própria cor do objeto.
	# Obs.: Também pode ser mostrada em uma janela, como a imagem.
	mascara_com_cor = cv2.bitwise_and(imagem, imagem, mask=mascara)

	# Pega o número do contorno dos objetos que apareceram na imagem em HSV,
	# e os coloca no contorno_objeto (array). Cada sessão desse array tem as
	# coordenadas (x, y) do objetos encontrados.
	contorno_objeto = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

	# Se o tamanho do array que contém as cores for diferente de 0, ou seja,
	# se existe a identificação de cor.
	# if len(contorno_objeto) != 0:

		# Chama a função que fará o contorno do objeto em forma de retângulo.
		# Obs.: Essa função tenta generalizar todos os pedaços encontrados do objeto
		# 		onde se tem a maior intensidade da cor escolhida.
		# cv2.drawContours(imagem, contornaObjeto(contorno_objeto), 0, corContorno, 2)

	# Desenha um contorno em volta dos objetos encontrados.
	# Obs.: O terceiro pârametro da função drawContours() define qual objeto
	# 		será contronado, sendo o "-1" todos os objetos encontrados com a 
	# 		cor escolhida. O 0 seria o primeiro objeto (sessão do array) 
	# 		encontrado pelo findContours(), o 1 o segundo e assim em diante.
	# Obs.: Diferente do desenho acima, esse desenho faz o contorno extamente
	# 		em todos as áreas onde o programa detectar a cor escolhida. Aí
	# 		depende de vc escolher. :)
	cv2.drawContours(imagem, contorno_objeto, 0, corContorno, 2)

	# Mostra a imagem na tela do computador.

	# Mostra a imagem em RGB.
	cv2.imshow("Cor", imagem)

	# Caso queira salvar a imagem em alguma pasta.
	# cv2.imwrite("imagens/opencv-azul.png", imagem)

	print("[INFO] Imagem lida!")

	# Mostra a imagem em HSV, com a cor do objeto como branca.
	cv2.imshow("Mascara", mascara)

	# Mostra a imagem em HSV, com a cor do objeto.
	# cv2.imshow("Mascara com cor", mascara_com_cor)

	cv2.waitKey(0)

	print("[INFO] Terminando o programa...")

	cv2.destroyAllWindows()


# Função que fará a detecção da cor pela webcam.
# corMinima -> é o menor valor de cor que vc deseja captar.
# corMaxima -> é o maior valor de cor que vc deseja captar.
# corContorno -> é a cor que fará o contorno do objeto quando identificado.
def detectaCorWebcam(corMinima, corMaxima, corContorno):

	print("[INFO] Começando o programa...")

	# Inicia a webcam.
	captura = cv2.VideoCapture(0)

	print("[INFO] Programa iniciado!")

	print("[INFO] Pressione a tecla 'q' para terminar.")

	# Pega cada frame do vídeo.
	# Obs.: Cada loop do "while" é um frame do vídeo.
	while True:

		# Cada frame do vídeo é lido.
		ret, frame = captura.read()

		# Se não houver vídeo, interrompa.
		if not ret:

			print("Erro ao carregar o vídeo!")

			break

		# Redimensione o tamanho do frame.
		frame = imutils.resize(frame, width=600)

		# Converta a cor do frame de BRG (padrão do OpenCV) para HSV.
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# Faz a detecção (em HSV) da cor escolhida.
		# Obs.: A máscara pode ser mostrada em uma janela, como o frame.
		#		Dessa forma vc consegue ver como o HSV funciona.
		# Obs.: O HSV "transforma" em branco a cor escolhida e
		# 		deixa todas as outras cores como preto.
		mascara = cv2.inRange(hsv_frame, corMinima, corMaxima)

		# Faz algumas alterações na apresentação da imagem, não é obrigatório.
		mascara = cv2.erode(mascara, None, iterations=2)
		mascara = cv2.dilate(mascara, None, iterations=2)

		# Nessa opção o HSV não usa o branco para a cor do objeto e
		# sim a própria cor do objeto.
		# Obs.: Também pode ser mostrada em uma janela, como o frame.
		mascara_com_cor = cv2.bitwise_and(frame, frame, mask=mascara)

		# Pega o número do contorno dos objetos que apareceram na imagem em HSV,
		# e os coloca no contorno_objeto (array). Cada sessão desse array tem as
		# coordenadas (x, y) do objetos encontrados.
		contorno_objeto = cv2.findContours(mascara.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

		# Se o tamanho do array que contém as cores for diferente de 0, ou seja,
		# se existe a identificação de cor.
		if len(contorno_objeto) != 0:

			# Chama a função que fará o contorno do objeto em forma de retângulo.
			# Obs.: Essa função tenta generalizar todos os pedaços encontrados do objeto
			# 		onde se tem a maior intensidade da cor escolhida.
			cv2.drawContours(frame, contornaObjeto(contorno_objeto), 0, corContorno, 2)

		# Desenha um contorno em volta dos objetos encontrados.
		# Obs.: O terceiro pârametro da função drawContours() define qual objeto
		# 		será contronado, sendo o "-1" todos os objetos encontrados com a 
		# 		cor escolhida. O 0 seria o primeiro objeto (sessão do array) 
		# 		encontrado pelo findContours(), o 1 o segundo e assim em diante.
		# Obs.: Diferente do desenho acima, esse desenho faz o contorno extamente
		# 		em todos as áreas onde o programa detectar a cor escolhida. Aí
		# 		depende de vc escolher. :)
		# cv2.drawContours(frame, contorno_objeto, 0, corContorno, 2)

		# Mostra a imagem na tela do computador.

		# Mostra a imagem em RGB.
		cv2.imshow("Cor", frame)

		# Mostra a imagem em HSV, com a cor do objeto como branca.
		# cv2.imshow("Mascara", mascara)

		# Mostra a imagem em HSV, com a cor do objeto.
		# cv2.imshow("Mascara com cor", mascara_com_cor)

		# Condição para terminar o programa. Se a letra "q" do teclado
		# for apertada, o programa será encerrado.
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break

	print("[INFO] Terminando o programa...")

	# Liberando a captura da webcam e fechando todas as janelas abertas.
	captura.release()
	cv2.destroyAllWindows()


# Função que recebe um array contendo as coordenadas dos objetos detectados e seleciona
# a área com maior intensidade da cor escolhida. Além disso, seleciona encaixa o objeto 
# no menor retângulo possível e então retorna as coordenadas desse retângulo.
# Obs.: Como essa função seleciona o local onde tem a maior intensidade da cor, só vai
# 		fazer o reconhecimento de um objeto.
# objeto -> é um array que contém as coordenadas de todos os objetos detectados.
def contornaObjeto(objeto):

	# Retorna o máximo item escolhido pela "key". O parâmetro "key" é opcional e
	# pode ser escolhido como área, números, letras, ...
	area_cor_max = max(objeto, key=cv2.contourArea)

	# Retorna a menor área delimitando o retângulo em volta do objeto.
	# Obs.: A função minAreaRect() coloca a imagem no menor retângulo possível que
	# 		ela possa ocupar.
	# 		É retornado o (centro da imagem, (altura e largura), ângulo de rotação).
	area_min = cv2.minAreaRect(area_cor_max)

	# Desenha esse mínimo quadrado que foi delimitado pela função minAreaRect().
	vertices_retangulo = cv2.boxPoints(area_min)

	# Pega os vértices do retângulo desenhado e faz a indexação desses valores.
	# Obs.: Contém a localização dos vértices do menor retângulo desenhado em
	# 		volta da imagem.
	vertices_retangulo = np.int0(vertices_retangulo)

	return [vertices_retangulo]


# Função principal que chamará todas as outras funções.
def main():

	# Aqui vc passa a cor que deseja detectar, com a sua cor
	# mínima e máxima (1º e 2º parâmetros). Alguma dessas cores
	# foram testadas e estão no início do código, só copiar e colar. :)
	# Vc também pode escolher a cor (3º parâmetro) que fará o contorno do objeto.
	# No caso da imagem (4º parâmetro), vc precisará passar o caminho onde a imagem
	# está armazenada.
	
	# Escolha sua opção. :)
	corMinima = (25, 100, 100)
	corMaxima = (32, 255, 255)
	corContorno = (255, 255, 255)
	# caminhoImagem = "imagens/opencv-logo.png"
	
	# Chamando a função para detectar a cor pela webcam.
	detectaCorWebcam(corMinima, corMaxima, corContorno)

	# Chamando a função para detectar a cor em uma imagem.
	# detectaCorImagem(corMinima, corMaxima, corContorno, caminhoImagem)


if __name__ == "__main__":
	main()
