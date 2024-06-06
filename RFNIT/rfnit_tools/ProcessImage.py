import time

import cv2
import os
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
import numpy as np


class ProcessImage:
    def __init__(self, save_directory):
        self.save_directory = save_directory
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Inicializa a câmera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("Erro ao abrir a câmera")

        # Capture and discard some frames to allow the camera to adjust
        for _ in range(10):
            ret, _ = self.cap.read()
            if not ret:
                raise Exception("Falha ao ajustar a câmera")

    def __del__(self):
        # Libera a câmera quando o objeto é destruído
        if self.cap.isOpened():
            self.cap.release()

    def take_photo(self, filename):
        # Capture and discard some frames to allow the camera to adjust
        for _ in range(10):
            ret, frame = self.cap.read()
            if not ret:
                print("Falha ao capturar a imagem")
                return None

        # Capture the final frame to save
        ret, frame = self.cap.read()
        if ret:
            file_path = os.path.join(self.save_directory, filename)
            cv2.imwrite(file_path, frame)
            print(f"Imagem salva em: {file_path}")
            return file_path
        else:
            print("Falha ao capturar a imagem")
            return None

    def compare_images(self, image_path1, image_path2):
        # Load the two images
        image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
        image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

        if image1 is None or image2 is None:
            print("Erro ao carregar as imagens")
            return None

        # Resize images to the same size if they are different
        if image1.shape != image2.shape:
            print("Redimensionando imagens para comparar...")
            image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

        # Compute the Mean Squared Error
        mse_value = mean_squared_error(image1, image2)

        # Compute the Structural Similarity Index (SSIM)
        ssim_value, _ = ssim(image1, image2, full=True)

        print(f"MSE: {mse_value}")
        print(f"SSIM: {ssim_value}")

        return mse_value, ssim_value


# Exemplo de uso
if __name__ == "__main__":
    save_dir = "images"
    processor = ProcessImage(save_dir)

    # Tirar fotos
    processor.take_photo("image1.jpg")
    time.sleep(4)
    processor.take_photo("image2.jpg")
    # time.sleep(4)
    # processor.take_photo("image3.jpg")

    # Comparar imagens
    mse, ssim_index = processor.compare_images(os.path.join(save_dir, "image1.jpg"),
                                               os.path.join(save_dir, "image2.jpg"))
    print(f"Mean Squared Error: {mse}")
    print(f"Structural Similarity Index: {ssim_index}")
