# Detecta Cor
Programa que faz a identificação de cores.

# Descrição
Esse programa foi escrito na linguagem python e faz a detecção de cores em objetos a partir de uma câmera (webcam) ou de uma imagem. Você consegue escolher como usar e qual cor deseja captar.

# Como funciona?
As funções presentes no código irão receber alguns parâmetros, dentre eles estão:

  * corMinima - é a menor cor que você deseja que o programa capture.
  * corMaxima - é a maior cor que você deseja que o programa capture.
  * corContorno - é a cor que fará o contorno nos objetos que o programa capturar.
  * caminhoImagem* - caso você deseja usar para reconhecer imagem, será necessário passar o caminho para buscar a imagem.

# Instalação
É preciso ter o python instalado no seu computador (<a href="https://www.python.org/downloads/">Python</a>, recomendado baixar a última versão). Para importar algumas funções usadas nesse projeto é preciso fazer a instalação de algumas bibliotecas, são elas:

  * opencv-python - Forma de instalação: <b>pip install opencv-python</b>
  * numpy - Forma de instalação: <b>pip install numpy</b>
  * imutils - Forma de instalação: <b>pip install imutils</b>

<b>Obs.:</b> Essas instalações podem ser feitas pelo terminal do seu computador (necessário que já tenha o python instalado) ou pelo terminal do <a href="https://www.jetbrains.com/pt-br/pycharm/download/">PyCharm</a>, se preferir.

# Uso
Após as instalações, para começar a usar basta clonar esse repositório e digitar o comando <b>python detecta-cor.py</b> no terminal ou rodar pelo PyCharm.

# Cores
Ao longo desse projeto eu testei algumas cores e as deixei comentadas dentro do código para que você possa copiar, colar e fazer seus testes. Essas cores foram:

  * ![#F10000](https://placehold.it/15/F10000/000000?text=+) - <b>corMinima</b> = (0, 100, 100), <b>corMaxima</b> = (15, 255, 255)
  * ![#DA0007](https://placehold.it/15/DA0007/000000?text=+) - <b>corMinima</b> = (140, 100, 100), <b>corMaxima</b> = (180, 255, 255)
  * ![#00FF00](https://placehold.it/15/00FF00/000000?text=+) - <b>corMinima</b> = (38, 100, 100), <b>corMaxima</b> = (75, 255, 255)
  * ![#0000FF](https://placehold.it/15/0000FF/000000?text=+) - <b>corMinima</b> = (100, 100, 100), <b>corMaxima</b> = (130, 255, 255)
  * ![#FFFF00](https://placehold.it/15/FFFF00/000000?text=+) - <b>corMinima</b> = (25, 100, 100), <b>corMaxima</b> = (32, 255, 255)
  * ![#00FFFF](https://placehold.it/15/00FFFF/000000?text=+) - <b>corMinima</b> = (80, 100, 100), <b>corMaxima</b> = (100, 255, 255)
  * ![#FF00FF](https://placehold.it/15/FF00FF/000000?text=+) - <b>corMinima</b> = (140, 100, 100), <b>corMaxima</b> = (180, 255, 255)
  * ![#FFFFFF](https://placehold.it/15/FFFFFF/000000?text=+) - <b>corMinima</b> = (0, 0, 100), <b>corMaxima</b> = (179, 0, 255)
  * ![#FF8000](https://placehold.it/15/FF8000/000000?text=+) - <b>corMinima</b> = (8, 100, 100), <b>corMaxima</b> = (24, 255, 255)

# Exemplos
Alguns exemplos do uso do programa reconhecendo a cor verde de um objeto em vídeo e as cores da logo do <a href="https://opencv.org/">OpenCV</a> em uma imagem.
  
  * Fazendo o reconhecimento em vídeo da cor verde. <br><br>
  ![detecta-cor](https://user-images.githubusercontent.com/60857927/82390444-1a08da80-9a15-11ea-9647-5195238ccb60.gif)
  
  * Fazendo o reconhecimento da cor vermelha. <br><br>
  ![opencv-vermelho-claro](https://user-images.githubusercontent.com/60857927/82385253-0a36c980-9a08-11ea-9172-23879c5b979f.png)
  
  * Fazendo o reconhecimento da cor verde. <br><br>
  ![opencv-verde](https://user-images.githubusercontent.com/60857927/82384815-12dad000-9a07-11ea-97cf-a2cfda23d11e.png)
  
  * Fazendo o reconhecimento da cor azul. <br><br>
  ![opencv-azul](https://user-images.githubusercontent.com/60857927/82385344-3fdbb280-9a08-11ea-9ff8-dfdbb0338201.png)
