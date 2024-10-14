import threading
from PIL import Image, ImageFilter
import time
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def apply_filter(image_path, output_path, filter_function):
    """
    Aplica um filtro a uma imagem e salva a imagem processada.
    """
    logging.info(f'Iniciando processamento da imagem {image_path}')
    start_time = time.time()
    
    # Abrir imagem
    image = Image.open(image_path)
    
    # Aplicar filtro (ex: BLUR ou GRAYSCALE)
    filtered_image = filter_function(image)
    
    # Salvar a imagem processada
    filtered_image.save(output_path)
    
    # Log do tempo de processamento
    end_time = time.time()
    logging.info(f'Imagem {image_path} processada em {end_time - start_time:.2f} segundos e salva como {output_path}')


def filter_grayscale(image):
    """
    Aplica o filtro de escala de cinza.
    """
    return image.convert('L')

def filter_blur(image):
    """
    Aplica o filtro de desfoque.
    """
    return image.filter(ImageFilter.BLUR)

def main():
    # Caminhos das imagens de entrada e saída
    image1_path = 'imagens/image1.jpg'
    image2_path = 'imagens/image2.jpg'
    output1_path = 'resultados/output1.jpg'
    output2_path = 'resultados/output2.jpg'

    # Iniciar threads para processamento paralelo
    thread1 = threading.Thread(target=apply_filter, args=(image1_path, output1_path, filter_grayscale))
    thread2 = threading.Thread(target=apply_filter, args=(image2_path, output2_path, filter_blur))

    start_time = time.time()
    logging.info('Iniciando processamento paralelo das imagens')

    # Iniciar as threads
    thread1.start()
    thread2.start()

    # Aguardar ambas as threads terminarem
    thread1.join()
    thread2.join()

    end_time = time.time()
    logging.info(f'Processamento completo em {end_time - start_time:.2f} segundos')


if __name__ == '__main__':
    main()

