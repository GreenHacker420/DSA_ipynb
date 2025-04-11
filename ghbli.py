import cv2
import numpy as np
def ghibli_filter(image_path, output_path="ghibli_output.jpg"):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 800))  # Resize for consistency
    # Step 1: Apply bilateral filter multiple times
    smooth = img.copy()
    for _ in range(5):
        smooth = cv2.bilateralFilter(smooth, d=9, sigmaColor=75, sigmaSpace=75)
    # Step 2: Edge detection for anime outlines
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(edges, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 9, 9)
    # Step 3: Color quantization (using k-means)
    Z = img.reshape((-1, 3))
    Z = np.float32(Z)
    K = 8  # You can tweak this for different styles
    _, label, center = cv2.kmeans(Z, K, None,
                                  (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
                                  10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    quantized = center[label.flatten()]
    quantized = quantized.reshape((img.shape))
    # Step 4: Combine quantized image with edges
    cartoon = cv2.bitwise_and(quantized, quantized, mask=edges)
    # Save and return
    cv2.imwrite(output_path, cartoon)
    return cartoon

image = ghibli_filter('photo.jpg')
while True:
    cv2.imshow('Ghibli Filter', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()