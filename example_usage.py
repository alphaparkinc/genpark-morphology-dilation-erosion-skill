from client import MorphologyDilationErosionEngine

def main():
    morph = MorphologyDilationErosionEngine()
    bin_img = [[0]*7 for _ in range(7)]
    bin_img[3][3] = 255
    dilated = morph.dilate(bin_img)
    print("Morphology Dilation Verification:")
    print(f"Original Foreground Count: 1")
    print(f"Dilated Foreground Count: {sum(row.count(255) for row in dilated)}")

if __name__ == "__main__":
    main()
